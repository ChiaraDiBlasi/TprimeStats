import ROOT
import cmsstyle as CMS
from array import array
import numpy as np
from samples import *
import subprocess
import argparse
import json
import sys
from utils import unpackLabel
ROOT.gROOT.SetBatch()


parser = argparse.ArgumentParser(description="Collect histograms for one era")
parser.add_argument("-e", "--era",                                                        default="2022",             help="Era to process, e.g. 2022, 2022EE, 2022+2023, etc.")
parser.add_argument('-j', '--jsonInput',          dest='jsonInput',       type=str,       default="settings.json",    help='json file containing the settings')
parser.add_argument('-l', '--limitInput',          dest='limitInput',       type=str,       default="",    help='json file containing the results with the limits')
parser.add_argument('-u', '--unblind',            dest='unblind',         action='store_true',    default=False,              help='Unblind')
parser.add_argument('-s','--suffix',                   dest='suffix',          type=str,               default="",               help='suffix to add to histo.root file name (e.g. histo2022_<suffix>.root)')

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


suffix= opt.suffix if opt.suffix=="" else "_"+opt.suffix
blindlabel= "_obs_" if opt.unblind else "" 
namejson="Limits_"+era+blindlabel+suffix+".json"#take the same naming convention of the runlimits for the suffix/era/unblind if nothing specified

limitInputName = f"{outputFolderPath}/{namejson}" if opt.limitInput=="" else opt.limitInput
with open(limitInputName) as file:
    limitInput = json.load(file)

finalmodel=""
masses      = []
sigma       = []
r           = []
r_ey1_down  = []
r_ey1_up    = []
r_ey2_down  = []
r_ey2_up    = []

for l in limitInput:
    mass, model= unpackLabel(l,1)
    l_era=l+"_"+((str(era)).split("+"))[0] #Take the era if only 1 number, the first if more than one
    masses.append((mass))
    sigma.append(sample_dict[l_era].sigma) 
    if(finalmodel!="" and finalmodel != model):
        print (f"WARNING! model for sample{l} is different from the previous one! Might be a mistake in the settings! Exiting. " )
        sys.exit(1)
    finalmodel=model
    values=limitInput[l]
    r_ey2_down.append(values[0])
    r_ey1_down.append(values[1])
    r.append(values[2])
    r_ey1_up.append(values[3])
    r_ey2_up.append(values[4])
print("r vectors: ", r, "\n",r_ey1_down, "\n",r_ey1_up,"\n", r_ey2_down, "\n",r_ey2_up)
    
# masses      = [0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]
ex          = [0]*len(masses)

print("sigmas are ",sigma)

y_central   = [s*r_ for s,r_ in zip(sigma, r)]
y1_up       = [s*r_ for s,r_ in zip(sigma, r_ey1_up)]
y1_down     = [s*r_ for s,r_ in zip(sigma, r_ey1_down)]
y2_up       = [s*r_ for s,r_ in zip(sigma, r_ey2_up)]
y2_down     = [s*r_ for s,r_ in zip(sigma, r_ey2_down)]
print(y_central, y1_up, y1_down, y2_up, y2_down)

y1_down     = np.array(y_central)-np.array(y1_down)
y1_up       = np.array(y1_up)-np.array(y_central)
y2_down     = np.array(y_central)-np.array(y2_down)
y2_up       = np.array(y2_up)-np.array(y_central)
print(y_central, y1_up, y1_down, y2_up, y2_down)

x           = masses

g     = ROOT.TGraphErrors(len(x), array('d',x),  array('d',y_central))
ge    = ROOT.TGraphAsymmErrors(len(x), array('d',x),  array('d',y_central), array('d',ex), array('d',ex), array('d',y1_down), array('d',y1_up))
ge2   = ROOT.TGraphAsymmErrors(len(x), array('d',x),  array('d',y_central), array('d',ex), array('d',ex), array('d',y2_down), array('d',y2_up))
th    = ROOT.TGraph(len(x), array('d',x),  array('d',sigma))
thw5  = ROOT.TGraph(len(x), array('d',x),  array('d',[0.3877, 0.20453, 0.113759, 0.0659085, 0.039696, 0.02459, 0.0156, 0.0101, 0.0066, 0.0045, 0.0031, 0.00213]))

