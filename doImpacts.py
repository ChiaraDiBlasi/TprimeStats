import subprocess
import os
import optparse
import json

usage  = 'python3 doImpacts.py'
parser = optparse.OptionParser(usage)
parser.add_option('-e', '--era',        dest='era',         type=str,   default = '2022',                                   help='Please enter the era of the datacard, if not specified the code will take the era 2022')
parser.add_option('-m', '--massPoint',                      type=int,   default = 700,                                      help='Please enter the mass point of the datacard, if not specified the code will take the mass point 700')
parser.add_option("-j", "--jsonInput",                                  default = "settings.json",                          help="Settings JSON file")
parser.add_option(      '--FitOption',  dest='FitOption',   type=str,   default = "--robustFit 1 -t -1 --setParameterRanges r=-100,100",  help='Please enter the fit option, if not specified the code will take the fit option -t -1')
parser.add_option(      '--suffix',     dest='suffix',      type=str,   default = "",                                     help='Suffix of the datacard folder (e.g. TprimeToTZ_700_<suffix>)')
parser.add_option('--sigpath',        dest='sigpath',         type=str,   default = '',                                   help='Input the signal path as an argument rather than deriving it here')
parser.add_option('--signal',        dest='signal',         type=str,   default = '',                                   help='Input the signal as well')
(opt, args) = parser.parse_args()


with open(opt.jsonInput) as file:
    jsoninput = json.load(file)

era             = opt.era
mass            = str(opt.massPoint)
FitOption       = opt.FitOption
dc_folder       = jsoninput["dc-folder"][era]
sig_folder      = f"{dc_folder}/TprimeToTZ_{mass}{f'_{opt.suffix}' if opt.suffix else ''}" if opt.sigpath=='' else opt.sigpath 
impact_dir      = f"{sig_folder}/impacts/"
signal          = f"TprimeToTZ_{mass}" if opt.signal =='' else opt.signal  

print("Running impacts for era: {}, mass: {}, FitOption: {}".format(era, mass, FitOption))

if not os.path.exists(impact_dir):
    os.makedirs(impact_dir)
# subprocess.run("pwd")
# Change working directory for subsequent commands by using cwd parameter in subprocess.run
print("impact dir is ",impact_dir)
subprocess.run(f"text2workspace.py ../{signal}.txt -m 125 -o workspace_{signal}.root",                     shell=True, check=True, cwd=impact_dir)
subprocess.run(f"combineTool.py -M Impacts -d workspace_{signal}.root -m 125 --doInitialFit {FitOption}",           shell=True, check=True, cwd=impact_dir)
subprocess.run(f"combineTool.py -M Impacts -d workspace_{signal}.root -m 125 --doFit {FitOption} --parallel 50",    shell=True, check=True, cwd=impact_dir)
subprocess.run(f"combineTool.py -M Impacts -d workspace_{signal}.root -m 125 -o impact.json",                       shell=True, check=True, cwd=impact_dir)
subprocess.run(f"plotImpacts.py -i impact.json -o impacts --summary",                                                        shell=True, check=True, cwd=impact_dir)
