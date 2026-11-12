import ROOT
import cmsstyle as CMS
from array import array
import numpy as np
import pandas as pd
import argparse
import json
ROOT.gROOT.SetBatch()

parser = argparse.ArgumentParser(description="Collect histograms for one era")

parser.add_argument('-j', '--jsonInput',          dest='jsonInput',       type=str,       default="settings.json",    help='json file containing the settings')
parser.add_argument("-r",   "--regions",      required=True,   help="Comma-separated list of datasets (can be either entire samples or single components)")
opt = parser.parse_args()
regions = [r.strip() for r in opt.regions.split(",") if r.strip()]
with open(opt.jsonInput) as file:
    print("Opening JSON file {}".format(opt.jsonInput))
    jsoninput   = json.load(file)

def read_txt(era, region):
    suffix = f"{region}_zerosFixed"
    outputFolderPath = f"{jsoninput['dc-folder'][era].rstrip('/')}/{region}"
    df = pd.read_csv(f"{outputFolderPath}/expectedLimits_{suffix}.txt")
    return df


y_expectedFullRun2      = [2.779, 0.7454, 0.2848, 0.1388,  0.07662, 0.04614, 0.02958, 0.01957, 0.01141, 0.006877, 0.004427,0.0002494]
masses_expectedFullRun2 = [0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 1.0]
exprun2 = ROOT.TGraph(len(masses_expectedFullRun2), array('d', masses_expectedFullRun2), array('d', y_expectedFullRun2))
#th_width5               = [0.3877, 0.20453, 0.113759, 0.0659085, 0.039696, 0.02459, 0.0156, 0.0101, 0.0066, 0.0045, 0.0031, 0.00213]
#th_width1               = [0.078047, 0.041545, 0.023345, 0.013625, 0.008228, 0.005113, 0.003256, 0.002121, 0.001407, 0.0009456, 0.0006454, 0.0004463, 0.0002205, 0.0003119]
df_2024 = {}
masses = {}
expected_2024 = {}
exp2024 = {}

for region in regions:
    df_2024[region] = read_txt("2024", region).sort_values("mass")
    expected_2024[region] = df_2024[region]["expected"]
    masses[region] = df_2024[region]["mass"]
    exp2024[region] = ROOT.TGraph(len(masses[region]), array('d',masses[region]),  array('d',expected_2024[region]))


all_masses = list(masses_expectedFullRun2)
for region in regions:
    all_masses.extend(masses[region])

all_masses = sorted(set(all_masses)) #elimina duplicati


CMS.SetExtraText("Work in progress")
CMS.SetLumi(None, run="")
iPos = 0
canv_name = 'limitplot_root'
CMS.SetEnergy(13.6)
CMS.ResetAdditionalInfo()
y_str = "#sigma(pp#rightarrowTbq) #times BR(T#rightarrowtZ) [pb]"
canv = CMS.cmsCanvas(
    "comparison",             # nome del canvas
    min(all_masses) - 0.005,   # minimo asse X, in TeV
    max(all_masses) + 0.05,    # massimo asse X, in TeV
    0.0001,                   # minimo asse Y, in pb
    10,                       # massimo asse Y, in pb
    "#varphi mass [TeV]",      # titolo asse X per DM
    "#sigma(pp#rightarrow t #varphi) [pb]",  # titolo asse Y
    square=True,
    extraSpace=0.05,
    iPos=0
)
canv.SetLogy()

#obsrun2 = ROOT.TGraph(len(masses), array('d',masses),  array('d',y_observedFullRun2))
colors = ["#5790fc", "#f89c20", "#832db6", "#a5a06c", "#00a6a6", "#e763b0"]

for i, region in enumerate(regions):
    CMS.cmsDraw(
        exp2024[region], "L",
        lcolor=ROOT.TColor.GetColor(colors[i % len(colors)]),
        lstyle=2 if region.endswith("_tight_lepVeto") else 1,
        lwidth=3
    )
# Styling
CMS.cmsDraw(exprun2, "L", lcolor=ROOT.TColor.GetColor("#bd1f01"), lwidth=2)
# CMS.SetExtraText("Preliminary")




# canv.SetLogy()
leg = CMS.cmsLeg(0.20, 0.16, 0.78, 0.36, textSize=0.022)
"""
for region in regions:
    leg.AddEntry(exp2024[region], region, "L")
"""
labels = {
    "TOPXT_TNotXT_LNotT_tight_lepVeto": "XT + TNotXT + LNotT",
    "TOPXT_TNotXT_tight_lepVeto": "XT + TNotXT",
    "TOPXT_LNotT_tight_lepVeto": "XT + LNotT",
    "TOPT_LNotT_tight_lepVeto_old": "T + LNotT",
}

for region in regions:
    leg.AddEntry(exp2024[region], labels.get(region, region), "L")
leg.AddEntry(exprun2, "#sigma teorica", "L")

CMS.SaveCanvas(canv, "./ComparisonExpectedLimits.png", False)
CMS.SaveCanvas(canv, "./ComparisonExpectedLimits.pdf")