#masses_observedFullRun2 = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]
#y_observedFullRun2      = [0.21201, 0.09651, 0.07699, 0.07321, 0.06227, 0.04283, 0.04972, 0.04938, 0.03669, 0.02263, 0.0183, 0.01505]
#y_expectedFullRun2      = [0.36702, 0.1707, 0.10685, 0.07576, 0.05272, 0.03193, 0.02376, 0.01967, 0.01859, 0.01639, 0.01372, 0.01271]
#obsrun2                 = ROOT.TGraph(len(masses_observedFullRun2), array('d',masses_observedFullRun2),  array('d',y_observedFullRun2))
#exprun2                 = ROOT.TGraph(len(masses_observedFullRun2), array('d',masses_observedFullRun2),  array('d',y_expectedFullRun2))

if("TBDM" in finalmodel):
    masses_observedFullRun2 = [0.01,  0.05,   0.1,    0.15,    0.2,     0.25,    0.3,     0.35,    0.4,     0.45,     0.5,     1.0 ]
    y_expectedFullRun2      = [2.779, 0.7454, 0.2848, 0.1388,  0.07662, 0.04614, 0.02958, 0.01957, 0.01141, 0.006877, 0.004427,0.0002494]
    exprun2                 = ROOT.TGraph(len(masses_observedFullRun2), array('d',masses_observedFullRun2),  array('d',y_expectedFullRun2))
    
    #print(finalmodel)
if("TprimeToTZNW" in finalmodel):
    masses_observedFullRun2 = [0.7,     0.8,     0.9,     1.0,      1.1,     1.2,     1.3,     1.4,     1.5,     1.6,      1.7,      1.8]
    xrun2=masses_observedFullRun2
    y_expectedFullRun2      = [0.36602, 0.17070, 0.10685, 0.07576,  0.05272, 0.03193, 0.02376, 0.01967, 0.01859, 0.016390, 0.013720, 0.012710 ]
    y_observedFullRun2      = [0.21201, 0.09651, 0.07699, 0.07321,  0.06227, 0.04283, 0.04972, 0.04938, 0.03669, 0.022630, 0.018300, 0.015040 ]
    exprun2 = ROOT.TGraph(len(xrun2), array('d',xrun2), array('d',y_expectedFullRun2) )
    obsrun2 = ROOT.TGraph(len(xrun2), array('d',xrun2), array('d',y_observedFullRun2) )
    #    thrun2                 = th

# Styling
# CMS.SetExtraText("Preliminary")
CMS.SetExtraText("Work in progress")
iPos = 11
canv_name = 'limitplot_root'
CMS.SetLumi(lumi, run="Run 3", round_lumi=3)
CMS.SetEnergy(13.6)
CMS.ResetAdditionalInfo()
#y_str = "#sigma(pp#rightarrowTbq) #times BR(T#rightarrowtZ) [pb]"
signal_y_min = max(0, min(np.array(y_central) - np.array(y2_down)) * 0.9)
signal_y_max = max(np.array(y_central) + np.array(y2_up)) * 10 # log scale: leave room for the CMS label and the legend
if("TBDM" in finalmodel):
    y_str = "#sigma (pp#rightarrow t #varphi) [pb]"
    canv = CMS.cmsCanvas(canv_name, min(x)-0.05,max(x)+0.05,signal_y_min,signal_y_max,"#varphi mass [TeV]",y_str,square=True,extraSpace=0.05,iPos=iPos)
if("Tprime" in finalmodel):
    y_str = "#sigma(pp#rightarrowTbq) #times BR(T#rightarrowtZ) [pb]"
    canv = CMS.cmsCanvas(canv_name, min(x)-0.05,max(x)+0.05,signal_y_min,signal_y_max,"T' mass [TeV]",y_str,square=True,extraSpace=0.05,iPos=iPos)

CMS.cmsDraw(ge2, "3L", fcolor = ROOT.TColor.GetColor("#F5BB54"))
CMS.cmsDraw(ge, "3", fcolor = ROOT.TColor.GetColor("#607641"))
CMS.cmsDraw(g, "L", lstyle=ROOT.kDashed)
CMS.cmsDraw(th, "L", lcolor = ROOT.TColor.GetColor("#bd1f01"), lwidth=2)
CMS.cmsDraw(exprun2, "L", lcolor = ROOT.TColor.GetColor("#964a8b"), lwidth=2)
#CMS.cmsDraw(obsrun2, "L", lcolor = ROOT.TColor.GetColor("#964a8b"), lwidth=2)
#MS.cmsDraw(exprun2, "L", lcolor = ROOT.TColor.GetColor("#964a8b"), lwidth=2, lstyle=ROOT.kDashed)

