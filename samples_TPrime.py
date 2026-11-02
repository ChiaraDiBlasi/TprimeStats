import ROOT
import os
#import json_reader as jr

path = os.path.dirname(os.path.abspath(__file__))

class sample:
    def __init__(self, color, style, fill, leglabel, label):
        self.color = color
        self.style = style
        self.fill = fill
        self.leglabel = leglabel
        self.label = label

# unix_code = <era><2: MC signal><0: Tprime><2-digit mass index (700 -> 00, ..., 3000 -> 18)>
# era digit: 3 = 2022, 4 = 2022EE, 5 = 2023, 6 = 2023postBPix, 7 = 2024
# Aggregates TprimeToTZ_<era> have no unix_code (as for the other samples with components)
# 2018 samples are kept as in the original samples.py (legacy codes 22000-22002, no process, no aggregate)

sigma_TprimeToTZ_13TeV  = {                               # fb * 1e-3 = pb (all sample.sigma are in pb)
                            "700": 88.107 / 1.1289 * 1e-3,
                            "800": 45.920 / 1.1053 * 1e-3,
                            "900": 25.327 / 1.0849 * 1e-3,
                            "1000": 14.550 / 1.0679 * 1e-3,
                            "1100": 8.640 / 1.0501 * 1e-3,
                            "1200": 5.342 / 1.0448 * 1e-3,
                            "1300": 3.390 / 1.0412 * 1e-3,
                            "1400": 2.197 / 1.0358 * 1e-3,
                            "1500": 1.448 / 1.0291 * 1e-3,
                            "1600": 0.9743 / 1.0304 * 1e-3,
                            "1700": 0.6638 / 1.0285 * 1e-3,
                            "1800": 0.4588 / 1.0280 * 1e-3,
                            "1900": 0.3201 / 1.0263 * 1e-3,
                            "2000": 0.2256 / 1.0231 * 1e-3,
                            "2200": 0.119 / 1.0200 * 1e-3,
                            "2400": 0.0671 / 1.0168 * 1e-3,
                            "2600": 0.0401 / 1.0137 * 1e-3,
                            "2800": 0.0 * 1e-3,
                            "3000": 0.0 * 1e-3,
                        }

sigma_TprimeToTZ_13p6TeV  = {
                            "700": sigma_TprimeToTZ_13TeV["700"],
                            "800": sigma_TprimeToTZ_13TeV["800"],
                            "900": sigma_TprimeToTZ_13TeV["900"],
                            "1000": sigma_TprimeToTZ_13TeV["1000"],
                            "1100": sigma_TprimeToTZ_13TeV["1100"],
                            "1200": sigma_TprimeToTZ_13TeV["1200"],
                            "1300": sigma_TprimeToTZ_13TeV["1300"],
                            "1400": sigma_TprimeToTZ_13TeV["1400"],
                            "1500": sigma_TprimeToTZ_13TeV["1500"],
                            "1600": sigma_TprimeToTZ_13TeV["1600"],
                            "1700": sigma_TprimeToTZ_13TeV["1700"],
                            "1800": sigma_TprimeToTZ_13TeV["1800"],
                            "1900": sigma_TprimeToTZ_13TeV["1900"],
                            "2000": sigma_TprimeToTZ_13TeV["2000"],
                            "2200": sigma_TprimeToTZ_13TeV["2200"],
                            "2400": sigma_TprimeToTZ_13TeV["2400"],
                            "2600": sigma_TprimeToTZ_13TeV["2600"],
                            "2800": sigma_TprimeToTZ_13TeV["2800"],
                            "3000": sigma_TprimeToTZ_13TeV["3000"],
                        }

################################ VLQ T signals 2018 ################################
TprimeToTZ_1800_2018         = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1800GeV", "TprimeToTZ_1800_2018")
TprimeToTZ_1800_2018.sigma   = 0.00045 #pb
TprimeToTZ_1800_2018.year    = 2018
TprimeToTZ_1800_2018.dataset = '/TprimeBToTZ_M-1800_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM'
TprimeToTZ_1800_2018.unix_code = 22000
# TprimeToTZ_1800_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/"+TprimeToTZ_1800_2018.label +"_Skim.root"

TprimeToTZ_1000_2018         = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow TZ M1000GeV", "TprimeToTZ_1000_2018")
TprimeToTZ_1000_2018.sigma   = 0.01362 #pb
TprimeToTZ_1000_2018.year    = 2018
TprimeToTZ_1000_2018.dataset = '/TprimeBToTZ_M-1000_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM'
TprimeToTZ_1000_2018.unix_code = 22001
# TprimeToTZ_1000_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/"+TprimeToTZ_1000_2018.label +"_Skim.root"

TprimeToTZ_700_2018         = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M700GeV", "TprimeToTZ_700_2018")
TprimeToTZ_700_2018.sigma   = 0.07804 #pb
TprimeToTZ_700_2018.year    = 2018
TprimeToTZ_700_2018.dataset = '/TprimeBToTZ_M-700_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM'
TprimeToTZ_700_2018.unix_code = 22002
# TprimeToTZ_700_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/"+TprimeToTZ_700_2018.label +"_Skim.root"

################################ VLQ T signals 2022 ################################
TprimeToTZ_700_2022           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M700GeV", "TprimeToTZ_700_2022")
TprimeToTZ_700_2022.sigma     = sigma_TprimeToTZ_13p6TeV["700"]
TprimeToTZ_700_2022.year      = 2022
TprimeToTZ_700_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-700_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_700_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_700_2022.unix_code = 32000
TprimeToTZ_700_2022.EE        = 0

TprimeToTZ_800_2022           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M800GeV", "TprimeToTZ_800_2022")
TprimeToTZ_800_2022.sigma     = sigma_TprimeToTZ_13p6TeV["800"]
TprimeToTZ_800_2022.year      = 2022
TprimeToTZ_800_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_800_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_800_2022.unix_code = 32001
TprimeToTZ_800_2022.EE        = 0

TprimeToTZ_900_2022           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M900GeV", "TprimeToTZ_900_2022")
TprimeToTZ_900_2022.sigma     = sigma_TprimeToTZ_13p6TeV["900"]
TprimeToTZ_900_2022.year      = 2022
TprimeToTZ_900_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-900_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_900_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_900_2022.unix_code = 32002
TprimeToTZ_900_2022.EE        = 0

TprimeToTZ_1000_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1000GeV", "TprimeToTZ_1000_2022")
TprimeToTZ_1000_2022.sigma     = sigma_TprimeToTZ_13p6TeV["1000"]
TprimeToTZ_1000_2022.year      = 2022
TprimeToTZ_1000_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-1000_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_1000_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_1000_2022.unix_code = 32003
TprimeToTZ_1000_2022.EE        = 0

TprimeToTZ_1100_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1100GeV", "TprimeToTZ_1100_2022")
TprimeToTZ_1100_2022.sigma     = sigma_TprimeToTZ_13p6TeV["1100"]
TprimeToTZ_1100_2022.year      = 2022
TprimeToTZ_1100_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-1100_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_1100_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_1100_2022.unix_code = 32004
TprimeToTZ_1100_2022.EE        = 0

TprimeToTZ_1200_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1200GeV", "TprimeToTZ_1200_2022")
TprimeToTZ_1200_2022.sigma     = sigma_TprimeToTZ_13p6TeV["1200"]
TprimeToTZ_1200_2022.year      = 2022
TprimeToTZ_1200_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-1200_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_1200_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_1200_2022.unix_code = 32005
TprimeToTZ_1200_2022.EE        = 0

