import subprocess
import os
import optparse
import json

usage = "python3 doGoodnessOfFit.py"
parser = optparse.OptionParser(usage)
parser.add_option("-e", "--era",       dest="era",       type=str, default="2022",          help="Era of the datacard")
parser.add_option("-m", "--massPoint", dest="massPoint", type=int, default=700,             help="Tprime mass point")
parser.add_option("-j", "--jsonInput", dest="jsonInput",           default="settings.json", help="Settings JSON file")
parser.add_option("-t", "--toys",      dest="toys",      type=int, default=1000,            help="Number of toys")
parser.add_option("-s", "--seed",      dest="seed",      type=int, default=123456,          help="Random seed")
parser.add_option(      "--freezeSignalStrength",        dest="freezeSignalStrength",       action="store_true", default=False, help="Fix the signal strength r to zero")
parser.add_option(      "--robustMinimizer",             dest="robustMinimizer",            action="store_true", default=False, help="Enable fallback minimizers to avoid false local minima")
parser.add_option(      "--suffix",    dest="suffix",    type=str, default="",              help="Suffix of the datacard folder (e.g. TprimeToTZ_700_<suffix>)")
parser.add_option('--sigpath',        dest='sigpath',         type=str,   default = '',                                   help='Input the signal path as an argument rather than deriving it here')
parser.add_option('--signal',        dest='signal',         type=str,   default = '',                                   help='Input the signal as well')
(opt, args) = parser.parse_args()

with open(opt.jsonInput) as file:
    jsoninput = json.load(file)

era                 = opt.era
mass                = str(opt.massPoint)
toys                = str(opt.toys)
seed                = str(opt.seed)
dc_folder           = jsoninput["dc-folder"][era]
#sig_folder          = f"{dc_folder}/TprimeToTZ_{mass}{f'_{opt.suffix}' if opt.suffix else ''}"
sig_folder          = f"{dc_folder}/TprimeToTZ_{mass}{f'_{opt.suffix}' if opt.suffix else ''}" if opt.sigpath=='' else opt.sigpath 
gof_dir             = f"{sig_folder}/gof/"
data_output         = f"higgsCombine_gof_data_bonly.GoodnessOfFit.mH125.root"
toys_output         = f"higgsCombine_gof_toys_bonly.GoodnessOfFit.mH125.{seed}.root"
# data_gof_options    = "--algo saturated --setParameters r=0 --freezeParameters r"
# mc_gof_options      = "--algo saturated --setParameters r=0 --freezeParameters r --toysFrequentist"
signal_options      = "--setParameters r=0 --freezeParameters r" if opt.freezeSignalStrength else ""
minimizer_options   = "--cminFallbackAlgo Minuit2,Simplex,0:0.01 --cminFallbackAlgo Minuit2,Migrad,2:0.001" if opt.robustMinimizer else ""
data_gof_options    = f"--algo saturated --toysFrequentist --bypassFrequentistFit --rMin -250 --rMax 250 {signal_options} {minimizer_options}"
mc_gof_options      = f"--algo saturated --toysFrequentist --bypassFrequentistFit --rMin -250 --rMax 250 {signal_options} {minimizer_options}"
signal          = f"TprimeToTZ_{mass}" if opt.signal =='' else opt.signal  

signal_status = "fixed at 0" if opt.freezeSignalStrength else "floating"
minimizer_status = "with fallback minimizers" if opt.robustMinimizer else "with the default minimizer"
print(f"Running Goodness of Fit for era {era}, mass {mass}, toys {toys}, signal strength r {signal_status}, {minimizer_status}")
if not os.path.exists(gof_dir):
    os.makedirs(gof_dir)


subprocess.run(f"text2workspace.py ../{signal}.txt -m 125 -o workspace_{signal}.root",                                             shell=True, check=True, cwd=gof_dir)
subprocess.run(f"combine -M GoodnessOfFit -d workspace_{signal}.root -m 125 {data_gof_options} -n _gof_data_bonly",                         shell=True, check=True, cwd=gof_dir)
subprocess.run(f"combine -M GoodnessOfFit -d workspace_{signal}.root -m 125 {mc_gof_options} -n _gof_toys_bonly -t {toys} -s {seed}",       shell=True, check=True, cwd=gof_dir)
subprocess.run(f"combineTool.py -M CollectGoodnessOfFit --input {data_output} {toys_output} -m 125.0 -o gof.json",                                   shell=True, check=True, cwd=gof_dir)
subprocess.run(f"python3 plotGoodnessOfFit.py -i {gof_dir}/gof.json -e {era} -j {opt.jsonInput} -m {mass}",                                          shell=True, check=True, cwd=".")
