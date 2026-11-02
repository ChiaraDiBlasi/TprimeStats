import ROOT
#import cmsstyle as CMS
from array import array
import numpy as np
from samples import *
import subprocess
import argparse
import json
import sys
ROOT.gROOT.SetBatch()


parser = argparse.ArgumentParser(description="Collect histograms for one era")
parser.add_argument("-e", "--era",                                                        default="2022",             help="Era to process, e.g. 2022, 2022EE, 2022+2023, etc.")
parser.add_argument('-j', '--jsonInput',          dest='jsonInput',       type=str,       default="settings.json",    help='json file containing the settings')
parser.add_argument('-u', '--unblind',            dest='unblind',         action='store_true',    default=False,              help='Unblind')
parser.add_argument('-s','--suffix',                   dest='suffix',          type=str,               default="",               help='suffix to add to histo.root file name (e.g. histo2022_<suffix>.root)')
parser.add_argument('-R','--readOnly',            dest='readOnly',         action='store_true',    default=False,              help='read only mode-do not repeat the fit ')

opt = parser.parse_args()
with open(opt.jsonInput) as file:
    print("Opening JSON file {}".format(opt.jsonInput))
    jsoninput   = json.load(file)
lumi_dict                           = jsoninput["lumi_dict"]
lumi_dict["2022+2023"]              = lumi_dict["2022"] + lumi_dict["2023"]
lumi_dict["2022+2023+2024"]         = lumi_dict["2022"] + lumi_dict["2023"] + lumi_dict["2024"]



era                                 = opt.era
lumi                                = lumi_dict[era]
outputFolderPath                    = jsoninput["dc-folder"][era]
signals                             = jsoninput["processes"]["signals"]

signalsSubset=[]
suffix= opt.suffix if opt.suffix=="" else "_"+opt.suffix
blindlabel= "_obs_" if opt.unblind else "" 
combineOptions="" 

print ("suffix is", suffix)
def RunCombine_Limits(signal,doLaunch=True):
    print("Reading combine output for signal", signal)
#    m = str(int(mass*10**3))
    dcFolderPath   = f'{jsoninput["dc-folder"][era]}/{signal}{suffix}'
    if(doLaunch):
        combinecommand = f"combine -M AsymptoticLimits -d {dcFolderPath}/{signal}.txt {combineOptions} > {dcFolderPath}/out.log"
        subprocess.run(f"cd {dcFolderPath} && {combinecommand}", shell=True, check=True)
    else:subprocess.run(f"cd {dcFolderPath}", shell=True, check=True)
    with open(f"{dcFolderPath}/out.log") as f:
        lines = f.readlines()
    for line in lines:
        print (line)
        if "50.0%" in line:
            expected = float(line.split()[-1])
        elif "16.0%" in line:
            expected_16 = float(line.split()[-1])
        elif "84.0%" in line:
            expected_84 = float(line.split()[-1])
        elif "2.5%" in line:
            expected_2_5 = float(line.split()[-1])
        elif "97.5%" in line:
            expected_97_5 = float(line.split()[-1])
    return expected_2_5, expected_16, expected, expected_84, expected_97_5


Resultdict= {}
launchLimits=not opt.readOnly

for ns in range(len(signals)):
    s= signals[ns]
    try: values=(RunCombine_Limits(s,doLaunch=launchLimits))
    except:
        if(ns>0):
            print(f"warning! Fit for signal {s} did not produce limit output! Using{signals[ns-1]} instead")
            Resultdict[s]=Resultdict[signals[ns-1]]#values=(RunCombine_Limits(signals[ns-1],doLaunch=launchLimits))
        else:
            print("warning! first fit failed - exiting")
            sys.exit(1)
    Resultdict[s]=values
    
namejson="Limits_"+era+blindlabel+suffix+".json"

with open(f"{outputFolderPath}/{namejson}",'w') as fp:
    json.dump(Resultdict,fp)