TprimeToTZ_1300_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1300GeV", "TprimeToTZ_1300_2022")
TprimeToTZ_1300_2022.sigma     = sigma_TprimeToTZ_13p6TeV["1300"]
TprimeToTZ_1300_2022.year      = 2022
TprimeToTZ_1300_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-1300_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_1300_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_1300_2022.unix_code = 32006
TprimeToTZ_1300_2022.EE        = 0

TprimeToTZ_1400_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1400GeV", "TprimeToTZ_1400_2022")
TprimeToTZ_1400_2022.sigma     = sigma_TprimeToTZ_13p6TeV["1400"]
TprimeToTZ_1400_2022.year      = 2022
TprimeToTZ_1400_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-1400_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_1400_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_1400_2022.unix_code = 32007
TprimeToTZ_1400_2022.EE        = 0

TprimeToTZ_1500_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1500GeV", "TprimeToTZ_1500_2022")
TprimeToTZ_1500_2022.sigma     = sigma_TprimeToTZ_13p6TeV["1500"]
TprimeToTZ_1500_2022.year      = 2022
TprimeToTZ_1500_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-1500_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_1500_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_1500_2022.unix_code = 32008
TprimeToTZ_1500_2022.EE        = 0

TprimeToTZ_1600_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1600GeV", "TprimeToTZ_1600_2022")
TprimeToTZ_1600_2022.sigma     = sigma_TprimeToTZ_13p6TeV["1600"]
TprimeToTZ_1600_2022.year      = 2022
TprimeToTZ_1600_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-1600_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_1600_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_1600_2022.unix_code = 32009
TprimeToTZ_1600_2022.EE        = 0

TprimeToTZ_1700_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1700GeV", "TprimeToTZ_1700_2022")
TprimeToTZ_1700_2022.sigma     = sigma_TprimeToTZ_13p6TeV["1700"]
TprimeToTZ_1700_2022.year      = 2022
TprimeToTZ_1700_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-1700_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_1700_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_1700_2022.unix_code = 32010
TprimeToTZ_1700_2022.EE        = 0

TprimeToTZ_1800_2022           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1800GeV", "TprimeToTZ_1800_2022")
TprimeToTZ_1800_2022.sigma     = sigma_TprimeToTZ_13p6TeV["1800"]
TprimeToTZ_1800_2022.year      = 2022
TprimeToTZ_1800_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-1800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_1800_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_1800_2022.unix_code = 32011
TprimeToTZ_1800_2022.EE        = 0

TprimeToTZ_1900_2022           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1900GeV", "TprimeToTZ_1900_2022")
TprimeToTZ_1900_2022.sigma     = sigma_TprimeToTZ_13p6TeV["1900"]
TprimeToTZ_1900_2022.year      = 2022
TprimeToTZ_1900_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-1900_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_1900_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_1900_2022.unix_code = 32012
TprimeToTZ_1900_2022.EE        = 0

TprimeToTZ_2000_2022           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2000GeV", "TprimeToTZ_2000_2022")
TprimeToTZ_2000_2022.sigma     = sigma_TprimeToTZ_13p6TeV["2000"]
TprimeToTZ_2000_2022.year      = 2022
TprimeToTZ_2000_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-2000_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_2000_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_2000_2022.unix_code = 32013
TprimeToTZ_2000_2022.EE        = 0

TprimeToTZ_2200_2022           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2200GeV", "TprimeToTZ_2200_2022")
TprimeToTZ_2200_2022.sigma     = sigma_TprimeToTZ_13p6TeV["2200"]
TprimeToTZ_2200_2022.year      = 2022
TprimeToTZ_2200_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-2200_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_2200_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_2200_2022.unix_code = 32014
TprimeToTZ_2200_2022.EE        = 0

TprimeToTZ_2400_2022           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2400GeV", "TprimeToTZ_2400_2022")
TprimeToTZ_2400_2022.sigma     = sigma_TprimeToTZ_13p6TeV["2400"]
TprimeToTZ_2400_2022.year      = 2022
TprimeToTZ_2400_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-2400_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_2400_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_2400_2022.unix_code = 32015
TprimeToTZ_2400_2022.EE        = 0

TprimeToTZ_2600_2022           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2600GeV", "TprimeToTZ_2600_2022")
TprimeToTZ_2600_2022.sigma     = sigma_TprimeToTZ_13p6TeV["2600"]
TprimeToTZ_2600_2022.year      = 2022
TprimeToTZ_2600_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-2600_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_2600_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_2600_2022.unix_code = 32016
TprimeToTZ_2600_2022.EE        = 0

TprimeToTZ_2800_2022           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2800GeV", "TprimeToTZ_2800_2022")
TprimeToTZ_2800_2022.sigma     = sigma_TprimeToTZ_13p6TeV["2800"]
TprimeToTZ_2800_2022.year      = 2022
TprimeToTZ_2800_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-2800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_2800_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_2800_2022.unix_code = 32017
TprimeToTZ_2800_2022.EE        = 0

TprimeToTZ_3000_2022           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M3000GeV", "TprimeToTZ_3000_2022")
TprimeToTZ_3000_2022.sigma     = sigma_TprimeToTZ_13p6TeV["3000"]
TprimeToTZ_3000_2022.year      = 2022
TprimeToTZ_3000_2022.dataset   = '/TprimeBtoTZ-LH_Par-M-3000_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM'
TprimeToTZ_3000_2022.process   = "TprimeToTZ_2022"
TprimeToTZ_3000_2022.unix_code = 32018
TprimeToTZ_3000_2022.EE        = 0

TprimeToTZ_2022            = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ", "TprimeToTZ_2022")
TprimeToTZ_2022.year       = 2022
TprimeToTZ_2022.components = [
    TprimeToTZ_700_2022,
    TprimeToTZ_800_2022,
    TprimeToTZ_900_2022,
    TprimeToTZ_1000_2022,
    TprimeToTZ_1100_2022,
    TprimeToTZ_1200_2022,
    TprimeToTZ_1300_2022,
    TprimeToTZ_1400_2022,
    TprimeToTZ_1500_2022,
    TprimeToTZ_1600_2022,
    TprimeToTZ_1700_2022,
    TprimeToTZ_1800_2022,
    TprimeToTZ_1900_2022,
    TprimeToTZ_2000_2022,
    TprimeToTZ_2200_2022,
    TprimeToTZ_2400_2022,
    TprimeToTZ_2600_2022,
    TprimeToTZ_2800_2022,
    TprimeToTZ_3000_2022,
]

################################ VLQ T signals 2022EE ################################
TprimeToTZ_700_2022EE            = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M700GeV", "TprimeToTZ_700_2022EE")
TprimeToTZ_700_2022EE.sigma      = sigma_TprimeToTZ_13p6TeV["700"]
TprimeToTZ_700_2022EE.year       = 2022
TprimeToTZ_700_2022EE.dataset    = '/TprimeBtoTZ-LH_Par-M-700_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_700_2022EE.process    = "TprimeToTZ_2022EE"
TprimeToTZ_700_2022EE.unix_code  = 42000
TprimeToTZ_700_2022EE.EE         = 1

TprimeToTZ_800_2022EE            = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M800GeV", "TprimeToTZ_800_2022EE")
TprimeToTZ_800_2022EE.sigma      = sigma_TprimeToTZ_13p6TeV["800"]
TprimeToTZ_800_2022EE.year       = 2022
TprimeToTZ_800_2022EE.dataset    = '/TprimeBtoTZ-LH_Par-M-800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_800_2022EE.process    = "TprimeToTZ_2022EE"
TprimeToTZ_800_2022EE.unix_code  = 42001
TprimeToTZ_800_2022EE.EE         = 1

