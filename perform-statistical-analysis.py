import subprocess
import json
import argparse
import os
import shutil
from utils import unpackLabel

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-e', '--era',          type=str,               default='2023',             help='Era of the datacard')
parser.add_argument('-j', '--jsonInput',    type=str,               default='settings.json',    help='Settings JSON file')
#parser.add_argument('-p', '--positive',     action="store_true",                                help='Fix zero bin contents in histograms')
parser.add_argument("-u", "--unblind",      action="store_true",                                help="Use data instead of the background sum")
parser.add_argument('-s', '--suffix',       type=str,               default='',                 help='Suffix labelling the whole run (e.g. histo2023_<suffix>.root)')
parser.add_argument('-m', '--mode',       type=str,               default='csmdlpbig',                 help='Operation mode - each letter activates one part: c=collect histos; s=symmetrize jesTotal/jer; m=make positive /fix histograms, d=datacard creation, l=limit evaluation, p=plot limit (brazil plot), i=impacts, g=gof')
parser.add_argument('--dryrun',       action="store_true", default=False,                 help='just get run the commands file without executing them')
parser.add_argument('--verbose',       type=int,               default=0,                 help='Verbosity level')
parser.add_argument('-v', '--variant',       type=str,               default='',                 help='Suffix labelling the variant at datacard level)')
args = parser.parse_args()


#--mode: c-collect z-fixzeros/systss d-createdatacard m-makepositive l-limits p-plotbrazil i-impacts b-bias g-gof ; nessuno: fa tutto

era             = args.era
unblind         = "--unblind" if args.unblind else ""
histo_suffix    = args.suffix                                                       # suffix of histo<era>_<suffix>.root
sym_suffix      = "_".join(s for s in [args.suffix, "symmetrized" if "s" in args.mode else ""] if s)  # suffix of histo<era>_<suffix>_symmetrized.root
suffix          = "_".join(s for s in [sym_suffix, "zerosFixed" if "m" in args.mode else "" ] if s)   # suffix of the whole run
variant         = args.variant
suffix_dc       = "_".join(s for s in [suffix, variant ] if s)   # suffix for the datacard-level variation
doRun           = not args.dryrun
verbose         = args.verbose

with open(args.jsonInput) as file:
    print("Opening JSON file {}".format(args.jsonInput))
    jsoninput   = json.load(file)

output_dir      = jsoninput["dc-folder"][era].rstrip("/")
massPoints      = [ unpackLabel(signal,verbose)[0] for signal in jsoninput["processes"]["signals"]]



# Save a copy of the settings and the list of commands in the output folder, to be able to rerun exactly the same analysis
os.makedirs(output_dir, exist_ok=True)
settings_file   = f"{output_dir}/settings{f'_{suffix}' if suffix else ''}.json"
commands_file   = f"{output_dir}/commands{f'_{suffix}' if suffix else ''}.sh"
shutil.copy(args.jsonInput, settings_file)
with open(commands_file, "w") as f:
    f.write(f"cd {os.getcwd()}\n")

suffix_opt      = f"--suffix {suffix}" if suffix else ""
variant_opt      = f"--variant {variant}" if variant else ""
suffix_dc_opt      = f"--suffix {suffix_dc}" if variant else suffix_opt


def write_run(cmd, doRun=True):
    with open(commands_file, "a") as f:
        print(f"Writing: {cmd}")
        f.write(cmd + "\n")
    if(doRun):
        print(f"Running: {cmd}")
        subprocess.run(cmd, shell=True, check=True)

fitoptions=""#we should give as arguments to the limit functions some options - there might be the need
if ("c" in args.mode):
    write_run(f"python3 CollectHistos.py -e {era} -j {settings_file} --addSyst {f'--suffix {histo_suffix}' if histo_suffix else ''} {unblind}",doRun=False)

if ("s" in args.mode):
    write_run(f"python3 symmetrizeHistos.py -i {output_dir}/histo{era}{f'_{histo_suffix}' if histo_suffix else ''}.root -s jesTotal,jer",doRun=False)

if ("m" in args.mode):
    write_run(f"python3 makePositiveHistos.py -i {output_dir}/histo{era}{f'_{sym_suffix}' if sym_suffix else ''}.root",doRun=False)

if ("d" in args.mode):
    write_run(f"python3 CreateDatacards.py -e {era} -j {settings_file} --addSyst --addMCStat {suffix_opt} {variant_opt} {unblind}",doRun=False)

if ("l" in args.mode):
    write_run(f"python3 RunLimits.py -e {era} -j {settings_file} {suffix_dc_opt} {unblind}",doRun=False)

if ("p" in args.mode):
    write_run(f"python3 BrazilPlot.py -e {era} -j {settings_file} {suffix_dc_opt} {unblind}",doRun=False)

#unpackLabel(signal,verbose)[0] for signal in jsoninput["processes"]["signals"]]
for signal in jsoninput["processes"]["signals"]:
    mass=str(int(1000*unpackLabel(signal,verbose)[0]))
    signalpath=output_dir+"/"+signal+"_"+suffix_dc+"/"
    impactOptions = "--robustFit 1 --cminDefaultMinimizerStrategy=1 --setParameterRanges r=-100,100" # -t -1 --autoBoundsPOIs r --autoRange 1 --cminDefaultMinimizerStrategy=1
    if("i" in args.mode):
        write_run(f"python3 doImpacts.py -e {era} -m {mass} --signal {signal} --sigpath {signalpath} -j {settings_file} {suffix_opt} --FitOption '{impactOptions}'",doRun=False)
    if("g" in args.mode):
        write_run(f"python3 doGoodnessOfFit.py -e {era} -m {mass} --signal {signal} --sigpath {signalpath} -j {settings_file} -t 500 -s 123456 {suffix_opt}",doRun=False)
    if("b" in args.mode):
        write_run(f"python3 doBiasTest.py -e {era} -m {mass} --signal {signal} --sigpath {signalpath} -j {settings_file} -t 500 {suffix_opt}",doRun=False)


#The best way is to first write, then run, otherwise when it fails it does not write and one cannot run the failed command for debugging
if(doRun):
    subprocess.run("source "+commands_file, shell=True, check=True)
