#!/usr/bin/env python3

import argparse, json, math, os, ROOT
from array import array
import sys
import subprocess

parser = argparse.ArgumentParser(description="Collect histograms for one era")
parser.add_argument("-e", "--era",              default="2022",                 help="Era to process, e.g. 2022, 2022EE, 2022+2023, etc.")
parser.add_argument("-j", "--jsonInput",        default="settings.json",        help="Settings JSON file")
parser.add_argument("-u", "--unblind",          action="store_true",            help="Use real data in every category, overriding the per-category data-source flags")
parser.add_argument("--addSyst",                action="store_true",            help="Collect shape systematics")
parser.add_argument("-s", "--suffix",           default="",                     help="Suffix for the output file name (e.g. histo2023_<suffix>.root)")
opt = parser.parse_args()

dorebin=False

def SampleFiles(sample, era):
    from samples import sample_dict
    d = sample_dict[f"{sample}_{era}"]
    return [f"{c.label}.root" for c in getattr(d, "components", [d])]

def CollectHistos(inputEosFolder, outFolderPath, jsonInput, era, unblind=False, addSyst=False, suffix=""):
    inputEosFolder  = inputEosFolder.rstrip("/")
    outFolderPath   = outFolderPath.rstrip("/")
    lumi            = jsonInput["lumi_dict"][era]
    outFilePath     = f"{outFolderPath}/histo{era}{f'_{suffix}' if suffix else ''}.root"
    var             = jsonInput["variable"]
    bins            = [(name, useRealData) for name, useRealData in jsonInput["categories"]]
    backgrounds     = jsonInput["processes"]["backgrounds"]
    signals         = jsonInput["processes"]["signals"]
    processFiles    = {p: SampleFiles(jsonInput["samples"][p], era) for p in backgrounds + signals}
    dataFiles       = SampleFiles(jsonInput["samples"]["Data"], era)
    missingFiles    = [f for f in dataFiles + sum(processFiles.values(), []) if not os.path.exists(f"{inputEosFolder}/{f}")]
    if missingFiles: raise RuntimeError(f"Missing input files in {inputEosFolder}: {missingFiles}")
    all_processes   = backgrounds + signals
    systs           = [("nominal", "nominal", all_processes)]
    if addSyst:
        for syst in jsonInput["systematics"].values():
            if syst["type"] != "shape":
                continue

            target_processes = syst["processes"]
            if target_processes == "":
                target_processes = all_processes
            elif isinstance(target_processes, str):
                target_processes = [target_processes]

            systs += [
                (f"{syst['branchRootFile']}_up", f"{syst['name']}Up", target_processes),
                (f"{syst['branchRootFile']}_down", f"{syst['name']}Down", target_processes),
            ]

    os.makedirs(outFolderPath, exist_ok=True)
    output              = ROOT.TFile(outFilePath, "RECREATE")
    xbins               = array("d", [500, 600, 700, 800, 1000, 1400, 2000])
    nominalHistos       = {}
    componentIntegrals  = {}
    summaryInfo         = {}
    
    ##### Collect MONTECARLO histograms #####
    for inputSyst, outputSyst, target_processes in systs:
        for process, processFileList in processFiles.items():
            if process not in target_processes:
                continue
            for region, useRealData in bins:
                h_out                           = None
                inputName                       = f"{var}_{region}_{inputSyst}"
                outputName                      = f"hist_{process}_{region}_{outputSyst}"
                componentIntegrals[outputName]  = []
                summaryInfo[outputName]         = (region, outputSyst, process)
                for i, f in enumerate(processFileList):
                    inputFile                   = ROOT.TFile.Open(f"{inputEosFolder}/{f}")
                    print(process, region, inputName, f)
                    tmp                         = inputFile.Get(inputName)
                    tmp                         = tmp.Clone(f"{outputName}_source{i}")
                    tmp.SetDirectory(0)
                    inputFile.Close()
                    tmp.Scale(lumi)
                    if(dorebin):tmp                         = tmp.Rebin(len(xbins)-1, f"{outputName}_rebin{i}", xbins)
                    tmp.SetDirectory(0)
                    componentIntegrals[outputName].append((f, tmp.Integral()))
                    
                    if h_out is None:
                        h_out                   = tmp.Clone(outputName)
                        h_out.SetDirectory(0)
                    else:
                        h_out.Add(tmp)
                output.cd()
                print(f"Wrote {outputName}: integral={h_out.Integral():.6f}")
                h_out.Write()
                if inputSyst == "nominal":
                    nominalHistos[(process, region)] = h_out.Clone()
                nominalHistos[(process, region)].SetDirectory(0)
    print(componentIntegrals)

    ##### Collect DATA histograms #####
    for region, useRealData in bins:
        outputName                      = f"hist_data_obs_{region}_nominal"
        h_out                           = None
        componentIntegrals[outputName]  = []
        summaryInfo[outputName]         = (region, "nominal", "data_obs")
        if unblind or useRealData:
            if not dataFiles: raise RuntimeError("No data ROOT files found")
            inputName = f"{var}_{region}"
            for i, f in enumerate(dataFiles):
                input = ROOT.TFile.Open(f"{inputEosFolder}/{f}")
                tmp = input.Get(inputName)
                if not tmp:
                    input.Close()
                    raise RuntimeError(f"Histogram {inputName} not found in {inputEosFolder}/{f}")
                tmp = tmp.Clone(f"{outputName}_source{i}")
                tmp.SetDirectory(0)
                input.Close()
                if(dorebin):tmp = tmp.Rebin(len(xbins)-1, f"{outputName}_rebin{i}", xbins)
                tmp.SetDirectory(0)
                componentIntegrals[outputName].append((f, tmp.Integral()))
                if h_out is None: h_out = tmp.Clone(outputName); h_out.SetDirectory(0)
                else: h_out.Add(tmp)
        else:
            for process in backgrounds:
                tmp = nominalHistos[(process, region)]
                if h_out is None: h_out = tmp.Clone(outputName); h_out.SetDirectory(0)
                else: h_out.Add(tmp)
                inputName = f"hist_{process}_{region}_nominal"
                componentIntegrals[outputName] += [(f"{process}: {f}", integral) for f, integral in componentIntegrals[inputName]]
        output.cd()
        h_out.Write()

    output.Close()
    output                  = ROOT.TFile.Open(outFilePath, "READ")
    validationErrors        = 0
    for outputName, components in componentIntegrals.items():
        histogram           = output.Get(outputName)
        if not histogram:
            print(f"ERROR {outputName}: histogram is missing from the output file")
            validationErrors += 1
            continue
        region, systematic, process = summaryInfo[outputName]
        componentSum                = sum(integral for _, integral in components)
        finalIntegral               = histogram.Integral()
        integralOK                  = math.isclose(componentSum, finalIntegral, rel_tol=1e-9, abs_tol=1e-9)
        print(f"\nSUMMARY region={region} systematic={systematic} process={process}")
        for component, integral in components:
            print(f"  {component:<55} {integral:>16.6f}")
        print(f"  {'SUM OF COMPONENTS':<55} {componentSum:>16.6f}")
        print(f"  {'FINAL HISTOGRAM':<55} {finalIntegral:>16.6f}")
        print(f"  RESULT: {'PASS' if integralOK else 'FAIL'}")
        if not integralOK:
            validationErrors += 1
    output.Close()
    if validationErrors: raise RuntimeError(f"Histogram integral validation failed for {validationErrors} histograms")
    print(f"Created {outFilePath}")