TprimeToTZ_900_2022EE            = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M900GeV", "TprimeToTZ_900_2022EE")
TprimeToTZ_900_2022EE.sigma      = sigma_TprimeToTZ_13p6TeV["900"]
TprimeToTZ_900_2022EE.year       = 2022
TprimeToTZ_900_2022EE.dataset    = '/TprimeBtoTZ-LH_Par-M-900_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_900_2022EE.process    = "TprimeToTZ_2022EE"
TprimeToTZ_900_2022EE.unix_code  = 42002
TprimeToTZ_900_2022EE.EE         = 1

TprimeToTZ_1000_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1000GeV", "TprimeToTZ_1000_2022EE")
TprimeToTZ_1000_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["1000"]
TprimeToTZ_1000_2022EE.year      = 2022
TprimeToTZ_1000_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-1000_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_1000_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_1000_2022EE.unix_code = 42003
TprimeToTZ_1000_2022EE.EE        = 1

TprimeToTZ_1100_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1100GeV", "TprimeToTZ_1100_2022EE")
TprimeToTZ_1100_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["1100"]
TprimeToTZ_1100_2022EE.year      = 2022
TprimeToTZ_1100_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-1100_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_1100_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_1100_2022EE.unix_code = 42004
TprimeToTZ_1100_2022EE.EE        = 1

TprimeToTZ_1200_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1200GeV", "TprimeToTZ_1200_2022EE")
TprimeToTZ_1200_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["1200"]
TprimeToTZ_1200_2022EE.year      = 2022
TprimeToTZ_1200_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-1200_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_1200_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_1200_2022EE.unix_code = 42005
TprimeToTZ_1200_2022EE.EE        = 1

TprimeToTZ_1300_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1300GeV", "TprimeToTZ_1300_2022EE")
TprimeToTZ_1300_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["1300"]
TprimeToTZ_1300_2022EE.year      = 2022
TprimeToTZ_1300_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-1300_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_1300_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_1300_2022EE.unix_code = 42006
TprimeToTZ_1300_2022EE.EE        = 1

TprimeToTZ_1400_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1400GeV", "TprimeToTZ_1400_2022EE")
TprimeToTZ_1400_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["1400"]
TprimeToTZ_1400_2022EE.year      = 2022
TprimeToTZ_1400_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-1400_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_1400_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_1400_2022EE.unix_code = 42007
TprimeToTZ_1400_2022EE.EE        = 1

TprimeToTZ_1500_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1500GeV", "TprimeToTZ_1500_2022EE")
TprimeToTZ_1500_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["1500"]
TprimeToTZ_1500_2022EE.year      = 2022
TprimeToTZ_1500_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-1500_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_1500_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_1500_2022EE.unix_code = 42008
TprimeToTZ_1500_2022EE.EE        = 1

TprimeToTZ_1600_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1600GeV", "TprimeToTZ_1600_2022EE")
TprimeToTZ_1600_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["1600"]
TprimeToTZ_1600_2022EE.year      = 2022
TprimeToTZ_1600_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-1600_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_1600_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_1600_2022EE.unix_code = 42009
TprimeToTZ_1600_2022EE.EE        = 1

TprimeToTZ_1700_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1700GeV", "TprimeToTZ_1700_2022EE")
TprimeToTZ_1700_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["1700"]
TprimeToTZ_1700_2022EE.year      = 2022
TprimeToTZ_1700_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-1700_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_1700_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_1700_2022EE.unix_code = 42010
TprimeToTZ_1700_2022EE.EE        = 1

TprimeToTZ_1800_2022EE           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1800GeV", "TprimeToTZ_1800_2022EE")
TprimeToTZ_1800_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["1800"]
TprimeToTZ_1800_2022EE.year      = 2022
TprimeToTZ_1800_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-1800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_1800_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_1800_2022EE.unix_code = 42011
TprimeToTZ_1800_2022EE.EE        = 1

TprimeToTZ_1900_2022EE           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1900GeV", "TprimeToTZ_1900_2022EE")
TprimeToTZ_1900_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["1900"]
TprimeToTZ_1900_2022EE.year      = 2022
TprimeToTZ_1900_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-1900_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_1900_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_1900_2022EE.unix_code = 42012
TprimeToTZ_1900_2022EE.EE        = 1

TprimeToTZ_2000_2022EE           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2000GeV", "TprimeToTZ_2000_2022EE")
TprimeToTZ_2000_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["2000"]
TprimeToTZ_2000_2022EE.year      = 2022
TprimeToTZ_2000_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-2000_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_2000_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_2000_2022EE.unix_code = 42013
TprimeToTZ_2000_2022EE.EE        = 1

TprimeToTZ_2200_2022EE           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2200GeV", "TprimeToTZ_2200_2022EE")
TprimeToTZ_2200_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["2200"]
TprimeToTZ_2200_2022EE.year      = 2022
TprimeToTZ_2200_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-2200_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_2200_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_2200_2022EE.unix_code = 42014
TprimeToTZ_2200_2022EE.EE        = 1

TprimeToTZ_2400_2022EE           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2400GeV", "TprimeToTZ_2400_2022EE")
TprimeToTZ_2400_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["2400"]
TprimeToTZ_2400_2022EE.year      = 2022
TprimeToTZ_2400_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-2400_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_2400_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_2400_2022EE.unix_code = 42015
TprimeToTZ_2400_2022EE.EE        = 1

TprimeToTZ_2600_2022EE           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2600GeV", "TprimeToTZ_2600_2022EE")
TprimeToTZ_2600_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["2600"]
TprimeToTZ_2600_2022EE.year      = 2022
TprimeToTZ_2600_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-2600_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_2600_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_2600_2022EE.unix_code = 42016
TprimeToTZ_2600_2022EE.EE        = 1

TprimeToTZ_2800_2022EE           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2800GeV", "TprimeToTZ_2800_2022EE")
TprimeToTZ_2800_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["2800"]
TprimeToTZ_2800_2022EE.year      = 2022
TprimeToTZ_2800_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-2800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_2800_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_2800_2022EE.unix_code = 42017
TprimeToTZ_2800_2022EE.EE        = 1

TprimeToTZ_3000_2022EE           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M3000GeV", "TprimeToTZ_3000_2022EE")
TprimeToTZ_3000_2022EE.sigma     = sigma_TprimeToTZ_13p6TeV["3000"]
TprimeToTZ_3000_2022EE.year      = 2022
TprimeToTZ_3000_2022EE.dataset   = '/TprimeBtoTZ-LH_Par-M-3000_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM'
TprimeToTZ_3000_2022EE.process   = "TprimeToTZ_2022EE"
TprimeToTZ_3000_2022EE.unix_code = 42018
TprimeToTZ_3000_2022EE.EE        = 1

