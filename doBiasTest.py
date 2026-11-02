#!/usr/bin/env python3
import argparse
import json
import os, sys
import ROOT
import cmsstyle as CMS
import subprocess

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptFit(0)

parser = argparse.ArgumentParser(description="Perform bias test")
parser.add_argument("-e", "--era",                      dest="era",                                         default="2022",                 help="Era to process, e.g. 2022, 2022EE, 2022+2023, etc.")
parser.add_argument("-j", "--jsonInput",                dest="jsonInput",                                   default="settings.json",        help="Settings JSON file")
parser.add_argument("-m", "--massPoint",                dest="massPoint",               type=int,           default=700,                    help="Tprime mass point")
parser.add_argument("-t", "--toys",                     dest="toys",                    type=int,           default=1000,                   help="Number of toys")
parser.add_argument("-s", "--seed",                     dest="seed",                    type=int,           default=123456,                 help="Random seed")
parser.add_argument(      "--suffix",                 dest="suffix",                                      default="",                     help="Suffix of the datacard folder (e.g. TprimeToTZ_700_<suffix>)")
parser.add_argument('--sigpath',        dest='sigpath',         type=str,   default = '',                                   help='Input the signal path as an argument rather than deriving it here')
parser.add_argument('--signal',        dest='signal',         type=str,   default = '',                                   help='Input the signal as well')
args   = parser.parse_args()

with open(args.jsonInput) as file:
    jsoninput = json.load(file)


era             = args.era
mass            = args.massPoint
toys            = args.toys
seed            = args.seed
extraFitOptions = ""
lumi            = jsoninput["lumi_dict"][era]
signal          = f"TprimeToTZ_{mass}" if args.signal =='' else args.signal  
dc_folder       = jsoninput["dc-folder"][era]
sig_folder      = f"{dc_folder}/{signal}{f'_{opt.suffix}' if opt.suffix else ''}" if args.sigpath=='' else args.sigpath 



def read_combineOutput(sig_folder,signal_loc,mass=700):
    dc_folder=sig_folder
    sig_loc=signal_loc
    subprocess.run(f"combine -M AsymptoticLimits -d {dc_folder}/{sig_loc}.txt > out.log", shell=True, check=True, cwd=dc_folder)
    r_dict          = {
                        "expected_2p5":  None,
                        "expected_16p0": None,
                        "expected_50p0": None,
                        "expected_84p0": None,
                        "expected_97p5": None
                    }
    with open(f"{dc_folder}/out.log") as f:
        lines = f.readlines()
        for line in lines:
            if "50.0%" in line:
                r_dict["expected_50p0"] = float(line.split()[-1])
            elif "16.0%" in line:
                r_dict["expected_16p0"] = float(line.split()[-1])
            elif "84.0%" in line:
                r_dict["expected_84p0"] = float(line.split()[-1])
            elif "2.5%" in line:
                r_dict["expected_2p5"]  = float(line.split()[-1])
            elif "97.5%" in line:
                r_dict["expected_97p5"] = float(line.split()[-1])

    return r_dict





print(f"Performing bias test for mass {mass} GeV")
r_dict              = read_combineOutput(sig_folder=sig_folder,signal_loc=signal,mass=mass)
r_dict['BOnly']     = 0
r_dict['rNominal']  = 1
print(f"Results for mass {mass} GeV:")
print(f"    rBOnly:             {r_dict['BOnly']}")
print(f"    rNominal:           {r_dict['rNominal']}")
print(f"    rExpected 16%:      {r_dict['expected_16p0']}")
print(f"    rExpected 50%:      {r_dict['expected_50p0']}")
print(f"    rExpected 84%:      {r_dict['expected_84p0']}")


#bias_dir = f"{jsoninput['dc-folder'][era]}/TprimeToTZ_{mass}{f'_{args.suffix}' if args.suffix else ''}/bias/"
bias_dir = f"{sig_folder}/bias/"
if not os.path.exists(bias_dir):
    os.makedirs(bias_dir)

    subprocess.run(f"text2workspace.py ../{signal}.txt -m 125 -o workspace_{signal}.root", shell=True, check=True, cwd=bias_dir)

for key, injected_signal in r_dict.items():
    bias_subdir     = f"{bias_dir}/{key}/"
    plot_name       = f"pulls_{key}_r{injected_signal}_{mass}"
    if not os.path.exists(bias_subdir):
        os.makedirs(bias_subdir)
    genOptions      = f"--saveToys --toysFrequentist --bypassFrequentistFit -t {toys} -s {seed} --expectSignal {injected_signal} --rMin -250 --rMax 250"
    fitOptions      = f"--skipBOnlyFit --rMin -250 --rMax 250 -t {toys} -s {seed} --toysFile higgsCombine.{key}_r{injected_signal}_M{mass}.GenerateOnly.mH125.{seed}.root {extraFitOptions}"

    genCommand      = f"combine -M GenerateOnly -d ../workspace_{signal}.root -m 125 {genOptions} -n .{key}_r{injected_signal}_M{mass}"
    fitCommand      = f"combine -M FitDiagnostics -d ../workspace_{signal}.root -m 125 {fitOptions} -n .{key}_r{injected_signal}_M{mass}"
    # print(f"Running: {genCommand}")
    # print(f"Running: {fitCommand}")
    subprocess.run(genCommand, shell=True, check=True, cwd=bias_subdir)
    subprocess.run(fitCommand, shell=True, check=True, cwd=bias_subdir)
    

    #### PLOT ####
    inFilePath  = f"{bias_subdir}/fitDiagnostics.{key}_r{injected_signal}_M{mass}.root"
    CMS.SetExtraText("Work in progress")
    CMS.SetLumi(lumi, run=None)
    CMS.SetEnergy(13.6)

    f           = ROOT.TFile.Open(inFilePath)
    tmp         = f.Get("tree_fit_sb").Clone()
    h           = ROOT.TH1F(f"h_{plot_name}","",20,-4,4)
    successful_fits = int(tmp.Project(h.GetName(),f"(r-{injected_signal})/rErr","fit_status==0"))
    func        = ROOT.TF1(f"gaus_{plot_name}", "gaus(0)", -2, 2)
    h.Fit(func, "R")

    c1 = CMS.cmsCanvas(
        f"c1_{plot_name}",
        -4,
        4,
        0,
        1.6 * h.GetMaximum(),
        "(r - r_{Truth}) / #sigma_{r}",
        "Pseudo-experiments",
        square=True,
        extraSpace=0.01,
        iPos=0
    )

    red     = ROOT.TColor.GetColor("#e42536")
    CMS.cmsDraw(h,"E",marker=ROOT.kFullCircle,msize=1.0,lwidth=2,fstyle=0)
    CMS.cmsDraw(func,"L",lwidth=2,lcolor=red,fstyle=0)

    mean    = func.GetParameter(1)
    sigma   = func.GetParameter(2)

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextFont(42)
    latex.SetTextSize(0.04)

    legend = CMS.cmsLeg(0.48, 0.77, 0.90, 0.92, textSize=0.035)
    legend.AddEntry(h,              f"Pseudo-experiments ({successful_fits})",         "lep")
    legend.AddEntry(func,           f"Fit: #mu = {mean:.3f}, #sigma = {sigma:.3f}",    "l")
    legend.AddEntry(ROOT.nullptr,   f"r_{{Truth}} = {injected_signal}",                "")
    legend.Draw()

    c1.Update()
    c1.SaveAs(f"{bias_subdir}/{plot_name}.png")
    c1.SaveAs(f"{bias_subdir}/{plot_name}.pdf")
    c1.Close()
    f.Close()
