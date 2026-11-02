import CombineHarvester.CombineTools.ch as ch
import optparse
import json, os
from array import array
import sys

usage = 'python3 CreateDatacards.py -e 2023 -j settings.json --addSyst --addMCStat'
parser = optparse.OptionParser(usage)
parser.add_option('-e', '--era',                dest='era',             type=str,               default="2022",             help='insert era (e.g. 2022, 2022EE)')
parser.add_option('-j', '--jsonInput',          dest='jsonInput',       type=str,               default="settings.json",    help='json file containing the settings')
parser.add_option('-u', '--unblind',            dest='unblind',         action='store_true',    default=False,              help='Unblind')
# parser.add_option('-s', '--singledatacards',    dest='singledatacards', action='store_true',    default=False,              help='Write single datacards per each bin')
parser.add_option('--addSyst',                  dest='addSyst',         action='store_true',    default=False,              help='add Systematics in the datacards')
parser.add_option('--addMCStat',                dest='addMCStat',       action='store_true',    default=False,              help='add auto MC Stat in the datacards')
parser.add_option('-s','--suffix',                   dest='suffix',          type=str,               default=None,               help='suffix to add to histo.root file name (e.g. histo2022_<suffix>.root)')
parser.add_option('-v', '--variant',       type=str,               default='',                 help='Suffix labelling the variant at datacard level)')

(opt, args)     = parser.parse_args()
# Open JSON file
with open(opt.jsonInput) as file:
    print("Opening JSON file {}".format(opt.jsonInput))
    jsoninput   = json.load(file)


era             = opt.era
unblind         = opt.unblind
suffix          = opt.suffix  if opt.suffix is not None else ""
variant         = opt.variant if opt.variant is not None else ""
suffix_dc       = "_".join(s for s in [suffix, variant ] if s)   # suffix for the datacard-level variation
outFolderPath   = jsoninput["dc-folder"][era]

def writeSingleDatacards():
    return 0

def writeTotalDatacard(jsoninput, era, unblind, sig, suffix="", suffix_dc=""):
    cb = ch.CombineHarvester()
    cb.SetVerbosity(3)

    cats = [(i, cat) for i, (cat, useRealData) in enumerate(jsoninput["categories"])]
    print("categories are : " ,cats)
    backgrounds = jsoninput["processes"]["backgrounds"]
    # signals = jsoninput["processes"]["signals"]
    signals = [sig]

    # if unblind:
    cb.AddObservations( ["*"], ["TprimeToTZ"], ["13.6TeV"], ["jets+MET"],          cats)
    # ['*'], ['my_analysis'], ['13TeV'], ['my_category']
    cb.AddProcesses( ["*"], ["TprimeToTZ"], ["13.6TeV"], ["jets+MET"], backgrounds, cats, False)
    cb.AddProcesses( ["*"], ["TprimeToTZ"], ["13.6TeV"], ["jets+MET"], signals, cats, True)


    inputShapePath = f"{outFolderPath}/histo{era}{f'_{suffix}' if suffix else ''}.root"
    print(f"Using shape input file: {inputShapePath}")

    # Add systematics
    if opt.addSyst:
        print("Systematics to be added: ", jsoninput["systematics"].keys())
        for s in jsoninput["systematics"].keys():
            name        = jsoninput["systematics"][s]["name"]
            processes   = jsoninput["systematics"][s]["processes"]
            bins        = jsoninput["systematics"][s]["bin"]
            type        = jsoninput["systematics"][s]["type"]
            syst_value  = jsoninput["systematics"][s]["value"]
            if isinstance(syst_value, dict):
                value = syst_value[era]
            else:
                value = syst_value

            if processes == "" and bins == "":
                cb.cp().process(backgrounds+signals).AddSyst(cb, name, type, ch.SystMap()(value))
            elif processes == "" and bins != "":
                cb.cp().process(backgrounds+signals).bin([bins]).AddSyst(cb, name, type, ch.SystMap()(value))
            elif processes != "" and bins == "":
                cb.cp().process(processes).AddSyst(cb, name, type, ch.SystMap()(value))
            else:
                cb.cp().process(processes).bin(bins).AddSyst(cb, name, type, ch.SystMap()(value))

        cb.ExtractShapes(inputShapePath,
                        "hist_$PROCESS_$BIN_nominal", # nominal isto saved in histo2022.root as hist_"sample"_"region"
                        "hist_$PROCESS_$BIN_$SYSTEMATIC") # syst hist_$PROCESS_$BIN_$SYSTEMATIC
    else:
        cb.ExtractShapes(inputShapePath,
                        "hist_$PROCESS_$BIN_nominal","") # nominal isto saved in histo2022.root as hist_"sample"_"region"

    cb.PrintAll()
    sigFolderPath = f"{outFolderPath}/{sig}{f'_{suffix_dc}' if suffix else ''}"
    print(sigFolderPath)
    if not os.path.exists(sigFolderPath):
        os.makedirs(sigFolderPath)
    cb.WriteDatacard(f"{sigFolderPath}/{sig}.txt", f"{sigFolderPath}/{sig}.root")
    with open(f"{sigFolderPath}/datacard_metadata.json", "w") as metadataFile:
        json.dump(
            {
                "era": era,
                "signal": sig,
                "categories": [cat for cat, _ in jsoninput["categories"]],
                "shape_input": inputShapePath,
                "suffix": suffix_dc,
            },
            metadataFile,
            indent=2,
            sort_keys=True,
        )
    print(f"{sigFolderPath}/datacard_metadata.json")
    if opt.addMCStat:
        with open(f"{sigFolderPath}/{sig}.txt", "a") as f:
            f.write("* autoMCStats 0 0 1\n")

if __name__ == "__main__":
    # print("ATTENTION the UNBLIND option is set to {}".format(unblind))
    # if inputEosFolder!="":
    #     print("Collecting data from {} in histo{}.root".format(inputEosFolder, era))
    #     CollectHistos(inputEosFolder, outFolderPath, jsoninput, era)
    # Call the appropriate function based on the value of singledatacards
    # if opt.singledatacards:
    #     writeSingleDatacards()
    # else:
    #     print(jsoninput["processes"]["signals"])
    #     for sig in jsoninput["processes"]["signals"]:
    #         print(sig)
    #         writeTotalDatacard(jsoninput, era, unblind, sig)

    print(jsoninput["processes"]["signals"])
    for sig in jsoninput["processes"]["signals"]:
        print(sig)
        writeTotalDatacard(jsoninput, era, unblind, sig, suffix=suffix, suffix_dc=suffix_dc)