TprimeToTZ_2022EE            = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ", "TprimeToTZ_2022EE")
TprimeToTZ_2022EE.year       = 2022
TprimeToTZ_2022EE.components = [
    TprimeToTZ_700_2022EE,
    TprimeToTZ_800_2022EE,
    TprimeToTZ_900_2022EE,
    TprimeToTZ_1000_2022EE,
    TprimeToTZ_1100_2022EE,
    TprimeToTZ_1200_2022EE,
    TprimeToTZ_1300_2022EE,
    TprimeToTZ_1400_2022EE,
    TprimeToTZ_1500_2022EE,
    TprimeToTZ_1600_2022EE,
    TprimeToTZ_1700_2022EE,
    TprimeToTZ_1800_2022EE,
    TprimeToTZ_1900_2022EE,
    TprimeToTZ_2000_2022EE,
    TprimeToTZ_2200_2022EE,
    TprimeToTZ_2400_2022EE,
    TprimeToTZ_2600_2022EE,
    TprimeToTZ_2800_2022EE,
    TprimeToTZ_3000_2022EE,
]

################################ VLQ T signals 2023 ################################
TprimeToTZ_700_2023           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M700GeV", "TprimeToTZ_700_2023")
TprimeToTZ_700_2023.sigma     = sigma_TprimeToTZ_13p6TeV["700"]
TprimeToTZ_700_2023.year      = 2023
TprimeToTZ_700_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-700_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_700_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_700_2023.unix_code = 52000
TprimeToTZ_700_2023.EE        = 0

TprimeToTZ_800_2023           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M800GeV", "TprimeToTZ_800_2023")
TprimeToTZ_800_2023.sigma     = sigma_TprimeToTZ_13p6TeV["800"]
TprimeToTZ_800_2023.year      = 2023
TprimeToTZ_800_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_800_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_800_2023.unix_code = 52001
TprimeToTZ_800_2023.EE        = 0

TprimeToTZ_900_2023           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M900GeV", "TprimeToTZ_900_2023")
TprimeToTZ_900_2023.sigma     = sigma_TprimeToTZ_13p6TeV["900"]
TprimeToTZ_900_2023.year      = 2023
TprimeToTZ_900_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-900_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_900_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_900_2023.unix_code = 52002
TprimeToTZ_900_2023.EE        = 0

TprimeToTZ_1000_2023           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1000GeV", "TprimeToTZ_1000_2023")
TprimeToTZ_1000_2023.sigma     = sigma_TprimeToTZ_13p6TeV["1000"]
TprimeToTZ_1000_2023.year      = 2023
TprimeToTZ_1000_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-1000_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_1000_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_1000_2023.unix_code = 52003
TprimeToTZ_1000_2023.EE        = 0

TprimeToTZ_1100_2023           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1100GeV", "TprimeToTZ_1100_2023")
TprimeToTZ_1100_2023.sigma     = sigma_TprimeToTZ_13p6TeV["1100"]
TprimeToTZ_1100_2023.year      = 2023
TprimeToTZ_1100_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-1100_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_1100_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_1100_2023.unix_code = 52004
TprimeToTZ_1100_2023.EE        = 0

TprimeToTZ_1200_2023           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1200GeV", "TprimeToTZ_1200_2023")
TprimeToTZ_1200_2023.sigma     = sigma_TprimeToTZ_13p6TeV["1200"]
TprimeToTZ_1200_2023.year      = 2023
TprimeToTZ_1200_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-1200_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_1200_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_1200_2023.unix_code = 52005
TprimeToTZ_1200_2023.EE        = 0

TprimeToTZ_1300_2023           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1300GeV", "TprimeToTZ_1300_2023")
TprimeToTZ_1300_2023.sigma     = sigma_TprimeToTZ_13p6TeV["1300"]
TprimeToTZ_1300_2023.year      = 2023
TprimeToTZ_1300_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-1300_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_1300_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_1300_2023.unix_code = 52006
TprimeToTZ_1300_2023.EE        = 0

TprimeToTZ_1400_2023           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1400GeV", "TprimeToTZ_1400_2023")
TprimeToTZ_1400_2023.sigma     = sigma_TprimeToTZ_13p6TeV["1400"]
TprimeToTZ_1400_2023.year      = 2023
TprimeToTZ_1400_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-1400_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_1400_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_1400_2023.unix_code = 52007
TprimeToTZ_1400_2023.EE        = 0

TprimeToTZ_1500_2023           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1500GeV", "TprimeToTZ_1500_2023")
TprimeToTZ_1500_2023.sigma     = sigma_TprimeToTZ_13p6TeV["1500"]
TprimeToTZ_1500_2023.year      = 2023
TprimeToTZ_1500_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-1500_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_1500_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_1500_2023.unix_code = 52008
TprimeToTZ_1500_2023.EE        = 0

TprimeToTZ_1600_2023           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1600GeV", "TprimeToTZ_1600_2023")
TprimeToTZ_1600_2023.sigma     = sigma_TprimeToTZ_13p6TeV["1600"]
TprimeToTZ_1600_2023.year      = 2023
TprimeToTZ_1600_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-1600_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_1600_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_1600_2023.unix_code = 52009
TprimeToTZ_1600_2023.EE        = 0

TprimeToTZ_1700_2023           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1700GeV", "TprimeToTZ_1700_2023")
TprimeToTZ_1700_2023.sigma     = sigma_TprimeToTZ_13p6TeV["1700"]
TprimeToTZ_1700_2023.year      = 2023
TprimeToTZ_1700_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-1700_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_1700_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_1700_2023.unix_code = 52010
TprimeToTZ_1700_2023.EE        = 0

TprimeToTZ_1800_2023           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1800GeV", "TprimeToTZ_1800_2023")
TprimeToTZ_1800_2023.sigma     = sigma_TprimeToTZ_13p6TeV["1800"]
TprimeToTZ_1800_2023.year      = 2023
TprimeToTZ_1800_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-1800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_1800_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_1800_2023.unix_code = 52011
TprimeToTZ_1800_2023.EE        = 0

TprimeToTZ_1900_2023           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1900GeV", "TprimeToTZ_1900_2023")
TprimeToTZ_1900_2023.sigma     = sigma_TprimeToTZ_13p6TeV["1900"]
TprimeToTZ_1900_2023.year      = 2023
TprimeToTZ_1900_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-1900_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_1900_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_1900_2023.unix_code = 52012
TprimeToTZ_1900_2023.EE        = 0

TprimeToTZ_2000_2023           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2000GeV", "TprimeToTZ_2000_2023")
TprimeToTZ_2000_2023.sigma     = sigma_TprimeToTZ_13p6TeV["2000"]
TprimeToTZ_2000_2023.year      = 2023
TprimeToTZ_2000_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-2000_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_2000_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_2000_2023.unix_code = 52013
TprimeToTZ_2000_2023.EE        = 0

TprimeToTZ_2200_2023           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2200GeV", "TprimeToTZ_2200_2023")
TprimeToTZ_2200_2023.sigma     = sigma_TprimeToTZ_13p6TeV["2200"]
TprimeToTZ_2200_2023.year      = 2023
TprimeToTZ_2200_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-2200_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_2200_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_2200_2023.unix_code = 52014
TprimeToTZ_2200_2023.EE        = 0

TprimeToTZ_2400_2023           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2400GeV", "TprimeToTZ_2400_2023")
TprimeToTZ_2400_2023.sigma     = sigma_TprimeToTZ_13p6TeV["2400"]
TprimeToTZ_2400_2023.year      = 2023
TprimeToTZ_2400_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-2400_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_2400_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_2400_2023.unix_code = 52015
TprimeToTZ_2400_2023.EE        = 0

TprimeToTZ_2600_2023           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2600GeV", "TprimeToTZ_2600_2023")
TprimeToTZ_2600_2023.sigma     = sigma_TprimeToTZ_13p6TeV["2600"]
TprimeToTZ_2600_2023.year      = 2023
TprimeToTZ_2600_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-2600_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_2600_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_2600_2023.unix_code = 52016
TprimeToTZ_2600_2023.EE        = 0