def HaddHistos(era, outFolderPath, jsonInput, suffix=""):
    sub_eras        = era.split("+")
    outFolderPath   = outFolderPath.rstrip("/")
    os.makedirs(outFolderPath, exist_ok=True)
    histoName       = lambda e: f"histo{e}{f'_{suffix}' if suffix else ''}.root"
    outFilePath     = f"{outFolderPath}/{histoName(era)}"
    for sub_era in sub_eras:
        inFilePath  = f"{jsonInput['dc-folder'][sub_era]}/{histoName(sub_era)}"
        if not os.path.exists(inFilePath):
            raise RuntimeError(f"Missing {histoName(sub_era)} file for era {sub_era} in folder {jsonInput['dc-folder'][sub_era]}. Please run CollectHistos.py for era {sub_era} first.")
    haddCommand = f"hadd -f {outFilePath} " + " ".join([f"{jsonInput['dc-folder'][sub_era]}/{histoName(sub_era)}" for sub_era in sub_eras])
    print(f"Running command: {haddCommand}")
    result = subprocess.run(haddCommand, shell=True)




if __name__ == "__main__":
    with open(opt.jsonInput) as file:
        jsonInput = json.load(file)

    if "+" in opt.era:
        HaddHistos(opt.era, jsonInput["dc-folder"][opt.era], jsonInput, opt.suffix)
    else:    
        CollectHistos(jsonInput["plots-folder"][opt.era], jsonInput["dc-folder"][opt.era], jsonInput, opt.era, opt.unblind, opt.addSyst, opt.suffix)