canv.SetLogy()
leg = CMS.cmsLeg(0.50, 0.60, 0.94, 0.90, textSize=0.026)
leg.AddEntry(g, "expected","L")
leg.AddEntry(ge, "68% expected","F")
leg.AddEntry(ge2, "95% expected","F")
leg.AddEntry(th, "#sigma(NLO), Singlet T, #Gamma/m_{T}<0.01","L")
#leg.AddEntry(obsrun2, "observed Full Run 2","L")
leg.AddEntry(exprun2, "expected Full Run 2","L")
CMS.CMS_lumi(canv, iPos)
CMS.SaveCanvas(canv, f"{outputFolderPath}/limitPlot_{finalmodel}_{era}{suffix}.png", False)
CMS.SaveCanvas(canv, f"{outputFolderPath}/limitPlot_{finalmodel}_{era}{suffix}.pdf")
# Save expected limits

with open(f"{outputFolderPath}/expectedLimits.txt", "w") as f:
    f.write("mass,expected,expected_16,expected_84,expected_2_5,expected_97_5\n")
    for i in range(len(masses)):
        f.write(str(masses[i])+","+str(y_central[i])+","+str(y1_down[i])+","+str(y1_up[i])+","+str(y2_down[i])+","+str(y2_up[i])+"\n")


# signal strenght
y_central   = [r_ for r_ in r]
y1_up       = [r_ for r_ in r_ey1_up]
y1_down     = [r_ for r_ in r_ey1_down]
y2_up       = [r_ for r_ in r_ey2_up]
y2_down     = [r_ for r_ in r_ey2_down]
print(y_central, y1_up, y1_down, y2_up, y2_down)

y1_down     = np.array(y_central)-np.array(y1_down)
y1_up       = np.array(y1_up)-np.array(y_central)
y2_down     = np.array(y_central)-np.array(y2_down)
y2_up       = np.array(y2_up)-np.array(y_central)
print(y_central, y1_up, y1_down, y2_up, y2_down)

x           = masses

g     = ROOT.TGraphErrors(len(x), array('d',x),  array('d',y_central))
ge    = ROOT.TGraphAsymmErrors(len(x), array('d',x),  array('d',y_central), array('d',ex), array('d',ex), array('d',y1_down), array('d',y1_up))
ge2   = ROOT.TGraphAsymmErrors(len(x), array('d',x),  array('d',y_central), array('d',ex), array('d',ex), array('d',y2_down), array('d',y2_up))
th    = ROOT.TGraph(len(x), array('d',x),  array('d',sigma))
thw5  = ROOT.TGraph(len(x), array('d',x),  array('d',[0.3877, 0.20453, 0.113759, 0.0659085, 0.039696, 0.02459, 0.0156, 0.0101, 0.0066, 0.0045, 0.0031, 0.00213]))

#masses_observedFullRun2 = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]
#y_observedFullRun2      = [0.21201, 0.09651, 0.07699, 0.07321, 0.06227, 0.04283, 0.04972, 0.04938, 0.03669, 0.02263, 0.0183, 0.01505]
#y_expectedFullRun2      = [0.36702, 0.1707, 0.10685, 0.07576, 0.05272, 0.03193, 0.02376, 0.01967, 0.01859, 0.01639, 0.01372, 0.01271]
#obsrun2                 = ROOT.TGraph(len(masses_observedFullRun2), array('d',masses_observedFullRun2),  array('d',y_observedFullRun2))

# Styling
# CMS.SetExtraText("Preliminary")
CMS.SetExtraText("Work in progress")
iPos = 11
canv_name = 'signalstrength_root'
CMS.SetLumi(lumi, run="Run 3", round_lumi=3)
CMS.SetEnergy(13.6)
CMS.ResetAdditionalInfo()
y_str = "Signal strength"
signal_y_min = max(0, min(np.array(y_central) - np.array(y2_down)) * 0.9)
signal_y_max = max(np.array(y_central) + np.array(y2_up)) * 1.1
canv = CMS.cmsCanvas(canv_name, min(x)-0.05,max(x)+0.05,signal_y_min,signal_y_max,"T' mass [TeV]",y_str,square=True,extraSpace=0.05,iPos=iPos)
CMS.cmsDraw(ge2, "3L", fcolor = ROOT.TColor.GetColor("#F5BB54"))
CMS.cmsDraw(ge, "3", fcolor = ROOT.TColor.GetColor("#607641"))
CMS.cmsDraw(g, "L", lstyle=ROOT.kDashed)
CMS.cmsDraw(th, "L", lcolor = ROOT.TColor.GetColor("#bd1f01"), lwidth=2)
CMS.CMS_lumi(canv, iPos)
CMS.SaveCanvas(canv, f"{outputFolderPath}/signalstrength_{finalmodel}_{era}{suffix}.png", False)
CMS.SaveCanvas(canv, f"{outputFolderPath}/signalstrength_{finalmodel}_{era}{suffix}.pdf")