TprimeToTZ_2800_2023           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2800GeV", "TprimeToTZ_2800_2023")
TprimeToTZ_2800_2023.sigma     = sigma_TprimeToTZ_13p6TeV["2800"]
TprimeToTZ_2800_2023.year      = 2023
TprimeToTZ_2800_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-2800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_2800_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_2800_2023.unix_code = 52017
TprimeToTZ_2800_2023.EE        = 0

TprimeToTZ_3000_2023           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M3000GeV", "TprimeToTZ_3000_2023")
TprimeToTZ_3000_2023.sigma     = sigma_TprimeToTZ_13p6TeV["3000"]
TprimeToTZ_3000_2023.year      = 2023
TprimeToTZ_3000_2023.dataset   = '/TprimeBtoTZ-LH_Par-M-3000_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM'
TprimeToTZ_3000_2023.process   = "TprimeToTZ_2023"
TprimeToTZ_3000_2023.unix_code = 52018
TprimeToTZ_3000_2023.EE        = 0

TprimeToTZ_2023            = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ", "TprimeToTZ_2023")
TprimeToTZ_2023.year       = 2023
TprimeToTZ_2023.components = [
    TprimeToTZ_700_2023,
    TprimeToTZ_800_2023,
    TprimeToTZ_900_2023,
    TprimeToTZ_1000_2023,
    TprimeToTZ_1100_2023,
    TprimeToTZ_1200_2023,
    TprimeToTZ_1300_2023,
    TprimeToTZ_1400_2023,
    TprimeToTZ_1500_2023,
    TprimeToTZ_1600_2023,
    TprimeToTZ_1700_2023,
    TprimeToTZ_1800_2023,
    TprimeToTZ_1900_2023,
    TprimeToTZ_2000_2023,
    TprimeToTZ_2200_2023,
    TprimeToTZ_2400_2023,
    TprimeToTZ_2600_2023,
    TprimeToTZ_2800_2023,
    TprimeToTZ_3000_2023,
]

################################ VLQ T signals 2023postBPix ################################
TprimeToTZ_700_2023postBPix            = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M700GeV", "TprimeToTZ_700_2023postBPix")
TprimeToTZ_700_2023postBPix.sigma      = sigma_TprimeToTZ_13p6TeV["700"]
TprimeToTZ_700_2023postBPix.year       = 2023
TprimeToTZ_700_2023postBPix.dataset    = '/TprimeBtoTZ-LH_Par-M-700_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_700_2023postBPix.process    = "TprimeToTZ_2023postBPix"
TprimeToTZ_700_2023postBPix.unix_code  = 62000
TprimeToTZ_700_2023postBPix.EE         = 1

TprimeToTZ_800_2023postBPix            = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M800GeV", "TprimeToTZ_800_2023postBPix")
TprimeToTZ_800_2023postBPix.sigma      = sigma_TprimeToTZ_13p6TeV["800"]
TprimeToTZ_800_2023postBPix.year       = 2023
TprimeToTZ_800_2023postBPix.dataset    = '/TprimeBtoTZ-LH_Par-M-800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_800_2023postBPix.process    = "TprimeToTZ_2023postBPix"
TprimeToTZ_800_2023postBPix.unix_code  = 62001
TprimeToTZ_800_2023postBPix.EE         = 1

TprimeToTZ_900_2023postBPix            = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M900GeV", "TprimeToTZ_900_2023postBPix")
TprimeToTZ_900_2023postBPix.sigma      = sigma_TprimeToTZ_13p6TeV["900"]
TprimeToTZ_900_2023postBPix.year       = 2023
TprimeToTZ_900_2023postBPix.dataset    = '/TprimeBtoTZ-LH_Par-M-900_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_900_2023postBPix.process    = "TprimeToTZ_2023postBPix"
TprimeToTZ_900_2023postBPix.unix_code  = 62002
TprimeToTZ_900_2023postBPix.EE         = 1

TprimeToTZ_1000_2023postBPix           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1000GeV", "TprimeToTZ_1000_2023postBPix")
TprimeToTZ_1000_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["1000"]
TprimeToTZ_1000_2023postBPix.year      = 2023
TprimeToTZ_1000_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-1000_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_1000_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_1000_2023postBPix.unix_code = 62003
TprimeToTZ_1000_2023postBPix.EE        = 1

TprimeToTZ_1100_2023postBPix           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1100GeV", "TprimeToTZ_1100_2023postBPix")
TprimeToTZ_1100_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["1100"]
TprimeToTZ_1100_2023postBPix.year      = 2023
TprimeToTZ_1100_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-1100_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_1100_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_1100_2023postBPix.unix_code = 62004
TprimeToTZ_1100_2023postBPix.EE        = 1

TprimeToTZ_1200_2023postBPix           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1200GeV", "TprimeToTZ_1200_2023postBPix")
TprimeToTZ_1200_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["1200"]
TprimeToTZ_1200_2023postBPix.year      = 2023
TprimeToTZ_1200_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-1200_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_1200_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_1200_2023postBPix.unix_code = 62005
TprimeToTZ_1200_2023postBPix.EE        = 1

TprimeToTZ_1300_2023postBPix           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1300GeV", "TprimeToTZ_1300_2023postBPix")
TprimeToTZ_1300_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["1300"]
TprimeToTZ_1300_2023postBPix.year      = 2023
TprimeToTZ_1300_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-1300_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_1300_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_1300_2023postBPix.unix_code = 62006
TprimeToTZ_1300_2023postBPix.EE        = 1

TprimeToTZ_1400_2023postBPix           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1400GeV", "TprimeToTZ_1400_2023postBPix")
TprimeToTZ_1400_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["1400"]
TprimeToTZ_1400_2023postBPix.year      = 2023
TprimeToTZ_1400_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-1400_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_1400_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_1400_2023postBPix.unix_code = 62007
TprimeToTZ_1400_2023postBPix.EE        = 1

TprimeToTZ_1500_2023postBPix           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1500GeV", "TprimeToTZ_1500_2023postBPix")
TprimeToTZ_1500_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["1500"]
TprimeToTZ_1500_2023postBPix.year      = 2023
TprimeToTZ_1500_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-1500_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_1500_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_1500_2023postBPix.unix_code = 62008
TprimeToTZ_1500_2023postBPix.EE        = 1

TprimeToTZ_1600_2023postBPix           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1600GeV", "TprimeToTZ_1600_2023postBPix")
TprimeToTZ_1600_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["1600"]
TprimeToTZ_1600_2023postBPix.year      = 2023
TprimeToTZ_1600_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-1600_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_1600_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_1600_2023postBPix.unix_code = 62009
TprimeToTZ_1600_2023postBPix.EE        = 1

TprimeToTZ_1700_2023postBPix           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1700GeV", "TprimeToTZ_1700_2023postBPix")
TprimeToTZ_1700_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["1700"]
TprimeToTZ_1700_2023postBPix.year      = 2023
TprimeToTZ_1700_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-1700_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_1700_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_1700_2023postBPix.unix_code = 62010
TprimeToTZ_1700_2023postBPix.EE        = 1

TprimeToTZ_1800_2023postBPix           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1800GeV", "TprimeToTZ_1800_2023postBPix")
TprimeToTZ_1800_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["1800"]
TprimeToTZ_1800_2023postBPix.year      = 2023
TprimeToTZ_1800_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-1800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_1800_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_1800_2023postBPix.unix_code = 62011
TprimeToTZ_1800_2023postBPix.EE        = 1

TprimeToTZ_1900_2023postBPix           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1900GeV", "TprimeToTZ_1900_2023postBPix")
TprimeToTZ_1900_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["1900"]
TprimeToTZ_1900_2023postBPix.year      = 2023
TprimeToTZ_1900_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-1900_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_1900_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_1900_2023postBPix.unix_code = 62012
TprimeToTZ_1900_2023postBPix.EE        = 1

TprimeToTZ_2000_2023postBPix           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2000GeV", "TprimeToTZ_2000_2023postBPix")
TprimeToTZ_2000_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["2000"]
TprimeToTZ_2000_2023postBPix.year      = 2023
TprimeToTZ_2000_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-2000_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_2000_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_2000_2023postBPix.unix_code = 62013
TprimeToTZ_2000_2023postBPix.EE        = 1

TprimeToTZ_2200_2023postBPix           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2200GeV", "TprimeToTZ_2200_2023postBPix")
TprimeToTZ_2200_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["2200"]
TprimeToTZ_2200_2023postBPix.year      = 2023
TprimeToTZ_2200_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-2200_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_2200_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_2200_2023postBPix.unix_code = 62014
TprimeToTZ_2200_2023postBPix.EE        = 1

TprimeToTZ_2400_2023postBPix           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2400GeV", "TprimeToTZ_2400_2023postBPix")
TprimeToTZ_2400_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["2400"]
TprimeToTZ_2400_2023postBPix.year      = 2023
TprimeToTZ_2400_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-2400_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_2400_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_2400_2023postBPix.unix_code = 62015
TprimeToTZ_2400_2023postBPix.EE        = 1

TprimeToTZ_2600_2023postBPix           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2600GeV", "TprimeToTZ_2600_2023postBPix")
TprimeToTZ_2600_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["2600"]
TprimeToTZ_2600_2023postBPix.year      = 2023
TprimeToTZ_2600_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-2600_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_2600_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_2600_2023postBPix.unix_code = 62016
TprimeToTZ_2600_2023postBPix.EE        = 1

TprimeToTZ_2800_2023postBPix           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2800GeV", "TprimeToTZ_2800_2023postBPix")
TprimeToTZ_2800_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["2800"]
TprimeToTZ_2800_2023postBPix.year      = 2023
TprimeToTZ_2800_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-2800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_2800_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_2800_2023postBPix.unix_code = 62017
TprimeToTZ_2800_2023postBPix.EE        = 1

TprimeToTZ_3000_2023postBPix           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M3000GeV", "TprimeToTZ_3000_2023postBPix")
TprimeToTZ_3000_2023postBPix.sigma     = sigma_TprimeToTZ_13p6TeV["3000"]
TprimeToTZ_3000_2023postBPix.year      = 2023
TprimeToTZ_3000_2023postBPix.dataset   = '/TprimeBtoTZ-LH_Par-M-3000_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM'
TprimeToTZ_3000_2023postBPix.process   = "TprimeToTZ_2023postBPix"
TprimeToTZ_3000_2023postBPix.unix_code = 62018
TprimeToTZ_3000_2023postBPix.EE        = 1

TprimeToTZ_2023postBPix            = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ", "TprimeToTZ_2023postBPix")
TprimeToTZ_2023postBPix.year       = 2023
TprimeToTZ_2023postBPix.components = [
    TprimeToTZ_700_2023postBPix,
    TprimeToTZ_800_2023postBPix,
    TprimeToTZ_900_2023postBPix,
    TprimeToTZ_1000_2023postBPix,
    TprimeToTZ_1100_2023postBPix,
    TprimeToTZ_1200_2023postBPix,
    TprimeToTZ_1300_2023postBPix,
    TprimeToTZ_1400_2023postBPix,
    TprimeToTZ_1500_2023postBPix,
    TprimeToTZ_1600_2023postBPix,
    TprimeToTZ_1700_2023postBPix,
    TprimeToTZ_1800_2023postBPix,
    TprimeToTZ_1900_2023postBPix,
    TprimeToTZ_2000_2023postBPix,
    TprimeToTZ_2200_2023postBPix,
    TprimeToTZ_2400_2023postBPix,
    TprimeToTZ_2600_2023postBPix,
    TprimeToTZ_2800_2023postBPix,
    TprimeToTZ_3000_2023postBPix,
]

################################ VLQ T signals 2024 ################################
TprimeToTZ_700_2024           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M700GeV", "TprimeToTZ_700_2024")
TprimeToTZ_700_2024.sigma     = sigma_TprimeToTZ_13p6TeV["700"]
TprimeToTZ_700_2024.year      = 2024
TprimeToTZ_700_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_700_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_700_2024.unix_code = 72000
TprimeToTZ_700_2024.EE        = 0

TprimeToTZ_800_2024           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M800GeV", "TprimeToTZ_800_2024")
TprimeToTZ_800_2024.sigma     = sigma_TprimeToTZ_13p6TeV["800"]
TprimeToTZ_800_2024.year      = 2024
TprimeToTZ_800_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_800_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_800_2024.unix_code = 72001
TprimeToTZ_800_2024.EE        = 0

TprimeToTZ_900_2024           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M900GeV", "TprimeToTZ_900_2024")
TprimeToTZ_900_2024.sigma     = sigma_TprimeToTZ_13p6TeV["900"]
TprimeToTZ_900_2024.year      = 2024
TprimeToTZ_900_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_900_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_900_2024.unix_code = 72002
TprimeToTZ_900_2024.EE        = 0

TprimeToTZ_1000_2024           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1000GeV", "TprimeToTZ_1000_2024")
TprimeToTZ_1000_2024.sigma     = sigma_TprimeToTZ_13p6TeV["1000"]
TprimeToTZ_1000_2024.year      = 2024
TprimeToTZ_1000_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM' 
TprimeToTZ_1000_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_1000_2024.unix_code = 72003
TprimeToTZ_1000_2024.EE        = 0

TprimeToTZ_1100_2024           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1100GeV", "TprimeToTZ_1100_2024")
TprimeToTZ_1100_2024.sigma     = sigma_TprimeToTZ_13p6TeV["1100"]
TprimeToTZ_1100_2024.year      = 2024
TprimeToTZ_1100_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-1100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM' 
TprimeToTZ_1100_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_1100_2024.unix_code = 72004
TprimeToTZ_1100_2024.EE        = 0

TprimeToTZ_1200_2024           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1200GeV", "TprimeToTZ_1200_2024")
TprimeToTZ_1200_2024.sigma     = sigma_TprimeToTZ_13p6TeV["1200"]
TprimeToTZ_1200_2024.year      = 2024
TprimeToTZ_1200_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-1200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_1200_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_1200_2024.unix_code = 72005
TprimeToTZ_1200_2024.EE        = 0

TprimeToTZ_1300_2024           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1300GeV", "TprimeToTZ_1300_2024")
TprimeToTZ_1300_2024.sigma     = sigma_TprimeToTZ_13p6TeV["1300"]
TprimeToTZ_1300_2024.year      = 2024
TprimeToTZ_1300_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-1300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_1300_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_1300_2024.unix_code = 72006
TprimeToTZ_1300_2024.EE        = 0

TprimeToTZ_1400_2024           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1400GeV", "TprimeToTZ_1400_2024")
TprimeToTZ_1400_2024.sigma     = sigma_TprimeToTZ_13p6TeV["1400"]
TprimeToTZ_1400_2024.year      = 2024
TprimeToTZ_1400_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-1400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_1400_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_1400_2024.unix_code = 72007
TprimeToTZ_1400_2024.EE        = 0

TprimeToTZ_1500_2024           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1500GeV", "TprimeToTZ_1500_2024")
TprimeToTZ_1500_2024.sigma     = sigma_TprimeToTZ_13p6TeV["1500"]
TprimeToTZ_1500_2024.year      = 2024
TprimeToTZ_1500_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-1500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_1500_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_1500_2024.unix_code = 72008
TprimeToTZ_1500_2024.EE        = 0

TprimeToTZ_1600_2024           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1600GeV", "TprimeToTZ_1600_2024")
TprimeToTZ_1600_2024.sigma     = sigma_TprimeToTZ_13p6TeV["1600"]
TprimeToTZ_1600_2024.year      = 2024
TprimeToTZ_1600_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-1600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_1600_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_1600_2024.unix_code = 72009
TprimeToTZ_1600_2024.EE        = 0

TprimeToTZ_1700_2024           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1700GeV", "TprimeToTZ_1700_2024")
TprimeToTZ_1700_2024.sigma     = sigma_TprimeToTZ_13p6TeV["1700"]
TprimeToTZ_1700_2024.year      = 2024
TprimeToTZ_1700_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-1700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_1700_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_1700_2024.unix_code = 72010
TprimeToTZ_1700_2024.EE        = 0

TprimeToTZ_1800_2024           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1800GeV", "TprimeToTZ_1800_2024")
TprimeToTZ_1800_2024.sigma     = sigma_TprimeToTZ_13p6TeV["1800"]
TprimeToTZ_1800_2024.year      = 2024
TprimeToTZ_1800_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-1800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_1800_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_1800_2024.unix_code = 72011
TprimeToTZ_1800_2024.EE        = 0

TprimeToTZ_1900_2024           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1900GeV", "TprimeToTZ_1900_2024")
TprimeToTZ_1900_2024.sigma     = sigma_TprimeToTZ_13p6TeV["1900"]
TprimeToTZ_1900_2024.year      = 2024
TprimeToTZ_1900_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-1900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_1900_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_1900_2024.unix_code = 72012
TprimeToTZ_1900_2024.EE        = 0

TprimeToTZ_2000_2024           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2000GeV", "TprimeToTZ_2000_2024")
TprimeToTZ_2000_2024.sigma     = sigma_TprimeToTZ_13p6TeV["2000"]
TprimeToTZ_2000_2024.year      = 2024
TprimeToTZ_2000_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-2000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_2000_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_2000_2024.unix_code = 72013
TprimeToTZ_2000_2024.EE        = 0

TprimeToTZ_2200_2024           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2200GeV", "TprimeToTZ_2200_2024")
TprimeToTZ_2200_2024.sigma     = sigma_TprimeToTZ_13p6TeV["2200"]
TprimeToTZ_2200_2024.year      = 2024
TprimeToTZ_2200_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-2200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_2200_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_2200_2024.unix_code = 72014
TprimeToTZ_2200_2024.EE        = 0

TprimeToTZ_2400_2024           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2400GeV", "TprimeToTZ_2400_2024")
TprimeToTZ_2400_2024.sigma     = sigma_TprimeToTZ_13p6TeV["2400"]
TprimeToTZ_2400_2024.year      = 2024
TprimeToTZ_2400_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-2400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_2400_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_2400_2024.unix_code = 72015
TprimeToTZ_2400_2024.EE        = 0

TprimeToTZ_2600_2024           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2600GeV", "TprimeToTZ_2600_2024")
TprimeToTZ_2600_2024.sigma     = sigma_TprimeToTZ_13p6TeV["2600"]
TprimeToTZ_2600_2024.year      = 2024
TprimeToTZ_2600_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-2600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_2600_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_2600_2024.unix_code = 72016
TprimeToTZ_2600_2024.EE        = 0

TprimeToTZ_2800_2024           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M2800GeV", "TprimeToTZ_2800_2024")
TprimeToTZ_2800_2024.sigma     = sigma_TprimeToTZ_13p6TeV["2800"]
TprimeToTZ_2800_2024.year      = 2024
TprimeToTZ_2800_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-2800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_2800_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_2800_2024.unix_code = 72017
TprimeToTZ_2800_2024.EE        = 0

TprimeToTZ_3000_2024           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M3000GeV", "TprimeToTZ_3000_2024")
TprimeToTZ_3000_2024.sigma     = sigma_TprimeToTZ_13p6TeV["3000"]
TprimeToTZ_3000_2024.year      = 2024
TprimeToTZ_3000_2024.dataset   = '/TprimeBtoTZ-LH_Par-M-3000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM'
TprimeToTZ_3000_2024.process   = "TprimeToTZ_2024"
TprimeToTZ_3000_2024.unix_code = 72018
TprimeToTZ_3000_2024.EE        = 0

TprimeToTZ_2024            = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ", "TprimeToTZ_2024")
TprimeToTZ_2024.year       = 2024
TprimeToTZ_2024.components = [
    TprimeToTZ_700_2024,
    TprimeToTZ_800_2024,
    TprimeToTZ_900_2024,
    TprimeToTZ_1000_2024,
    TprimeToTZ_1100_2024,
    TprimeToTZ_1200_2024,
    TprimeToTZ_1300_2024,
    TprimeToTZ_1400_2024,
    TprimeToTZ_1500_2024,
    TprimeToTZ_1600_2024,
    TprimeToTZ_1700_2024,
    TprimeToTZ_1800_2024,
    TprimeToTZ_1900_2024,
    TprimeToTZ_2000_2024,
    TprimeToTZ_2200_2024,
    TprimeToTZ_2400_2024,
    TprimeToTZ_2600_2024,
    TprimeToTZ_2800_2024,
    TprimeToTZ_3000_2024,
]

samples_dict_tprime_signals = {
    ########## 2018
    "TprimeToTZ_1800_2018": TprimeToTZ_1800_2018,
    "TprimeToTZ_1000_2018": TprimeToTZ_1000_2018,
    "TprimeToTZ_700_2018":  TprimeToTZ_700_2018,

    ########## 2022
    "TprimeToTZ_2022":      TprimeToTZ_2022,
    "TprimeToTZ_700_2022":  TprimeToTZ_700_2022,
    "TprimeToTZ_800_2022":  TprimeToTZ_800_2022,
    "TprimeToTZ_900_2022":  TprimeToTZ_900_2022,
    "TprimeToTZ_1000_2022": TprimeToTZ_1000_2022,
    "TprimeToTZ_1100_2022": TprimeToTZ_1100_2022,
    "TprimeToTZ_1200_2022": TprimeToTZ_1200_2022,
    "TprimeToTZ_1300_2022": TprimeToTZ_1300_2022,
    "TprimeToTZ_1400_2022": TprimeToTZ_1400_2022,
    "TprimeToTZ_1500_2022": TprimeToTZ_1500_2022,
    "TprimeToTZ_1600_2022": TprimeToTZ_1600_2022,
    "TprimeToTZ_1700_2022": TprimeToTZ_1700_2022,
    "TprimeToTZ_1800_2022": TprimeToTZ_1800_2022,
    "TprimeToTZ_1900_2022": TprimeToTZ_1900_2022,
    "TprimeToTZ_2000_2022": TprimeToTZ_2000_2022,
    "TprimeToTZ_2200_2022": TprimeToTZ_2200_2022,
    "TprimeToTZ_2400_2022": TprimeToTZ_2400_2022,
    "TprimeToTZ_2600_2022": TprimeToTZ_2600_2022,
    "TprimeToTZ_2800_2022": TprimeToTZ_2800_2022,
    "TprimeToTZ_3000_2022": TprimeToTZ_3000_2022,

    ########## 2022EE
    "TprimeToTZ_2022EE":      TprimeToTZ_2022EE,
    "TprimeToTZ_700_2022EE":  TprimeToTZ_700_2022EE,
    "TprimeToTZ_800_2022EE":  TprimeToTZ_800_2022EE,
    "TprimeToTZ_900_2022EE":  TprimeToTZ_900_2022EE,
    "TprimeToTZ_1000_2022EE": TprimeToTZ_1000_2022EE,
    "TprimeToTZ_1100_2022EE": TprimeToTZ_1100_2022EE,
    "TprimeToTZ_1200_2022EE": TprimeToTZ_1200_2022EE,
    "TprimeToTZ_1300_2022EE": TprimeToTZ_1300_2022EE,
    "TprimeToTZ_1400_2022EE": TprimeToTZ_1400_2022EE,
    "TprimeToTZ_1500_2022EE": TprimeToTZ_1500_2022EE,
    "TprimeToTZ_1600_2022EE": TprimeToTZ_1600_2022EE,
    "TprimeToTZ_1700_2022EE": TprimeToTZ_1700_2022EE,
    "TprimeToTZ_1800_2022EE": TprimeToTZ_1800_2022EE,
    "TprimeToTZ_1900_2022EE": TprimeToTZ_1900_2022EE,
    "TprimeToTZ_2000_2022EE": TprimeToTZ_2000_2022EE,
    "TprimeToTZ_2200_2022EE": TprimeToTZ_2200_2022EE,
    "TprimeToTZ_2400_2022EE": TprimeToTZ_2400_2022EE,
    "TprimeToTZ_2600_2022EE": TprimeToTZ_2600_2022EE,
    "TprimeToTZ_2800_2022EE": TprimeToTZ_2800_2022EE,
    "TprimeToTZ_3000_2022EE": TprimeToTZ_3000_2022EE,

    ########## 2023
    "TprimeToTZ_2023":      TprimeToTZ_2023,
    "TprimeToTZ_700_2023":  TprimeToTZ_700_2023,
    "TprimeToTZ_800_2023":  TprimeToTZ_800_2023,
    "TprimeToTZ_900_2023":  TprimeToTZ_900_2023,
    "TprimeToTZ_1000_2023": TprimeToTZ_1000_2023,
    "TprimeToTZ_1100_2023": TprimeToTZ_1100_2023,
    "TprimeToTZ_1200_2023": TprimeToTZ_1200_2023,
    "TprimeToTZ_1300_2023": TprimeToTZ_1300_2023,
    "TprimeToTZ_1400_2023": TprimeToTZ_1400_2023,
    "TprimeToTZ_1500_2023": TprimeToTZ_1500_2023,
    "TprimeToTZ_1600_2023": TprimeToTZ_1600_2023,
    "TprimeToTZ_1700_2023": TprimeToTZ_1700_2023,
    "TprimeToTZ_1800_2023": TprimeToTZ_1800_2023,
    "TprimeToTZ_1900_2023": TprimeToTZ_1900_2023,
    "TprimeToTZ_2000_2023": TprimeToTZ_2000_2023,
    "TprimeToTZ_2200_2023": TprimeToTZ_2200_2023,
    "TprimeToTZ_2400_2023": TprimeToTZ_2400_2023,
    "TprimeToTZ_2600_2023": TprimeToTZ_2600_2023,
    "TprimeToTZ_2800_2023": TprimeToTZ_2800_2023,
    "TprimeToTZ_3000_2023": TprimeToTZ_3000_2023,

    ########## 2023postBPix
    "TprimeToTZ_2023postBPix":      TprimeToTZ_2023postBPix,
    "TprimeToTZ_700_2023postBPix":  TprimeToTZ_700_2023postBPix,
    "TprimeToTZ_800_2023postBPix":  TprimeToTZ_800_2023postBPix,
    "TprimeToTZ_900_2023postBPix":  TprimeToTZ_900_2023postBPix,
    "TprimeToTZ_1000_2023postBPix": TprimeToTZ_1000_2023postBPix,
    "TprimeToTZ_1100_2023postBPix": TprimeToTZ_1100_2023postBPix,
    "TprimeToTZ_1200_2023postBPix": TprimeToTZ_1200_2023postBPix,
    "TprimeToTZ_1300_2023postBPix": TprimeToTZ_1300_2023postBPix,
    "TprimeToTZ_1400_2023postBPix": TprimeToTZ_1400_2023postBPix,
    "TprimeToTZ_1500_2023postBPix": TprimeToTZ_1500_2023postBPix,
    "TprimeToTZ_1600_2023postBPix": TprimeToTZ_1600_2023postBPix,
    "TprimeToTZ_1700_2023postBPix": TprimeToTZ_1700_2023postBPix,
    "TprimeToTZ_1800_2023postBPix": TprimeToTZ_1800_2023postBPix,
    "TprimeToTZ_1900_2023postBPix": TprimeToTZ_1900_2023postBPix,
    "TprimeToTZ_2000_2023postBPix": TprimeToTZ_2000_2023postBPix,
    "TprimeToTZ_2200_2023postBPix": TprimeToTZ_2200_2023postBPix,
    "TprimeToTZ_2400_2023postBPix": TprimeToTZ_2400_2023postBPix,
    "TprimeToTZ_2600_2023postBPix": TprimeToTZ_2600_2023postBPix,
    "TprimeToTZ_2800_2023postBPix": TprimeToTZ_2800_2023postBPix,
    "TprimeToTZ_3000_2023postBPix": TprimeToTZ_3000_2023postBPix,

    ########## 2024
    "TprimeToTZ_2024":      TprimeToTZ_2024,
    "TprimeToTZ_700_2024":  TprimeToTZ_700_2024,
    "TprimeToTZ_800_2024":  TprimeToTZ_800_2024,
    "TprimeToTZ_900_2024":  TprimeToTZ_900_2024,
    "TprimeToTZ_1000_2024": TprimeToTZ_1000_2024,
    "TprimeToTZ_1100_2024": TprimeToTZ_1100_2024,
    "TprimeToTZ_1200_2024": TprimeToTZ_1200_2024,
    "TprimeToTZ_1300_2024": TprimeToTZ_1300_2024,
    "TprimeToTZ_1400_2024": TprimeToTZ_1400_2024,
    "TprimeToTZ_1500_2024": TprimeToTZ_1500_2024,
    "TprimeToTZ_1600_2024": TprimeToTZ_1600_2024,
    "TprimeToTZ_1700_2024": TprimeToTZ_1700_2024,
    "TprimeToTZ_1800_2024": TprimeToTZ_1800_2024,
    "TprimeToTZ_1900_2024": TprimeToTZ_1900_2024,
    "TprimeToTZ_2000_2024": TprimeToTZ_2000_2024,
    "TprimeToTZ_2200_2024": TprimeToTZ_2200_2024,
    "TprimeToTZ_2400_2024": TprimeToTZ_2400_2024,
    "TprimeToTZ_2600_2024": TprimeToTZ_2600_2024,
    "TprimeToTZ_2800_2024": TprimeToTZ_2800_2024,
    "TprimeToTZ_3000_2024": TprimeToTZ_3000_2024,
}
