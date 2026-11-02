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

#da controllare i tag aggiungere la QCD

tag_2016 = 'RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8'
tag_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8'
tag2_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8'
tag_2018 = 'RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21'

################################ WJets ################################
altXSUp=0
kFactorsQCD={
    "WJetsHT100to200" : 1.21,
    "WJetsHT200to400" : 1.21,
    "WJetsHT400to600" : 1.21,
    "WJetsHT600to800" : 1.21,
    "WJetsHT800to1200" : 1.21,
    "WJetsHT1200to2500" : 1.21,
    "WJetsHT2500toInf" : 1.21
}

BR_t_to_bqq_13p6TeV     = 0.665                         # https://pdg.lbl.gov/2026/listings/rpp2026-list-t-quark.pdf
BR_t_to_blv_13p6TeV     = 0.1110 + 0.1140 + 0.107       # (e+mu+tau) https://pdg.lbl.gov/2026/listings/rpp2026-list-t-quark.pdf
BR_W_to_qq_13p6TeV      = 0.6741                        # https://pdg.lbl.gov/2026/listings/rpp2026-list-w-boson.pdf
BR_W_to_lv_13p6TeV      = 0.1071 + 0.1063 + 0.1138      # (e+mu+tau) https://pdg.lbl.gov/2026/listings/rpp2026-list-w-boson.pdf
BR_W_to_ev_13p6TeV      = 0.1071                        # https://pdg.lbl.gov/2026/listings/rpp2026-list-w-boson.pdf
BR_W_to_muv_13p6TeV     = 0.1063                        # https://pdg.lbl.gov/2026/listings/rpp2026-list-w-boson.pdf
BR_W_to_tauv_13p6TeV    = 0.1138                        # https://pdg.lbl.gov/2026/listings/rpp2026-list-w-boson.pdf
sigma_ttbar_13p6TeV     = 923.6                         # https://pdg.lbl.gov/2026/listings/rpp2026-list-t-quark.pdf
sigma_tWminus_13p6TeV   = 87.9 * 0.5                    # sigma(t+tbar) * asymmetry(t,tbar) https://pdg.lbl.gov/2026/listings/rpp2026-list-t-quark.pdf, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef#Single_top_quark_tW_channel_cros
sigma_tbarWplus_13p6TeV = 87.9 * 0.5                    # sigma(t+tbar) * asymmetry(t,tbar) https://pdg.lbl.gov/2026/listings/rpp2026-list-t-quark.pdf, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef#Single_top_quark_tW_channel_cros

###############################################################################################################################
##########################################                                           ##########################################
##########################################                    2018                   ##########################################
##########################################                                           ##########################################
###############################################################################################################################

################################ QCD ################################
QCDHT_100to200_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_100to200_2018")
QCDHT_100to200_2018.sigma   = 27990000 #23590000 #pb
QCDHT_100to200_2018.year    = 2018
QCDHT_100to200_2018.dataset = '/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_100to200_2018.process = 'QCD_2018'
QCDHT_100to200_2018.unix_code = 21000

QCDHT_200to300_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_200to300_2018")
QCDHT_200to300_2018.sigma   = 1712000#1555000 #pb
QCDHT_200to300_2018.year    = 2018
QCDHT_200to300_2018.dataset = '/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_200to300_2018.process = 'QCD_2018'
QCDHT_200to300_2018.unix_code = 21001

QCDHT_300to500_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_300to500_2018")
QCDHT_300to500_2018.sigma   = 347700 #324500 #pb
QCDHT_300to500_2018.year    = 2018
QCDHT_300to500_2018.dataset = '/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_300to500_2018.process = 'QCD_2018'
QCDHT_300to500_2018.unix_code = 21002
# QCDHT_300to500_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/QCD_HT300to500_2018_Skim.root"

QCDHT_500to700_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_500to700_2018")
QCDHT_500to700_2018.sigma   = 32100 #30310 #pb
QCDHT_500to700_2018.year    = 2018
QCDHT_500to700_2018.dataset = '/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_500to700_2018.process = 'QCD_2018'
QCDHT_500to700_2018.unix_code = 21003
# QCDHT_500to700_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/QCD_HT500to700_2018_Skim.root"

QCDHT_700to1000_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_700to1000_2018")
QCDHT_700to1000_2018.sigma   = 6832 #6444 #pb
QCDHT_700to1000_2018.year    = 2018
QCDHT_700to1000_2018.dataset = '/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_700to1000_2018.process = 'QCD_2018'
QCDHT_700to1000_2018.unix_code = 21004
# QCDHT_700to1000_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/QCD_HT700to1000_2018_Skim.root"

QCDHT_1000to1500_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1000to1500_2018")
QCDHT_1000to1500_2018.sigma   = 1207 #1127 #pb
QCDHT_1000to1500_2018.year    = 2018
QCDHT_1000to1500_2018.dataset = '/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_1000to1500_2018.process = 'QCD_2018'
QCDHT_1000to1500_2018.unix_code = 21005
# QCDHT_1000to1500_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/QCD_HT1000_Skim.root"

QCDHT_1500to2000_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1500to2000_2018")
QCDHT_1500to2000_2018.sigma   = 119.9 #109.8 #pb
QCDHT_1500to2000_2018.year    = 2018
QCDHT_1500to2000_2018.dataset = '/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_1500to2000_2018.process = 'QCD_2018'
QCDHT_1500to2000_2018.unix_code = 21006
# QCDHT_1500to2000_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/QCD-HT1500to2000_2018_Skim.root"

QCDHT_2000toInf_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_2000toInf_2018")
QCDHT_2000toInf_2018.sigma   = 25.24 #21.98 #pb   #####
QCDHT_2000toInf_2018.year    = 2018
QCDHT_2000toInf_2018.dataset = '/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_2000toInf_2018.process = 'QCD_2018'
QCDHT_2000toInf_2018.unix_code = 21007
# QCDHT_2000toInf_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/QCD-HT2000toInf_2018_Skim.root"

QCD_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2018")
QCD_2018.year = 2018
QCD_2018.components = [QCDHT_100to200_2018, QCDHT_200to300_2018,
                       QCDHT_300to500_2018, QCDHT_500to700_2018, 
                       QCDHT_700to1000_2018, QCDHT_1000to1500_2018, 
                       QCDHT_1500to2000_2018, QCDHT_2000toInf_2018]

#QCD_2018.components = [QCDHT_300to500_2018, QCDHT_500to700_2018, QCDHT_1000to1500_2018, QCDHT_1500to2000_2018, QCDHT_2000toInf_2018]

################################ TTbar ################################

TT_hadr_2018         = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_hadr_2018")
TT_hadr_2018.sigma   = 380.94 #687.1 #pb
TT_hadr_2018.year    = 2018
TT_hadr_2018.dataset = '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
TT_hadr_2018.process = 'TT_2018'
TT_hadr_2018.unix_code = 21101
# TT_hadr_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/TT_Hadr_2018_Skim.root"

TT_Mtt700to1000_2018         = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt700to1000_2018")
TT_Mtt700to1000_2018.sigma   = 80.5 #pb
TT_Mtt700to1000_2018.year    = 2018
TT_Mtt700to1000_2018.dataset = '/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
TT_Mtt700to1000_2018.process = 'TT_2018'
TT_Mtt700to1000_2018.unix_code = 21102
# TT_Mtt700to1000_2018.local_path= "/eos/home-a/acagnott/DarkMatter/topcandidate_file/TT_Mtt-700to1000_2018_Skim.root"

TT_Mtt1000toInf_2018         = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt1000toInf_2018")
TT_Mtt1000toInf_2018.sigma   = 21.3 #pb
TT_Mtt1000toInf_2018.year    = 2018
TT_Mtt1000toInf_2018.dataset = '/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
TT_Mtt1000toInf_2018.process = 'TT_2018'
TT_Mtt1000toInf_2018.unix_code = 21103
# TT_Mtt1000toInf_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/TT_Mtt-1000toInf_2018_Skim.root"

TT_semilep_2018         = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2018")
TT_semilep_2018.sigma   = 364.51 #pb
TT_semilep_2018.year    = 2018
TT_semilep_2018.dataset = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
TT_semilep_2018.process = 'TT_2018'
TT_semilep_2018.unix_code = 21104
# TT_semilep_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/TT_SemiLep_2018_Skim.root"

TT_2018             = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_2018")
TT_2018.year        = 2018
TT_2018.components  = [TT_hadr_2018, TT_semilep_2018, TT_Mtt1000toInf_2018, TT_Mtt700to1000_2018]

################################ ZJetsToNuNu ################################
ZJetsToNuNu_HT100to200_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT100to200_2018")
ZJetsToNuNu_HT100to200_2018.sigma   = 280.35 * 1.37 #267.0	 #pb 
ZJetsToNuNu_HT100to200_2018.year    = 2018
ZJetsToNuNu_HT100to200_2018.dataset = '/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT100to200_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT100to200_2018.unix_code = 21200
# ZJetsToNuNu_HT100to200_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT100to200_2018_Skim.root'

ZJetsToNuNu_HT200to400_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT200to400_2018")
ZJetsToNuNu_HT200to400_2018.sigma   = 77.67*1.52 #73.08 #pb
ZJetsToNuNu_HT200to400_2018.year    = 2018
ZJetsToNuNu_HT200to400_2018.dataset = '/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT200to400_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT200to400_2018.unix_code = 21201
# ZJetsToNuNu_HT200to400_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT200to400_2018_Skim.root'

ZJetsToNuNu_HT400to600_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT400to600_2018")
ZJetsToNuNu_HT400to600_2018.sigma   = 10.73*1.37 #9.904	 #pb
ZJetsToNuNu_HT400to600_2018.year    = 2018
ZJetsToNuNu_HT400to600_2018.dataset = '/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT400to600_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT400to600_2018.unix_code = 21202
# ZJetsToNuNu_HT400to600_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT400to600_2018_Skim.root'

ZJetsToNuNu_HT600to800_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT600to800_2018")
ZJetsToNuNu_HT600to800_2018.sigma   = 2.56*1.04 #2.413 #pb
ZJetsToNuNu_HT600to800_2018.year    = 2018
ZJetsToNuNu_HT600to800_2018.dataset = '/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT600to800_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT600to800_2018.unix_code = 21203
# ZJetsToNuNu_HT600to800_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT600to800_2018_Skim.root'

ZJetsToNuNu_HT800to1200_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT800to1200_2018")
ZJetsToNuNu_HT800to1200_2018.sigma   = 1.18*1.14 #1.071 #pb
ZJetsToNuNu_HT800to1200_2018.year    = 2018
ZJetsToNuNu_HT800to1200_2018.dataset = '/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT800to1200_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT800to1200_2018.unix_code = 21204
# ZJetsToNuNu_HT800to1200_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT800to1200_2018_Skim.root'

ZJetsToNuNu_HT1200to2500_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT1200to2500_2018")
ZJetsToNuNu_HT1200to2500_2018.sigma   = 0.29*0.88 #0.2497 #pb
ZJetsToNuNu_HT1200to2500_2018.year    = 2018
ZJetsToNuNu_HT1200to2500_2018.dataset = '/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT1200to2500_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT1200to2500_2018.unix_code = 21205
# ZJetsToNuNu_HT1200to2500_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT1200to2500_2018_Skim.root'

ZJetsToNuNu_HT2500toInf_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT2500toInf_2018")
ZJetsToNuNu_HT2500toInf_2018.sigma   = 0.007*0.88 #0.005618	 #pb
ZJetsToNuNu_HT2500toInf_2018.year    = 2018
ZJetsToNuNu_HT2500toInf_2018.dataset = '/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT2500toInf_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT2500toInf_2018.unix_code = 21206
# ZJetsToNuNu_HT2500toInf_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT2500toInf_2018_Skim.root'

ZJetsToNuNu_2018            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2018")
ZJetsToNuNu_2018.year       = 2018
ZJetsToNuNu_2018.components = [ZJetsToNuNu_HT100to200_2018, ZJetsToNuNu_HT200to400_2018, 
                               ZJetsToNuNu_HT400to600_2018, ZJetsToNuNu_HT600to800_2018, 
                               ZJetsToNuNu_HT800to1200_2018, ZJetsToNuNu_HT1200to2500_2018, 
                               ZJetsToNuNu_HT2500toInf_2018]

#ZJetsToNuNu_2018.components = [ZJetsToNuNu_HT100to200_2018, ZJetsToNuNu_HT200to400_2018, ZJetsToNuNu_HT400to600_2018, ZJetsToNuNu_HT600to800_2018, ZJetsToNuNu_HT1200to2500_2018, ZJetsToNuNu_HT2500toInf_2018]

################################ WJets ################################

WJetsHT70to100_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT70to100_2018")
WJetsHT70to100_2018.sigma   = 1353.0 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT70to100_2018.year    = 2018
WJetsHT70to100_2018.dataset = '/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
WJetsHT70to100_2018.process = 'WJets_2018'
WJetsHT70to100_2018.unix_code = 21200

WJetsHT100to200_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT100to200_2018")
WJetsHT100to200_2018.sigma   = 1345 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT100to200_2018.year    = 2018
WJetsHT100to200_2018.dataset = '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
WJetsHT100to200_2018.process = 'WJets_2018'
WJetsHT100to200_2018.unix_code = 21201

WJetsHT200to400_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT200to400_2018")
WJetsHT200to400_2018.sigma   = 359.7 * kFactorsQCD["WJetsHT200to400"] #pb
WJetsHT200to400_2018.year    = 2018
WJetsHT200to400_2018.dataset = '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
WJetsHT200to400_2018.process = 'WJets_2018'
WJetsHT200to400_2018.unix_code = 21202

WJetsHT400to600_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT400to600_2018")
WJetsHT400to600_2018.sigma   = 48.91 * kFactorsQCD["WJetsHT400to600"] #pb
WJetsHT400to600_2018.year    = 2018
WJetsHT400to600_2018.dataset = '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM'
WJetsHT400to600_2018.process = 'WJets_2018' 
WJetsHT400to600_2018.unix_code = 21203

WJetsHT600to800_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT600to800_2018")
WJetsHT600to800_2018.sigma   = 12.05 * kFactorsQCD["WJetsHT600to800"] #pb
WJetsHT600to800_2018.year    = 2018
WJetsHT600to800_2018.dataset = '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM'
WJetsHT600to800_2018.process = 'WJets_2018'
WJetsHT600to800_2018.unix_code = 21204

WJetsHT800to1200_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT800to1200_2018")
WJetsHT800to1200_2018.sigma   = 5.501 * kFactorsQCD["WJetsHT800to1200"] #pb
WJetsHT800to1200_2018.year    = 2018
WJetsHT800to1200_2018.dataset = '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM'
WJetsHT800to1200_2018.process = 'WJets_2018' 
WJetsHT800to1200_2018.unix_code = 21205

WJetsHT1200to2500_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT1200to2500_2018")
WJetsHT1200to2500_2018.sigma   = 1.329 * kFactorsQCD["WJetsHT1200to2500"] #pb
WJetsHT1200to2500_2018.year    = 2018
WJetsHT1200to2500_2018.dataset = '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM'
WJetsHT1200to2500_2018.process = 'WJets_2018' 
WJetsHT1200to2500_2018.unix_code = 21206

WJetsHT2500toInf_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT2500toInf_2018")
WJetsHT2500toInf_2018.sigma   = 0.03216 * kFactorsQCD["WJetsHT2500toInf"] #pb
WJetsHT2500toInf_2018.year    = 2018
WJetsHT2500toInf_2018.dataset = '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM'
WJetsHT2500toInf_2018.process = 'WJets_2018'
WJetsHT2500toInf_2018.unix_code = 21207

WJets_2018 = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2018")
WJets_2018.year = 2018
WJets_2018.components = [#WJetsHT70to100_2018, 
                         WJetsHT100to200_2018, WJetsHT200to400_2018, 
                         WJetsHT400to600_2018, WJetsHT600to800_2018, 
                         WJetsHT800to1200_2018, WJetsHT1200to2500_2018, 
                         WJetsHT2500toInf_2018]

################################ Signal tDM ################################

tDM_mPhi1000_mChi1_2018 = sample(ROOT.kGreen+2, 1, 1001, "DM (m_{#Phi}=1000)", "tDM_mPhi1000_mChi1_2018")
tDM_mPhi1000_mChi1_2018.sigma = 24.99 *0.00001 #*100    #pb  aggiunto*100 per i plot
tDM_mPhi1000_mChi1_2018.year = 2018
tDM_mPhi1000_mChi1_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/tDM_mPhi1000_mChi1_Skim.root"
tDM_mPhi1000_mChi1_2018.unix_code = 22100

tDM_mPhi500_mChi1_2018 = sample(ROOT.kGreen+1, 1, 1001, "DM (m_{#Phi}=500)", "tDM_mPhi500_mChi1_2018")
tDM_mPhi500_mChi1_2018.year = 2018
tDM_mPhi500_mChi1_2018.sigma = 43.85 *0.0001  #pb
tDM_mPhi500_mChi1_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/tDM_mPhi500_mChi1_Skim.root"
tDM_mPhi500_mChi1_2018.unix_code = 22101

tDM_mPhi50_mChi1_2018= sample(ROOT.kGreen, 1, 1001, "DM (m_{#Phi}=50)", "tDM_mPhi50_mChi1_2018")
tDM_mPhi50_mChi1_2018.year = 2018
tDM_mPhi50_mChi1_2018.sigma = 0.7  #pb
tDM_mPhi50_mChi1_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/tDM_mPhi50_mChi1_Skim.root"
tDM_mPhi50_mChi1_2018.unix_code = 22102

###############################################################################################################################
##########################################                                           ##########################################
##########################################       samples for tagger studies          ##########################################
##########################################                                           ##########################################
###############################################################################################################################
Zprime4top_500_2018          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M500GeV", "Zprime4top_500_2018")
Zprime4top_500_2018.sigma    = 1 #pb
Zprime4top_500_2018.year     = 2018
Zprime4top_500_2018.dataset  = '/TTZprimeToTT_M-500_Width4_TuneCP5_13TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-500_Width4_nanoaod_hotvr_UL2018v1_230510-00000000000000000000000000000000/USER'

Zprime4top_1000_2018          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M1000GeV", "Zprime4top_1000_2018")
Zprime4top_1000_2018.sigma    = 1 #pb
Zprime4top_1000_2018.year     = 2018
Zprime4top_1000_2018.dataset  = '/TTZprimeToTT_M-1000_Width4_TuneCP5_13TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-1000_Width4_nanoaod_hotvr_UL2018v1_230510-00000000000000000000000000000000/USER'

Zprime4top_2000_2018          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M2000GeV", "Zprime4top_2000_2018")
Zprime4top_2000_2018.sigma    = 1 #pb
Zprime4top_2000_2018.year     = 2018
Zprime4top_2000_2018.dataset  = '/TTZprimeToTT_M-2000_Width4_TuneCP5_13TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-2000_Width4_nanoaod_hotvr_UL2018v1_230510-00000000000000000000000000000000/USER'

###############################################################################################################################
##########################################                                           ##########################################
##########################################                    2022                   ##########################################
##########################################                                           ##########################################
###############################################################################################################################
#  EraCD (preEE) più avanti descrizione completa

################################ QCD ################################
# QCD_HT40to70_2022               = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT40to70_2022")
# QCD_HT40to70_2022.sigma         = 311400000 #pb
# QCD_HT40to70_2022.year          = 2022
# QCD_HT40to70_2022.dataset       = "/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-JMENano12p5_132X_mcRun3_2022_realistic_v3-v1/NANOAODSIM"
# QCD_HT40to70_2022.process       = "QCD_2022"
# QCD_HT40to70_2022.unix_code     = 31000
# QCD_HT40to70_2022.EE            = 0
QCD_HT70to100_2022              = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT70to100_2022")
QCD_HT70to100_2022.sigma        = 58500000 #pb
QCD_HT70to100_2022.year         = 2022
QCD_HT70to100_2022.dataset      = "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT70to100_2022.process      = "QCD_2022"
QCD_HT70to100_2022.unix_code    = 31001
QCD_HT70to100_2022.EE           = 0
QCD_HT100to200_2022             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT100to200_2022")
QCD_HT100to200_2022.sigma       = 25400000 #pb
QCD_HT100to200_2022.year        = 2022
QCD_HT100to200_2022.dataset     = "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT100to200_2022.process     = "QCD_2022"
QCD_HT100to200_2022.unix_code   = 31002
QCD_HT100to200_2022.EE          = 0
QCD_HT200to400_2022             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT200to400_2022")
QCD_HT200to400_2022.sigma       = 1961000 #pb
QCD_HT200to400_2022.year        = 2022
QCD_HT200to400_2022.dataset     = "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT200to400_2022.process     = "QCD_2022"
QCD_HT200to400_2022.unix_code   = 31003
QCD_HT200to400_2022.EE          = 0
QCD_HT400to600_2022             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT400to600_2022")
QCD_HT400to600_2022.sigma       = 95620 #pb
QCD_HT400to600_2022.year        = 2022
QCD_HT400to600_2022.dataset     = "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT400to600_2022.process     = "QCD_2022"
QCD_HT400to600_2022.unix_code   = 31004
QCD_HT400to600_2022.EE          = 0
QCD_HT600to800_2022             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT600to800_2022")
QCD_HT600to800_2022.sigma       = 13540 #pb
QCD_HT600to800_2022.year        = 2022
QCD_HT600to800_2022.dataset     = "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT600to800_2022.process     = "QCD_2022"
QCD_HT600to800_2022.unix_code   = 31005
QCD_HT600to800_2022.EE          = 0
QCD_HT800to1000_2022            = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT800to1000_2022")
QCD_HT800to1000_2022.sigma      = 3033 #pb
QCD_HT800to1000_2022.year       = 2022
QCD_HT800to1000_2022.dataset    = "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT800to1000_2022.process    = "QCD_2022"
QCD_HT800to1000_2022.unix_code  = 31006
QCD_HT800to1000_2022.EE         = 0
QCD_HT1000to1200_2022           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1000to1200_2022")
QCD_HT1000to1200_2022.sigma     = 883.7 #pb
QCD_HT1000to1200_2022.year      = 2022
QCD_HT1000to1200_2022.dataset   = "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT1000to1200_2022.process   = "QCD_2022"
QCD_HT1000to1200_2022.unix_code = 31007
QCD_HT1000to1200_2022.EE        = 0
QCD_HT1200to1500_2022           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1200to1500_2022")
QCD_HT1200to1500_2022.sigma     = 383.5 #pb 
QCD_HT1200to1500_2022.year      = 2022
QCD_HT1200to1500_2022.dataset   = "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT1200to1500_2022.process   = "QCD_2022"
QCD_HT1200to1500_2022.unix_code = 31007
QCD_HT1200to1500_2022.EE        = 0
QCD_HT1500to2000_2022           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1500to2000_2022")
QCD_HT1500to2000_2022.sigma     = 125.2 #pb
QCD_HT1500to2000_2022.year      = 2022
QCD_HT1500to2000_2022.dataset   = "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT1500to2000_2022.process   = "QCD_2022"
QCD_HT1500to2000_2022.unix_code = 31008
QCD_HT1500to2000_2022.EE        = 0
QCD_HT2000_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT2000_2022")
QCD_HT2000_2022.sigma           = 26.49 #pb
QCD_HT2000_2022.year            = 2022
QCD_HT2000_2022.dataset         = "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT2000_2022.process         = "QCD_2022"
QCD_HT2000_2022.unix_code       = 31009
QCD_HT2000_2022.EE              = 0
QCD_2022                        = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2022")
QCD_2022.year                   = 2022
QCD_2022.components             = [ 
                                    # QCD_HT40to70_2022, 
                                    QCD_HT70to100_2022, QCD_HT100to200_2022, QCD_HT200to400_2022,
                                    QCD_HT400to600_2022, QCD_HT600to800_2022, QCD_HT800to1000_2022, 
                                    QCD_HT1000to1200_2022, QCD_HT1200to1500_2022,
                                    QCD_HT1500to2000_2022, QCD_HT2000_2022
                                ]


################################ TTbar ################################
TT_semilep_2022             = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2022")
TT_semilep_2022.sigma       = sigma_ttbar_13p6TeV * BR_t_to_bqq_13p6TeV * BR_t_to_blv_13p6TeV * 2 #pb
TT_semilep_2022.year        = 2022
TT_semilep_2022.dataset     = "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
TT_semilep_2022.process     = 'TT_2022'
TT_semilep_2022.unix_code   = 31100
TT_semilep_2022.EE          = 0

TT_hadr_2022                = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_hadr_2022")
TT_hadr_2022.sigma          = sigma_ttbar_13p6TeV * BR_t_to_bqq_13p6TeV * BR_t_to_bqq_13p6TeV
TT_hadr_2022.year           = 2022
TT_hadr_2022.dataset        = "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
TT_hadr_2022.process        = 'TT_2022'
TT_hadr_2022.unix_code      = 31101
TT_hadr_2022.EE             = 0

TT_dilep_2022               = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_dilep_2022")
TT_dilep_2022.sigma         = sigma_ttbar_13p6TeV * BR_t_to_blv_13p6TeV * BR_t_to_blv_13p6TeV
TT_dilep_2022.year          = 2022
TT_dilep_2022.dataset       = "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
TT_dilep_2022.process       = 'TT_2022'
TT_dilep_2022.unix_code     = 31102
TT_dilep_2022.EE            = 0

TT_2022                     = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_2022")
TT_2022.year                = 2022
TT_2022.components          = [
                                TT_semilep_2022,
                                TT_hadr_2022,
                                TT_dilep_2022
                                ]

################################ SingleTop ################################
TWminustoLNu2Q_2022             = sample(ROOT.kViolet, 1, 1001, "tW", "TWminustoLNu2Q_2022")
TWminustoLNu2Q_2022.sigma       = sigma_tWminus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_lv_13p6TeV + BR_t_to_blv_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TWminustoLNu2Q_2022.year        = 2022
TWminustoLNu2Q_2022.dataset     = "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
TWminustoLNu2Q_2022.process     = 'TW_2022'
TWminustoLNu2Q_2022.EE          = 0

TWminusto4Q_2022                = sample(ROOT.kViolet, 1, 1001, "tW", "TWminusto4Q_2022")
TWminusto4Q_2022.sigma          = sigma_tWminus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TWminusto4Q_2022.year           = 2022
TWminusto4Q_2022.dataset        = "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
TWminusto4Q_2022.process        = 'TW_2022'
TWminusto4Q_2022.EE             = 0

TWminusto2L2Nu_2022             = sample(ROOT.kViolet, 1, 1001, "tW", "TWminusto2L2Nu_2022")
TWminusto2L2Nu_2022.sigma       = sigma_tWminus_13p6TeV * (BR_t_to_blv_13p6TeV * BR_W_to_lv_13p6TeV) #pb
TWminusto2L2Nu_2022.year        = 2022
TWminusto2L2Nu_2022.dataset     = "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
TWminusto2L2Nu_2022.process     = 'TW_2022'
TWminusto2L2Nu_2022.EE          = 0

TbarWplustoLNu2Q_2022           = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplustoLNu2Q_2022")
TbarWplustoLNu2Q_2022.sigma     = sigma_tbarWplus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_lv_13p6TeV + BR_t_to_blv_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TbarWplustoLNu2Q_2022.year      = 2022
TbarWplustoLNu2Q_2022.dataset   = "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
TbarWplustoLNu2Q_2022.process   = 'TW_2022'
TbarWplustoLNu2Q_2022.EE        = 0

TbarWplusto4Q_2022              = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplusto4Q_2022")
TbarWplusto4Q_2022.sigma        = sigma_tbarWplus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TbarWplusto4Q_2022.year         = 2022
TbarWplusto4Q_2022.dataset      = "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
TbarWplusto4Q_2022.process      = 'TW_2022'
TbarWplusto4Q_2022.EE           = 0

TbarWplusto2L2Nu_2022           = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplusto2L2Nu_2022")
TbarWplusto2L2Nu_2022.sigma     = sigma_tbarWplus_13p6TeV * (BR_t_to_blv_13p6TeV * BR_W_to_lv_13p6TeV) #pb
TbarWplusto2L2Nu_2022.year      = 2022
TbarWplusto2L2Nu_2022.dataset   = "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
TbarWplusto2L2Nu_2022.process   = 'TW_2022'
TbarWplusto2L2Nu_2022.EE        = 0

TW_2022                         = sample(ROOT.kViolet, 1, 1001, "tW", "TW_2022")
TW_2022.year                    = 2022
TW_2022.components              = [
                                    TWminustoLNu2Q_2022,
                                    TWminusto4Q_2022,
                                    TWminusto2L2Nu_2022,
                                    TbarWplustoLNu2Q_2022,
                                    TbarWplusto4Q_2022,
                                    TbarWplusto2L2Nu_2022
                                ]

################################ ZJets ################################

ZJetsToNuNu_HT100to200_2022             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT100to200_2022")
ZJetsToNuNu_HT100to200_2022.sigma       = 273.7 #pb
ZJetsToNuNu_HT100to200_2022.year        = 2022
ZJetsToNuNu_HT100to200_2022.dataset     = "/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT100to200_2022.process     = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT100to200_2022.unix_code   = 31200
ZJetsToNuNu_HT100to200_2022.EE          = 0

ZJetsToNuNu_HT200to400_2022             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT200to400_2022")
ZJetsToNuNu_HT200to400_2022.sigma       = 75.96 #pb
ZJetsToNuNu_HT200to400_2022.year        = 2022
ZJetsToNuNu_HT200to400_2022.dataset     = "/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT200to400_2022.process     = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT200to400_2022.unix_code   = 31201
ZJetsToNuNu_HT200to400_2022.EE          = 0

ZJetsToNuNu_HT400to800_2022             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT400to800_2022")
ZJetsToNuNu_HT400to800_2022.sigma       = 13.19 #pb
ZJetsToNuNu_HT400to800_2022.year        = 2022
ZJetsToNuNu_HT400to800_2022.dataset     = "/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT400to800_2022.process     = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT400to800_2022.unix_code   = 31202
ZJetsToNuNu_HT400to800_2022.EE          = 0

ZJetsToNuNu_HT800to1500_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT800to1500_2022")
ZJetsToNuNu_HT800to1500_2022.sigma      = 1.364 #pb
ZJetsToNuNu_HT800to1500_2022.year       = 2022
ZJetsToNuNu_HT800to1500_2022.dataset    = "/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT800to1500_2022.process    = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT800to1500_2022.unix_code  = 31203
ZJetsToNuNu_HT800to1500_2022.EE         = 0

ZJetsToNuNu_HT1500to2500_2022           = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT1500to2500_2022")
ZJetsToNuNu_HT1500to2500_2022.sigma     = 0.09865 #pb
ZJetsToNuNu_HT1500to2500_2022.year      = 2022
ZJetsToNuNu_HT1500to2500_2022.dataset   = "/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT1500to2500_2022.process   = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT1500to2500_2022.unix_code = 31204
ZJetsToNuNu_HT1500to2500_2022.EE        = 0

ZJetsToNuNu_HT2500_2022                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT2500_2022")
ZJetsToNuNu_HT2500_2022.sigma           = 0.006699 #pb
ZJetsToNuNu_HT2500_2022.year            = 2022
ZJetsToNuNu_HT2500_2022.dataset         = "/Zto2Nu-4Jets_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT2500_2022.process         = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT2500_2022.unix_code       = 31205
ZJetsToNuNu_HT2500_2022.EE              = 0

ZJetsToNuNu_2022                        = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2022")
ZJetsToNuNu_2022.year                   = 2022
ZJetsToNuNu_2022.components             = [
                                            ZJetsToNuNu_HT100to200_2022,
                                            ZJetsToNuNu_HT200to400_2022,
                                            ZJetsToNuNu_HT400to800_2022,
                                            ZJetsToNuNu_HT800to1500_2022,
                                            ZJetsToNuNu_HT1500to2500_2022,
                                            ZJetsToNuNu_HT2500_2022 
                                            ]

ZJetsToNuNu_2jets_PT40to100_1J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_1J_2022")
ZJetsToNuNu_2jets_PT40to100_1J_2022.sigma      = 929.8	
ZJetsToNuNu_2jets_PT40to100_1J_2022.year       = 2022
ZJetsToNuNu_2jets_PT40to100_1J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_1J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT40to100_1J_2022.unix_code  = 31206
ZJetsToNuNu_2jets_PT40to100_1J_2022.EE         = 0

ZJetsToNuNu_2jets_PT100to200_1J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_1J_2022")
ZJetsToNuNu_2jets_PT100to200_1J_2022.sigma      = 86.38
ZJetsToNuNu_2jets_PT100to200_1J_2022.year       = 2022
ZJetsToNuNu_2jets_PT100to200_1J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_1J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT100to200_1J_2022.unix_code  = 31207
ZJetsToNuNu_2jets_PT100to200_1J_2022.EE         = 0

ZJetsToNuNu_2jets_PT200to400_1J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_1J_2022")
ZJetsToNuNu_2jets_PT200to400_1J_2022.sigma      = 6.354	
ZJetsToNuNu_2jets_PT200to400_1J_2022.year       = 2022
ZJetsToNuNu_2jets_PT200to400_1J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_1J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT200to400_1J_2022.unix_code  = 31208
ZJetsToNuNu_2jets_PT200to400_1J_2022.EE         = 0

ZJetsToNuNu_2jets_PT400to600_1J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_1J_2022")
ZJetsToNuNu_2jets_PT400to600_1J_2022.sigma      = 0.2188
ZJetsToNuNu_2jets_PT400to600_1J_2022.year       = 2022
ZJetsToNuNu_2jets_PT400to600_1J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_1J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT400to600_1J_2022.unix_code  = 31209
ZJetsToNuNu_2jets_PT400to600_1J_2022.EE         = 0

ZJetsToNuNu_2jets_PT600_1J_2022                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_1J_2022")
ZJetsToNuNu_2jets_PT600_1J_2022.sigma           = 0.02583
ZJetsToNuNu_2jets_PT600_1J_2022.year            = 2022
ZJetsToNuNu_2jets_PT600_1J_2022.dataset         = "/Zto2Nu-2Jets_PTNuNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_1J_2022.process         = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT600_1J_2022.unix_code       = 31210
ZJetsToNuNu_2jets_PT600_1J_2022.EE              = 0

ZJetsToNuNu_2jets_PT40to100_2J_2022             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_2J_2022")
ZJetsToNuNu_2jets_PT40to100_2J_2022.sigma       = 335.5
ZJetsToNuNu_2jets_PT40to100_2J_2022.year        = 2022
ZJetsToNuNu_2jets_PT40to100_2J_2022.dataset     = "/Zto2Nu-2Jets_PTNuNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_2J_2022.process     = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT40to100_2J_2022.unix_code   = 31211
ZJetsToNuNu_2jets_PT40to100_2J_2022.EE          = 0

ZJetsToNuNu_2jets_PT100to200_2J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_2J_2022")
ZJetsToNuNu_2jets_PT100to200_2J_2022.sigma      = 100.4
ZJetsToNuNu_2jets_PT100to200_2J_2022.year       = 2022
ZJetsToNuNu_2jets_PT100to200_2J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_2J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT100to200_2J_2022.unix_code  = 31212
ZJetsToNuNu_2jets_PT100to200_2J_2022.EE         = 0

ZJetsToNuNu_2jets_PT200to400_2J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_2J_2022")
ZJetsToNuNu_2jets_PT200to400_2J_2022.sigma      = 13.86
ZJetsToNuNu_2jets_PT200to400_2J_2022.year       = 2022
ZJetsToNuNu_2jets_PT200to400_2J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_2J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT200to400_2J_2022.unix_code  = 31213
ZJetsToNuNu_2jets_PT200to400_2J_2022.EE         = 0

ZJetsToNuNu_2jets_PT400to600_2J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_2J_2022")
ZJetsToNuNu_2jets_PT400to600_2J_2022.sigma      = 0.7816
ZJetsToNuNu_2jets_PT400to600_2J_2022.year       = 2022
ZJetsToNuNu_2jets_PT400to600_2J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_2J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT400to600_2J_2022.unix_code  = 31214
ZJetsToNuNu_2jets_PT400to600_2J_2022.EE         = 0

ZJetsToNuNu_2jets_PT600_2J_2022                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_2J_2022")
ZJetsToNuNu_2jets_PT600_2J_2022.sigma           = 0.1311
ZJetsToNuNu_2jets_PT600_2J_2022.year            = 2022
ZJetsToNuNu_2jets_PT600_2J_2022.dataset         = "/Zto2Nu-2Jets_PTNuNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_2J_2022.process         = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT600_2J_2022.unix_code       = 31215
ZJetsToNuNu_2jets_PT600_2J_2022.EE              = 0

ZJetsToNuNu_2jets_2022 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_2022")
ZJetsToNuNu_2jets_2022.year = 2022
ZJetsToNuNu_2jets_2022.components = [
                                        ZJetsToNuNu_2jets_PT40to100_1J_2022,
                                        ZJetsToNuNu_2jets_PT100to200_1J_2022,
                                        ZJetsToNuNu_2jets_PT200to400_1J_2022,
                                        ZJetsToNuNu_2jets_PT400to600_1J_2022,
                                        ZJetsToNuNu_2jets_PT600_1J_2022,
                                        ZJetsToNuNu_2jets_PT40to100_2J_2022,
                                        ZJetsToNuNu_2jets_PT100to200_2J_2022,
                                        ZJetsToNuNu_2jets_PT200to400_2J_2022,
                                        ZJetsToNuNu_2jets_PT400to600_2J_2022,
                                        ZJetsToNuNu_2jets_PT600_2J_2022
                                    ]

################################ WJets ################################
WJets_HT120to200_2022               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT120to200_2022") 
WJets_HT120to200_2022.dataset       = "/WtoLNu-4Jets_MLNu-120to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT120to200_2022.sigma         = 167
WJets_HT120to200_2022.year          = 2022
WJets_HT120to200_2022.process       = "WJets_2022"
WJets_HT120to200_2022.unix_code     = 31300
WJets_HT120to200_2022.EE            = 0

WJets_HT200to400_2022               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT200to400_2022") 
WJets_HT200to400_2022.dataset       = "/WtoLNu-4Jets_MLNu-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT200to400_2022.sigma         = 20.3	
WJets_HT200to400_2022.year          = 2022
WJets_HT200to400_2022.process       = "WJets_2022"
WJets_HT200to400_2022.unix_code     = 31301
WJets_HT200to400_2022.EE            = 0

WJets_HT400to800_2022               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT400to800_2022") 
WJets_HT400to800_2022.dataset       = "/WtoLNu-4Jets_MLNu-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT400to800_2022.sigma         = 1.596
WJets_HT400to800_2022.year          = 2022
WJets_HT400to800_2022.process       = "WJets_2022"
WJets_HT400to800_2022.unix_code     = 31302
WJets_HT400to800_2022.EE            = 0

WJets_HT800to1500_2022              = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT800to1500_2022") 
WJets_HT800to1500_2022.dataset      = "/WtoLNu-4Jets_MLNu-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT800to1500_2022.sigma        = 0.1095	
WJets_HT800to1500_2022.year         = 2022
WJets_HT800to1500_2022.process      = "WJets_2022"
WJets_HT800to1500_2022.unix_code    = 31303
WJets_HT800to1500_2022.EE           = 0

WJets_HT1500to2500_2022             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT1500to2500_2022") 
WJets_HT1500to2500_2022.dataset     = "/WtoLNu-4Jets_MLNu-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT1500to2500_2022.sigma       = 0.006365
WJets_HT1500to2500_2022.year        = 2022
WJets_HT1500to2500_2022.process     = "WJets_2022"
WJets_HT1500to2500_2022.unix_code   = 31304
WJets_HT1500to2500_2022.EE          = 0

WJets_HT2500to4000_2022             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT2500to4000_2022") 
WJets_HT2500to4000_2022.dataset     = "/WtoLNu-4Jets_MLNu-2500to4000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT2500to4000_2022.sigma       = 0.0003463
WJets_HT2500to4000_2022.year        = 2022
WJets_HT2500to4000_2022.process     = "WJets_2022"
WJets_HT2500to4000_2022.unix_code   = 31305
WJets_HT2500to4000_2022.EE          = 0

WJets_HT4000to6000_2022             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT4000to6000_2022") 
WJets_HT4000to6000_2022.dataset     = "/WtoLNu-4Jets_MLNu-4000to6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT4000to6000_2022.sigma       = 0.00001075
WJets_HT4000to6000_2022.year        = 2022
WJets_HT4000to6000_2022.process     = "WJets_2022"
WJets_HT4000to6000_2022.unix_code   = 31306
WJets_HT4000to6000_2022.EE          = 0

WJets_HT6000_2022                   = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT6000_2022") 
WJets_HT6000_2022.dataset           = "/WtoLNu-4Jets_MLNu-6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT6000_2022.sigma             = 4.182e-7	
WJets_HT6000_2022.year              = 2022
WJets_HT6000_2022.process           = "WJets_2022"
WJets_HT6000_2022.unix_code         = 31307
WJets_HT6000_2022.EE                = 0

WJets_2022                  = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2022")
WJets_2022.year             = 2022
WJets_2022.components       = [WJets_HT120to200_2022, WJets_HT200to400_2022, WJets_HT400to800_2022, WJets_HT800to1500_2022, WJets_HT1500to2500_2022, WJets_HT2500to4000_2022, WJets_HT4000to6000_2022, WJets_HT6000_2022]

WJets_2jets0J_2022           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets0J_2022")
WJets_2jets0J_2022.dataset   = "/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM"
WJets_2jets0J_2022.sigma     = 55760 
WJets_2jets0J_2022.year      = 2022
WJets_2jets0J_2022.process   = "WJets_2jets_2022"
WJets_2jets0J_2022.unix_code = 31308
WJets_2jets0J_2022.EE        = 0

WJets_2jets1J_2022           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets1J_2022")
WJets_2jets1J_2022.dataset   = "/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
WJets_2jets1J_2022.sigma     = 9529 
WJets_2jets1J_2022.year      = 2022
WJets_2jets1J_2022.process   = "WJets_2jets_2022"
WJets_2jets1J_2022.unix_code = 31309
WJets_2jets1J_2022.EE        = 0

WJets_2jets2J_2022           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets2J_2022")
WJets_2jets2J_2022.dataset   = "/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
WJets_2jets2J_2022.sigma     = 3532 
WJets_2jets2J_2022.year      = 2022
WJets_2jets2J_2022.process   = "WJets_2jets_2022"
WJets_2jets2J_2022.unix_code = 31310
WJets_2jets2J_2022.EE        = 0

WJets_2jets_2022             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_2022")
WJets_2jets_2022.year        = 2022
WJets_2jets_2022.components  = [WJets_2jets0J_2022, WJets_2jets1J_2022, WJets_2jets2J_2022]

#######################################   t+DM   #######################################
tDM_mPhi50_mChi1_2022               = sample(ROOT.kGreen, 1, 1001, "DM (m_{#Phi}=50)", "tDM_mPhi50_mChi1_2022")
tDM_mPhi50_mChi1_2022.year          = 2022
tDM_mPhi50_mChi1_2022.sigma         = 0.07454  #pb
tDM_mPhi50_mChi1_2022.dataset       = '/tDM_Mchi1MPhi50_total/oiorio-tDM_Mchi1MPhi50Run3_NANOAOD_F-00000000000000000000000000000000/USER'
tDM_mPhi50_mChi1_2022.EE            = 0
tDM_mPhi50_mChi1_2022.unix_code     = 22102

tDM_mPhi200_mChi1_2022              = sample(ROOT.kGreen, 1, 1001, "DM (m_{#Phi}=200)", "tDM_mPhi200_mChi1_2022")
tDM_mPhi200_mChi1_2022.year         = 2022
tDM_mPhi200_mChi1_2022.sigma        = 0.07662  #pb
tDM_mPhi200_mChi1_2022.dataset      = '/tDM_Mchi1MPhi200_total/oiorio-tDM_Mchi1MPhi200Run3_NANOAOD_F-00000000000000000000000000000000/USER'
tDM_mPhi200_mChi1_2022.EE           = 0
tDM_mPhi200_mChi1_2022.unix_code    = 22102

tDM_mPhi500_mChi1_2022              = sample(ROOT.kGreen+2, 1, 1001, "DM (m_{#Phi}=1000)", "tDM_mPhi500_mChi1_2022")
tDM_mPhi500_mChi1_2022.sigma        = 0.004427 #pb
tDM_mPhi500_mChi1_2022.year         = 2022
tDM_mPhi500_mChi1_2022.dataset      = '/tDM_Mchi1MPhi500_total/oiorio-tDM_Mchi1MPhi500Run3_NANOAOD_F-00000000000000000000000000000000/USER'
tDM_mPhi500_mChi1_2022.EE           = 0
tDM_mPhi500_mChi1_2022.unix_code    = 22101

tDM_mPhi1000_mChi1_2022             = sample(ROOT.kGreen+2, 1, 1001, "DM (m_{#Phi}=1000)", "tDM_mPhi1000_mChi1_2022")
tDM_mPhi1000_mChi1_2022.sigma       = 0.0002494 #pb
tDM_mPhi1000_mChi1_2022.year        = 2022
tDM_mPhi1000_mChi1_2022.dataset     = '/tDM_Mchi1MPhi1000_total/oiorio-tDM_Mchi1MPhi1000Run3_NANOAOD_F-00000000000000000000000000000000/USER'
tDM_mPhi1000_mChi1_2022.EE          = 0
tDM_mPhi1000_mChi1_2022.unix_code   = 22100

#######################################   tt+DM   #######################################
ttDM_mPhi50_mChi1_2022              = sample(ROOT.kGreen, 1, 1001, "DM (m_{#Phi}=50)", "ttDM_mPhi50_mChi1_2022")
ttDM_mPhi50_mChi1_2022.year         = 2022
ttDM_mPhi50_mChi1_2022.sigma        = 3.0655 #pb
ttDM_mPhi50_mChi1_2022.dataset      = '/ttDM_Mchi1MPhi50_total/oiorio-ttDM_Mchi1MPhi50Run3_NANOAOD_F-00000000000000000000000000000000/USER'
ttDM_mPhi50_mChi1_2022.EE           = 0
ttDM_mPhi50_mChi1_2022.unix_code    = 22106

ttDM_mPhi200_mChi1_2022             = sample(ROOT.kGreen, 1, 1001, "DM (m_{#Phi}=200)", "ttDM_mPhi200_mChi1_2022")
ttDM_mPhi200_mChi1_2022.year        = 2022
ttDM_mPhi200_mChi1_2022.sigma       = 0.10425  #pb
ttDM_mPhi200_mChi1_2022.dataset     = '/ttDM_Mchi1MPhi200_total/oiorio-ttDM_Mchi1MPhi200Run3_NANOAOD_F-00000000000000000000000000000000/USER'
ttDM_mPhi200_mChi1_2022.EE          = 0
ttDM_mPhi200_mChi1_2022.unix_code   = 22105

ttDM_mPhi500_mChi1_2022             = sample(ROOT.kGreen+2, 1, 1001, "DM (m_{#Phi}=500)", "ttDM_mPhi500_mChi1_2022")
ttDM_mPhi500_mChi1_2022.sigma       = 0.005585 #pb
ttDM_mPhi500_mChi1_2022.year        = 2022
ttDM_mPhi500_mChi1_2022.dataset     = '/ttDM_Mchi1MPhi1000_total/oiorio-ttDM_Mchi1MPhi1000Run3_NANOAOD_F-00000000000000000000000000000000/USER'
ttDM_mPhi500_mChi1_2022.EE          = 0
ttDM_mPhi500_mChi1_2022.unix_code   = 22104

ttDM_mPhi1000_mChi1_2022            = sample(ROOT.kGreen+2, 1, 1001, "DM (m_{#Phi}=1000)", "ttDM_mPhi1000_mChi1_2022")
ttDM_mPhi1000_mChi1_2022.sigma      = 0.00065 #pb
ttDM_mPhi1000_mChi1_2022.year       = 2022
ttDM_mPhi1000_mChi1_2022.dataset    = '/ttDM_Mchi1MPhi1000_total/oiorio-ttDM_Mchi1MPhi1000Run3_NANOAOD_F-00000000000000000000000000000000/USER'
ttDM_mPhi1000_mChi1_2022.EE         = 0
ttDM_mPhi1000_mChi1_2022.unix_code  = 22103



###############################################################################################################################
##########################################                                           ##########################################
##########################################       samples for tagger studies          ##########################################
##########################################                                           ##########################################
###############################################################################################################################
Zprime4top_500_2022          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M500GeV", "Zprime4top_500_2022")
Zprime4top_500_2022.sigma    = 1 #pb
Zprime4top_500_2022.year     = 2022
Zprime4top_500_2022.dataset  = '/TopPhilic_ttzp_13p6TeV_m500_relwidth4_TuneCP5_13p6TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-500_Width4_nanoaod_hotvr_UL2022v1_230510-00000000000000000000000000000000/USER'
Zprime4top_500_2022.EE       = 0

Zprime4top_1000_2022          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M1000GeV", "Zprime4top_1000_2022")
Zprime4top_1000_2022.sigma    = 1 #pb
Zprime4top_1000_2022.year     = 2022
Zprime4top_1000_2022.dataset  = '/TopPhilic_ttzp_13p6TeV_m1000_relwidth4_TuneCP5_13p6TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-1000_Width4_nanoaod_hotvr_UL2022v1_230510-00000000000000000000000000000000/USER'
Zprime4top_1000_2022.EE       = 0

Zprime4top_2000_2022          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M2000GeV", "Zprime4top_2000_2022")
Zprime4top_2000_2022.sigma    = 1 #pb
Zprime4top_2000_2022.year     = 2022
Zprime4top_2000_2022.dataset  = '/TopPhilic_ttzp_13p6TeV_m2000_relwidth4_TuneCP5_13p6TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-2000_Width4_nanoaod_hotvr_UL2022v1_230510-00000000000000000000000000000000/USER'
Zprime4top_2000_2022.EE       = 0


###############################################################################################################################
##########################################                                           ##########################################
##########################################                   2022EE                  ##########################################
##########################################                                           ##########################################
###############################################################################################################################
# Era EFG del 2022 hanno avuto un proble water leak (controlla bene?) per cui vanno sotto una tag diversa 
# rispetto a era CD, per questo finora abbiamo usato la tag Run3Summer22 e da qui rifacciamo i sample con
# 2022EE --> Run3Summer22EE, ci sono correzioni diverse per i due pezzi quindi invece di cambiare l'anno
# aggiungerò un .EE che sarà True solo per i 2022EE, False per i 2022 e per gli altri anni non definito
# NB per i dati le ere hanno tutti year 2022 perché il golden JSON è lo stesso per tutti
################################ QCD ################################
# QCD_HT40to70_2022EE               = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT40to70_2022EE")
# QCD_HT40to70_2022EE.sigma         = 311400000 #pb
# QCD_HT40to70_2022EE.year          = 2022
# QCD_HT40to70_2022EE.dataset       = # NO DATASET
# QCD_HT40to70_2022EE.process       = "QCD_2022EE"
# QCD_HT40to70_2022EE.unix_code     = 41000
# QCD_HT40to70_2022EE.EE            = 1
QCD_HT70to100_2022EE              = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT70to100_2022EE")
QCD_HT70to100_2022EE.sigma        = 58500000 #pb 3.117e+08
QCD_HT70to100_2022EE.year         = 2022
QCD_HT70to100_2022EE.dataset      = "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT70to100_2022EE.process      = "QCD_2022EE"
QCD_HT70to100_2022EE.unix_code    = 41001
QCD_HT70to100_2022EE.EE           = 1

QCD_HT100to200_2022EE             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT100to200_2022EE")
QCD_HT100to200_2022EE.sigma       = 25400000 #pb
QCD_HT100to200_2022EE.year        = 2022
QCD_HT100to200_2022EE.dataset     = "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT100to200_2022EE.process     = "QCD_2022EE"
QCD_HT100to200_2022EE.unix_code   = 41002
QCD_HT100to200_2022EE.EE          = 1

QCD_HT200to400_2022EE             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT200to400_2022EE")
QCD_HT200to400_2022EE.sigma       = 1961000 #pb
QCD_HT200to400_2022EE.year        = 2022
QCD_HT200to400_2022EE.dataset     = "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT200to400_2022EE.process     = "QCD_2022EE"
QCD_HT200to400_2022EE.unix_code   = 41003
QCD_HT200to400_2022EE.EE          = 1

QCD_HT400to600_2022EE             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT400to600_2022EE")
QCD_HT400to600_2022EE.sigma       = 95620 #pb
QCD_HT400to600_2022EE.year        = 2022
QCD_HT400to600_2022EE.dataset     = "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT400to600_2022EE.process     = "QCD_2022EE"
QCD_HT400to600_2022EE.unix_code   = 41004
QCD_HT400to600_2022EE.EE          = 1

QCD_HT600to800_2022EE             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT600to800_2022EE")
QCD_HT600to800_2022EE.sigma       = 13540 #pb
QCD_HT600to800_2022EE.year        = 2022
QCD_HT600to800_2022EE.dataset     = "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT600to800_2022EE.process     = "QCD_2022EE"
QCD_HT600to800_2022EE.unix_code   = 41005
QCD_HT600to800_2022EE.EE          = 1

QCD_HT800to1000_2022EE            = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT800to1000_2022EE")
QCD_HT800to1000_2022EE.sigma      = 3033 #pb
QCD_HT800to1000_2022EE.year       = 2022
QCD_HT800to1000_2022EE.dataset    = "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT800to1000_2022EE.process    = "QCD_2022EE"
QCD_HT800to1000_2022EE.unix_code  = 41006
QCD_HT800to1000_2022EE.EE         = 1

QCD_HT1000to1200_2022EE           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1000to1200_2022EE")
QCD_HT1000to1200_2022EE.sigma     = 883.7 #pb
QCD_HT1000to1200_2022EE.year      = 2022
QCD_HT1000to1200_2022EE.dataset   = "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT1000to1200_2022EE.process   = "QCD_2022EE"
QCD_HT1000to1200_2022EE.unix_code = 41007
QCD_HT1000to1200_2022EE.EE        = 1

QCD_HT1200to1500_2022EE           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1200to1500_2022EE")
QCD_HT1200to1500_2022EE.sigma     = 383.5 #pb
QCD_HT1200to1500_2022EE.year      = 2022
QCD_HT1200to1500_2022EE.dataset   = "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT1200to1500_2022EE.process   = "QCD_2022EE"
QCD_HT1200to1500_2022EE.unix_code = 41007
QCD_HT1200to1500_2022EE.EE        = 1

QCD_HT1500to2000_2022EE           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1500to2000_2022EE")
QCD_HT1500to2000_2022EE.sigma     = 125.2 #pb
QCD_HT1500to2000_2022EE.year      = 2022
QCD_HT1500to2000_2022EE.dataset   = "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT1500to2000_2022EE.process   = "QCD_2022EE"
QCD_HT1500to2000_2022EE.unix_code = 41008
QCD_HT1500to2000_2022EE.EE        = 1

QCD_HT2000_2022EE                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT2000_2022EE")
QCD_HT2000_2022EE.sigma           = 26.49 #pb
QCD_HT2000_2022EE.year            = 2022
QCD_HT2000_2022EE.dataset         = "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT2000_2022EE.process         = "QCD_2022EE"
QCD_HT2000_2022EE.unix_code       = 41009
QCD_HT2000_2022EE.EE              = 1

QCD_2022EE                        = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2022EE")
QCD_2022EE.year                   = 2022
QCD_2022EE.components             = [ 
                                    # QCD_HT40to70_2022EE, 
                                    QCD_HT70to100_2022EE, QCD_HT100to200_2022EE, QCD_HT200to400_2022EE,
                                    QCD_HT400to600_2022EE, QCD_HT600to800_2022EE, QCD_HT800to1000_2022EE, 
                                    QCD_HT1000to1200_2022EE,QCD_HT1200to1500_2022EE,
                                    QCD_HT1500to2000_2022EE, QCD_HT2000_2022EE
                                ]


# /QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-JMENano12p5_132X_mcRun3_2022_realistic_postEE_v4-v2/NANOAODSIM


################################ TTbar ################################
TT_semilep_2022EE             = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2022EE")
TT_semilep_2022EE.sigma       = sigma_ttbar_13p6TeV * BR_t_to_bqq_13p6TeV * BR_t_to_blv_13p6TeV * 2 #pb 
TT_semilep_2022EE.year        = 2022
TT_semilep_2022EE.dataset     = "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"
TT_semilep_2022EE.process     = 'TT_2022EE'
TT_semilep_2022EE.unix_code   = 41100
TT_semilep_2022EE.EE          = 1

TT_hadr_2022EE                = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_hadr_2022EE")
TT_hadr_2022EE.sigma          = sigma_ttbar_13p6TeV * BR_t_to_bqq_13p6TeV * BR_t_to_bqq_13p6TeV
TT_hadr_2022EE.year           = 2022
TT_hadr_2022EE.dataset        = "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"
TT_hadr_2022EE.process        = 'TT_2022EE'
TT_hadr_2022EE.unix_code      = 41101
TT_hadr_2022EE.EE             = 1

TT_dilep_2022EE               = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_dilep_2022EE")
TT_dilep_2022EE.sigma         = sigma_ttbar_13p6TeV * BR_t_to_blv_13p6TeV * BR_t_to_blv_13p6TeV
TT_dilep_2022EE.year          = 2022
TT_dilep_2022EE.dataset       = "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"
TT_dilep_2022EE.process       = 'TT_2022EE'
TT_dilep_2022EE.unix_code     = 41102
TT_dilep_2022EE.EE            = 1

TT_2022EE                     = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_2022EE")
TT_2022EE.year                = 2022
TT_2022EE.components          = [
                                    TT_semilep_2022EE,
                                    TT_hadr_2022EE,
                                    TT_dilep_2022EE
                                    ]

################################ SingleTop ################################
TWminustoLNu2Q_2022EE             = sample(ROOT.kViolet, 1, 1001, "tW", "TWminustoLNu2Q_2022EE")
TWminustoLNu2Q_2022EE.sigma       = sigma_tWminus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_lv_13p6TeV + BR_t_to_blv_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TWminustoLNu2Q_2022EE.year        = 2022
TWminustoLNu2Q_2022EE.dataset     = "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
TWminustoLNu2Q_2022EE.process     = 'TW_2022EE'
TWminustoLNu2Q_2022EE.EE          = 1

TWminusto4Q_2022EE                = sample(ROOT.kViolet, 1, 1001, "tW", "TWminusto4Q_2022EE")
TWminusto4Q_2022EE.sigma          = sigma_tWminus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TWminusto4Q_2022EE.year           = 2022
TWminusto4Q_2022EE.dataset        = "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
TWminusto4Q_2022EE.process        = 'TW_2022EE'
TWminusto4Q_2022EE.EE             = 1

TWminusto2L2Nu_2022EE             = sample(ROOT.kViolet, 1, 1001, "tW", "TWminusto2L2Nu_2022EE")
TWminusto2L2Nu_2022EE.sigma       = sigma_tWminus_13p6TeV * (BR_t_to_blv_13p6TeV * BR_W_to_lv_13p6TeV) #pb
TWminusto2L2Nu_2022EE.year        = 2022
TWminusto2L2Nu_2022EE.dataset     = "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
TWminusto2L2Nu_2022EE.process     = 'TW_2022EE'
TWminusto2L2Nu_2022EE.EE          = 1

TbarWplustoLNu2Q_2022EE           = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplustoLNu2Q_2022EE")
TbarWplustoLNu2Q_2022EE.sigma     = sigma_tbarWplus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_lv_13p6TeV + BR_t_to_blv_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TbarWplustoLNu2Q_2022EE.year      = 2022
TbarWplustoLNu2Q_2022EE.dataset   = "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
TbarWplustoLNu2Q_2022EE.process   = 'TW_2022EE'
TbarWplustoLNu2Q_2022EE.EE        = 1

TbarWplusto4Q_2022EE              = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplusto4Q_2022EE")
TbarWplusto4Q_2022EE.sigma        = sigma_tbarWplus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TbarWplusto4Q_2022EE.year         = 2022
TbarWplusto4Q_2022EE.dataset      = "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
TbarWplusto4Q_2022EE.process      = 'TW_2022EE'
TbarWplusto4Q_2022EE.EE           = 1

TbarWplusto2L2Nu_2022EE           = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplusto2L2Nu_2022EE")
TbarWplusto2L2Nu_2022EE.sigma     = sigma_tbarWplus_13p6TeV * (BR_t_to_blv_13p6TeV * BR_W_to_lv_13p6TeV) #pb
TbarWplusto2L2Nu_2022EE.year      = 2022
TbarWplusto2L2Nu_2022EE.dataset   = "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
TbarWplusto2L2Nu_2022EE.process   = 'TW_2022EE'
TbarWplusto2L2Nu_2022EE.EE        = 1

TW_2022EE                         = sample(ROOT.kViolet, 1, 1001, "tW", "TW_2022EE")
TW_2022EE.year                    = 2022
TW_2022EE.components              = [
                                        TWminustoLNu2Q_2022EE,
                                        TWminusto4Q_2022EE,
                                        TWminusto2L2Nu_2022EE,
                                        TbarWplustoLNu2Q_2022EE,
                                        TbarWplusto4Q_2022EE,
                                        TbarWplusto2L2Nu_2022EE
                                    ]

################################ ZJets ################################

ZJetsToNuNu_HT100to200_2022EE             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT100to200_2022EE")
ZJetsToNuNu_HT100to200_2022EE.sigma       = 273.6 #pb
ZJetsToNuNu_HT100to200_2022EE.year        = 2022
ZJetsToNuNu_HT100to200_2022EE.dataset     = "/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
ZJetsToNuNu_HT100to200_2022EE.process     = 'ZJetsToNuNu_2022EE'
ZJetsToNuNu_HT100to200_2022EE.unix_code   = 41200
ZJetsToNuNu_HT100to200_2022EE.EE          = 1

ZJetsToNuNu_HT200to400_2022EE             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT200to400_2022EE")
ZJetsToNuNu_HT200to400_2022EE.sigma       = 76.14 #pb
ZJetsToNuNu_HT200to400_2022EE.year        = 2022
ZJetsToNuNu_HT200to400_2022EE.dataset     = "/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
ZJetsToNuNu_HT200to400_2022EE.process     = 'ZJetsToNuNu_2022EE'
ZJetsToNuNu_HT200to400_2022EE.unix_code   = 41201
ZJetsToNuNu_HT200to400_2022EE.EE          = 1

ZJetsToNuNu_HT400to800_2022EE             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT400to800_2022EE")
ZJetsToNuNu_HT400to800_2022EE.sigma       = 13.18 #pb
ZJetsToNuNu_HT400to800_2022EE.year        = 2022
ZJetsToNuNu_HT400to800_2022EE.dataset     = "/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
ZJetsToNuNu_HT400to800_2022EE.process     = 'ZJetsToNuNu_2022EE'
ZJetsToNuNu_HT400to800_2022EE.unix_code   = 41202
ZJetsToNuNu_HT400to800_2022EE.EE          = 1

ZJetsToNuNu_HT800to1500_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT800to1500_2022EE")
ZJetsToNuNu_HT800to1500_2022EE.sigma      = 1.366 #pb
ZJetsToNuNu_HT800to1500_2022EE.year       = 2022
ZJetsToNuNu_HT800to1500_2022EE.dataset    = "/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM"
ZJetsToNuNu_HT800to1500_2022EE.process    = 'ZJetsToNuNu_2022EE'
ZJetsToNuNu_HT800to1500_2022EE.unix_code  = 41203
ZJetsToNuNu_HT800to1500_2022EE.EE         = 1

ZJetsToNuNu_HT1500to2500_2022EE           = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT1500to2500_2022EE")
ZJetsToNuNu_HT1500to2500_2022EE.sigma     = 0.09852 #pb
ZJetsToNuNu_HT1500to2500_2022EE.year      = 2022
ZJetsToNuNu_HT1500to2500_2022EE.dataset   = "/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
ZJetsToNuNu_HT1500to2500_2022EE.process   = 'ZJetsToNuNu_2022EE'
ZJetsToNuNu_HT1500to2500_2022EE.unix_code = 41204
ZJetsToNuNu_HT1500to2500_2022EE.EE        = 1

ZJetsToNuNu_HT2500_2022EE                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT2500_2022EE")
ZJetsToNuNu_HT2500_2022EE.sigma           = 0.006699 #pb
ZJetsToNuNu_HT2500_2022EE.year            = 2022
ZJetsToNuNu_HT2500_2022EE.dataset         = "/Zto2Nu-4Jets_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
ZJetsToNuNu_HT2500_2022EE.process         = 'ZJetsToNuNu_2022EE'
ZJetsToNuNu_HT2500_2022EE.unix_code       = 41205
ZJetsToNuNu_HT2500_2022EE.EE              = 1

ZJetsToNuNu_2022EE                        = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2022EE")
ZJetsToNuNu_2022EE.year                   = 2022
ZJetsToNuNu_2022EE.components             = [
                                            ZJetsToNuNu_HT100to200_2022EE, ZJetsToNuNu_HT200to400_2022EE, ZJetsToNuNu_HT400to800_2022EE,
                                            ZJetsToNuNu_HT800to1500_2022EE, ZJetsToNuNu_HT1500to2500_2022EE, ZJetsToNuNu_HT2500_2022EE 
                                            ]

ZJetsToNuNu_2jets_PT40to100_1J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_1J_2022EE")
ZJetsToNuNu_2jets_PT40to100_1J_2022EE.sigma      = 929.8	
ZJetsToNuNu_2jets_PT40to100_1J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT40to100_1J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_1J_2022EE.process    = 'ZJetsToNuNu_2jets_2022EE'
ZJetsToNuNu_2jets_PT40to100_1J_2022EE.unix_code  = 41207
ZJetsToNuNu_2jets_PT40to100_1J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT100to200_1J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_1J_2022EE")
ZJetsToNuNu_2jets_PT100to200_1J_2022EE.sigma      = 86.38
ZJetsToNuNu_2jets_PT100to200_1J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT100to200_1J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_1J_2022EE.process    = 'ZJetsToNuNu_2jets_2022EE'
ZJetsToNuNu_2jets_PT100to200_1J_2022EE.unix_code  = 41208
ZJetsToNuNu_2jets_PT100to200_1J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT200to400_1J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_1J_2022EE")
ZJetsToNuNu_2jets_PT200to400_1J_2022EE.sigma      = 6.354	
ZJetsToNuNu_2jets_PT200to400_1J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT200to400_1J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_1J_2022EE.process    = 'ZJetsToNuNu_2jets_2022EE'
ZJetsToNuNu_2jets_PT200to400_1J_2022EE.unix_code  = 41209
ZJetsToNuNu_2jets_PT200to400_1J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT400to600_1J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_1J_2022EE")
ZJetsToNuNu_2jets_PT400to600_1J_2022EE.sigma      = 0.2188
ZJetsToNuNu_2jets_PT400to600_1J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT400to600_1J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_1J_2022EE.process    = 'ZJetsToNuNu_2jets_2022EE'
ZJetsToNuNu_2jets_PT400to600_1J_2022EE.unix_code  = 41210
ZJetsToNuNu_2jets_PT400to600_1J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT600_1J_2022EE                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_1J_2022EE")
ZJetsToNuNu_2jets_PT600_1J_2022EE.sigma           = 0.02583
ZJetsToNuNu_2jets_PT600_1J_2022EE.year            = 2022
ZJetsToNuNu_2jets_PT600_1J_2022EE.dataset         = "/Zto2Nu-2Jets_PTNuNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_1J_2022EE.process         = 'ZJetsToNuNu_2jets_2022EE'
ZJetsToNuNu_2jets_PT600_1J_2022EE.unix_code       = 41211
ZJetsToNuNu_2jets_PT600_1J_2022EE.EE              = 1

ZJetsToNuNu_2jets_PT40to100_2J_2022EE             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_2J_2022EE")
ZJetsToNuNu_2jets_PT40to100_2J_2022EE.sigma       = 335.5
ZJetsToNuNu_2jets_PT40to100_2J_2022EE.year        = 2022
ZJetsToNuNu_2jets_PT40to100_2J_2022EE.dataset     = "/Zto2Nu-2Jets_PTNuNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_2J_2022EE.process     = 'ZJetsToNuNu_2jets_2022EE'
ZJetsToNuNu_2jets_PT40to100_2J_2022EE.unix_code   = 41212
ZJetsToNuNu_2jets_PT40to100_2J_2022EE.EE          = 1

ZJetsToNuNu_2jets_PT100to200_2J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_2J_2022EE")
ZJetsToNuNu_2jets_PT100to200_2J_2022EE.sigma      = 100.4
ZJetsToNuNu_2jets_PT100to200_2J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT100to200_2J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_2J_2022EE.process    = 'ZJetsToNuNu_2jets_2022EE'
ZJetsToNuNu_2jets_PT100to200_2J_2022EE.unix_code  = 41213
ZJetsToNuNu_2jets_PT100to200_2J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT200to400_2J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_2J_2022EE")
ZJetsToNuNu_2jets_PT200to400_2J_2022EE.sigma      = 13.86
ZJetsToNuNu_2jets_PT200to400_2J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT200to400_2J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_2J_2022EE.process    = 'ZJetsToNuNu_2jets_2022EE'
ZJetsToNuNu_2jets_PT200to400_2J_2022EE.unix_code  = 41214
ZJetsToNuNu_2jets_PT200to400_2J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT400to600_2J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_2J_2022EE")
ZJetsToNuNu_2jets_PT400to600_2J_2022EE.sigma      = 0.7816
ZJetsToNuNu_2jets_PT400to600_2J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT400to600_2J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_2J_2022EE.process    = 'ZJetsToNuNu_2jets_2022EE'
ZJetsToNuNu_2jets_PT400to600_2J_2022EE.unix_code  = 41215
ZJetsToNuNu_2jets_PT400to600_2J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT600_2J_2022EE                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_2J_2022EE")
ZJetsToNuNu_2jets_PT600_2J_2022EE.sigma           = 0.1311
ZJetsToNuNu_2jets_PT600_2J_2022EE.year            = 2022
ZJetsToNuNu_2jets_PT600_2J_2022EE.dataset         = "/Zto2Nu-2Jets_PTNuNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_2J_2022EE.process         = 'ZJetsToNuNu_2jets_2022EE'
ZJetsToNuNu_2jets_PT600_2J_2022EE.unix_code       = 41216
ZJetsToNuNu_2jets_PT600_2J_2022EE.EE              = 1

ZJetsToNuNu_2jets_2022EE = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_2022EE")
ZJetsToNuNu_2jets_2022EE.year = 2022
ZJetsToNuNu_2jets_2022EE.components = [
                                        ZJetsToNuNu_2jets_PT40to100_1J_2022EE,
                                        ZJetsToNuNu_2jets_PT100to200_1J_2022EE,
                                        ZJetsToNuNu_2jets_PT200to400_1J_2022EE,
                                        ZJetsToNuNu_2jets_PT400to600_1J_2022EE,
                                        ZJetsToNuNu_2jets_PT600_1J_2022EE,
                                        ZJetsToNuNu_2jets_PT40to100_2J_2022EE,
                                        ZJetsToNuNu_2jets_PT100to200_2J_2022EE,
                                        ZJetsToNuNu_2jets_PT200to400_2J_2022EE,
                                        ZJetsToNuNu_2jets_PT400to600_2J_2022EE,
                                        ZJetsToNuNu_2jets_PT600_2J_2022EE
                                    ]
################################ WJets ################################

WJets_HT120to200_2022EE               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT120to200_2022EE") 
WJets_HT120to200_2022EE.dataset       = "/WtoLNu-4Jets_MLNu-120to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT120to200_2022EE.sigma         = 167
WJets_HT120to200_2022EE.year          = 2022
WJets_HT120to200_2022EE.process       = "WJets_2022"
WJets_HT120to200_2022EE.unix_code     = 41300
WJets_HT120to200_2022EE.EE            = 1

WJets_HT200to400_2022EE               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT200to400_2022EE") 
WJets_HT200to400_2022EE.dataset       = "/WtoLNu-4Jets_MLNu-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT200to400_2022EE.sigma         = 20.3
WJets_HT200to400_2022EE.year          = 2022
WJets_HT200to400_2022EE.process       = "WJets_2022"
WJets_HT200to400_2022EE.unix_code     = 41301
WJets_HT200to400_2022EE.EE            = 1

WJets_HT400to800_2022EE               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT400to800_2022EE") 
WJets_HT400to800_2022EE.dataset       = "/WtoLNu-4Jets_MLNu-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT400to800_2022EE.sigma         = 1.596	
WJets_HT400to800_2022EE.year          = 2022
WJets_HT400to800_2022EE.process       = "WJets_2022"
WJets_HT400to800_2022EE.unix_code     = 41302
WJets_HT400to800_2022EE.EE            = 1

WJets_HT800to1500_2022EE              = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT800to1500_2022EE") 
WJets_HT800to1500_2022EE.dataset      = "/WtoLNu-4Jets_MLNu-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT800to1500_2022EE.sigma        = 0.1095
WJets_HT800to1500_2022EE.year         = 2022
WJets_HT800to1500_2022EE.process      = "WJets_2022"
WJets_HT800to1500_2022EE.unix_code    = 41303
WJets_HT800to1500_2022EE.EE           = 1

WJets_HT1500to2500_2022EE             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT1500to2500_2022EE") 
WJets_HT1500to2500_2022EE.dataset     = "/WtoLNu-4Jets_MLNu-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM"
WJets_HT1500to2500_2022EE.sigma       = 0.006365
WJets_HT1500to2500_2022EE.year        = 2022
WJets_HT1500to2500_2022EE.process     = "WJets_2022"
WJets_HT1500to2500_2022EE.unix_code   = 41304
WJets_HT1500to2500_2022EE.EE          = 1

WJets_HT2500to4000_2022EE             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT2500to4000_2022EE") 
WJets_HT2500to4000_2022EE.dataset     = "/WtoLNu-4Jets_MLNu-2500to4000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT2500to4000_2022EE.sigma       = 0.0003463
WJets_HT2500to4000_2022EE.year        = 2022
WJets_HT2500to4000_2022EE.process     = "WJets_2022"
WJets_HT2500to4000_2022EE.unix_code   = 41305
WJets_HT2500to4000_2022EE.EE          = 1

WJets_HT4000to6000_2022EE             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT4000to6000_2022EE") 
WJets_HT4000to6000_2022EE.dataset     = "/WtoLNu-4Jets_MLNu-4000to6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT4000to6000_2022EE.sigma       = 0.00001075
WJets_HT4000to6000_2022EE.year        = 2022
WJets_HT4000to6000_2022EE.process     = "WJets_2022"
WJets_HT4000to6000_2022EE.unix_code   = 41306
WJets_HT4000to6000_2022EE.EE          = 1

WJets_HT6000_2022EE                   = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT6000_2022EE") 
WJets_HT6000_2022EE.dataset           = "/WtoLNu-4Jets_MLNu-6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT6000_2022EE.sigma             = 4.182e-7
WJets_HT6000_2022EE.year              = 2022
WJets_HT6000_2022EE.process           = "WJets_2022"
WJets_HT6000_2022EE.unix_code         = 41307
WJets_HT6000_2022EE.EE                = 1

WJets_2022EE                  = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2022EE")
WJets_2022EE.year             = 2022
WJets_2022EE.components       = [WJets_HT120to200_2022EE, WJets_HT200to400_2022EE, WJets_HT400to800_2022EE, WJets_HT800to1500_2022EE, WJets_HT1500to2500_2022EE, WJets_HT2500to4000_2022EE, WJets_HT4000to6000_2022EE, WJets_HT6000_2022EE]


WJets_2jets0J_2022EE           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets0J_2022EE")
WJets_2jets0J_2022EE.dataset   = "/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM"
WJets_2jets0J_2022EE.sigma     = 55760
WJets_2jets0J_2022EE.year      = 2022
WJets_2jets0J_2022EE.process   = "WJets_2jets_2022EE"
WJets_2jets0J_2022EE.unix_code = 41308
WJets_2jets0J_2022EE.EE        = 1

WJets_2jets1J_2022EE           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets1J_2022EE")
WJets_2jets1J_2022EE.dataset   = "/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
WJets_2jets1J_2022EE.sigma     = 9529
WJets_2jets1J_2022EE.year      = 2022
WJets_2jets1J_2022EE.process   = "WJets_2jets_2022EE"
WJets_2jets1J_2022EE.unix_code = 41309
WJets_2jets1J_2022EE.EE        = 1

WJets_2jets2J_2022EE           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets2J_2022EE")
WJets_2jets2J_2022EE.dataset   = "/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
WJets_2jets2J_2022EE.sigma     = 3532
WJets_2jets2J_2022EE.year      = 2022
WJets_2jets2J_2022EE.process   = "WJets_2jets_2022EE"
WJets_2jets2J_2022EE.unix_code = 41310
WJets_2jets2J_2022EE.EE        = 1

WJets_2jets_2022EE             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_2022EE")
WJets_2jets_2022EE.year        = 2022
WJets_2jets_2022EE.components  = [WJets_2jets0J_2022EE, WJets_2jets1J_2022EE, WJets_2jets2J_2022EE]

###############################################################################################################################
##########################################                                           ##########################################
##########################################       samples for tagger studies          ##########################################
##########################################                                           ##########################################
###############################################################################################################################
Zprime4top_500_2022EE          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M500GeV", "Zprime4top_500_2022EE")
Zprime4top_500_2022EE.sigma    = 1 #pb
Zprime4top_500_2022EE.year     = 2022
Zprime4top_500_2022EE.dataset  = '/TopPhilic_ttzp_13p6TeV_m500_relwidth4_TuneCP5_13p6TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-500_Width4_nanoaod_hotvr_UL2022_EEv1_230510-00000000000000000000000000000000/USER'
Zprime4top_500_2022EE.EE       = 1

Zprime4top_1000_2022EE          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M1000GeV", "Zprime4top_1000_2022EE")
Zprime4top_1000_2022EE.sigma    = 1 #pb
Zprime4top_1000_2022EE.year     = 2022
Zprime4top_1000_2022EE.dataset  = '/TopPhilic_ttzp_13p6TeV_m1000_relwidth4_TuneCP5_13p6TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-1000_Width4_nanoaod_hotvr_UL2022_EEv1_230510-00000000000000000000000000000000/USER'
Zprime4top_1000_2022EE.EE       = 1

Zprime4top_2000_2022EE          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M2000GeV", "Zprime4top_2000_2022EE")
Zprime4top_2000_2022EE.sigma    = 1 #pb
Zprime4top_2000_2022EE.year     = 2022
Zprime4top_2000_2022EE.dataset  = '/TopPhilic_ttzp_13p6TeV_m2000_relwidth4_TuneCP5_13p6TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-2000_Width4_nanoaod_hotvr_UL2022_EEv1_230510-00000000000000000000000000000000/USER'
Zprime4top_2000_2022EE.EE       = 1


###############################################################################################################################
##########################################                                           ##########################################
##########################################                    2023                   ##########################################
##########################################                                           ##########################################
###############################################################################################################################
# Per ora l'attributo EE viene usato anche per pre e post BPix, quindi se EE=0 è preBPix, se EE=1 è postBPix
# 
# 
# 
#
################################ QCD ################################
# QCD_HT40to70_2023               = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT40to70_2023")
# QCD_HT40to70_2023.sigma         = 311400000 #pb
# QCD_HT40to70_2023.year          = 2023
# QCD_HT40to70_2023.dataset       = "/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
# QCD_HT40to70_2023.process       = "QCD_2023"
# QCD_HT40to70_2023.unix_code     = 31000
# QCD_HT40to70_2023.EE            = 0
QCD_HT70to100_2023              = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT70to100_2023")
QCD_HT70to100_2023.sigma        = 58500000 #pb
QCD_HT70to100_2023.year         = 2023
QCD_HT70to100_2023.dataset      = "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
QCD_HT70to100_2023.process      = "QCD_2023"
QCD_HT70to100_2023.unix_code    = 31001
QCD_HT70to100_2023.EE           = 0
QCD_HT100to200_2023             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT100to200_2023")
QCD_HT100to200_2023.sigma       = 25400000 #pb
QCD_HT100to200_2023.year        = 2023
QCD_HT100to200_2023.dataset     = "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
QCD_HT100to200_2023.process     = "QCD_2023"
QCD_HT100to200_2023.unix_code   = 31002
QCD_HT100to200_2023.EE          = 0
QCD_HT200to400_2023             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT200to400_2023")
QCD_HT200to400_2023.sigma       = 1961000 #pb
QCD_HT200to400_2023.year        = 2023
QCD_HT200to400_2023.dataset     = "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
QCD_HT200to400_2023.process     = "QCD_2023"
QCD_HT200to400_2023.unix_code   = 31003
QCD_HT200to400_2023.EE          = 0
QCD_HT400to600_2023             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT400to600_2023")
QCD_HT400to600_2023.sigma       = 95620 #pb
QCD_HT400to600_2023.year        = 2023
QCD_HT400to600_2023.dataset     = "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
QCD_HT400to600_2023.process     = "QCD_2023"
QCD_HT400to600_2023.unix_code   = 31004
QCD_HT400to600_2023.EE          = 0
QCD_HT600to800_2023             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT600to800_2023")
QCD_HT600to800_2023.sigma       = 13540 #pb
QCD_HT600to800_2023.year        = 2023
QCD_HT600to800_2023.dataset     = "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
QCD_HT600to800_2023.process     = "QCD_2023"
QCD_HT600to800_2023.unix_code   = 31005
QCD_HT600to800_2023.EE          = 0
QCD_HT800to1000_2023            = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT800to1000_2023")
QCD_HT800to1000_2023.sigma      = 3033 #pb
QCD_HT800to1000_2023.year       = 2023
QCD_HT800to1000_2023.dataset    = "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
QCD_HT800to1000_2023.process    = "QCD_2023"
QCD_HT800to1000_2023.unix_code  = 31006
QCD_HT800to1000_2023.EE         = 0
QCD_HT1000to1200_2023           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1000to1200_2023")
QCD_HT1000to1200_2023.sigma     = 883.7 #pb
QCD_HT1000to1200_2023.year      = 2023
QCD_HT1000to1200_2023.dataset   = "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
QCD_HT1000to1200_2023.process   = "QCD_2023"
QCD_HT1000to1200_2023.unix_code = 31007
QCD_HT1000to1200_2023.EE        = 0
QCD_HT1200to1500_2023           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1200to1500_2023")
QCD_HT1200to1500_2023.sigma     = 383.5 #pb 
QCD_HT1200to1500_2023.year      = 2023
QCD_HT1200to1500_2023.dataset   = "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
QCD_HT1200to1500_2023.process   = "QCD_2023"
QCD_HT1200to1500_2023.unix_code = 31007
QCD_HT1200to1500_2023.EE        = 0
QCD_HT1500to2000_2023           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1500to2000_2023")
QCD_HT1500to2000_2023.sigma     = 125.2 #pb
QCD_HT1500to2000_2023.year      = 2023
QCD_HT1500to2000_2023.dataset   = "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
QCD_HT1500to2000_2023.process   = "QCD_2023"
QCD_HT1500to2000_2023.unix_code = 31008
QCD_HT1500to2000_2023.EE        = 0
QCD_HT2000_2023                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT2000_2023")
QCD_HT2000_2023.sigma           = 26.49 #pb
QCD_HT2000_2023.year            = 2023
QCD_HT2000_2023.dataset         = "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
QCD_HT2000_2023.process         = "QCD_2023"
QCD_HT2000_2023.unix_code       = 31009
QCD_HT2000_2023.EE              = 0
QCD_2023                        = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2023")
QCD_2023.year                   = 2023
QCD_2023.components             = [ 
                                    # QCD_HT40to70_2023, 
                                    QCD_HT70to100_2023, QCD_HT100to200_2023, QCD_HT200to400_2023,
                                    QCD_HT400to600_2023, QCD_HT600to800_2023, QCD_HT800to1000_2023, 
                                    QCD_HT1000to1200_2023, QCD_HT1200to1500_2023,
                                    QCD_HT1500to2000_2023, QCD_HT2000_2023
                                ]


################################ TTbar ################################
TT_semilep_2023             = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2023")
TT_semilep_2023.sigma       = sigma_ttbar_13p6TeV * BR_t_to_bqq_13p6TeV * BR_t_to_blv_13p6TeV * 2 #pb
TT_semilep_2023.year        = 2023
TT_semilep_2023.dataset     = "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
TT_semilep_2023.process     = 'TT_2023'
TT_semilep_2023.unix_code   = 31100
TT_semilep_2023.EE          = 0

TT_hadr_2023                = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_hadr_2023")
TT_hadr_2023.sigma          = sigma_ttbar_13p6TeV * BR_t_to_bqq_13p6TeV * BR_t_to_bqq_13p6TeV
TT_hadr_2023.year           = 2023
TT_hadr_2023.dataset        = "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
TT_hadr_2023.process        = 'TT_2023'
TT_hadr_2023.unix_code      = 31101
TT_hadr_2023.EE             = 0

TT_dilep_2023               = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_dilep_2023")
TT_dilep_2023.sigma         = sigma_ttbar_13p6TeV * BR_t_to_blv_13p6TeV * BR_t_to_blv_13p6TeV
TT_dilep_2023.year          = 2023
TT_dilep_2023.dataset       = "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
TT_dilep_2023.process       = 'TT_2023'
TT_dilep_2023.unix_code     = 31102
TT_dilep_2023.EE            = 0

TT_2023                     = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_2023")
TT_2023.year                = 2023
TT_2023.components          = [
                                TT_semilep_2023,
                                TT_hadr_2023,
                                TT_dilep_2023
                                ]

################################ SingleTop ################################
TWminustoLNu2Q_2023             = sample(ROOT.kViolet, 1, 1001, "tW", "TWminustoLNu2Q_2023")
TWminustoLNu2Q_2023.sigma       = sigma_tWminus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_lv_13p6TeV + BR_t_to_blv_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TWminustoLNu2Q_2023.year        = 2023
TWminustoLNu2Q_2023.dataset     = "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
TWminustoLNu2Q_2023.process     = 'TW_2023'
TWminustoLNu2Q_2023.EE          = 0

TWminusto4Q_2023                = sample(ROOT.kViolet, 1, 1001, "tW", "TWminusto4Q_2023")
TWminusto4Q_2023.sigma          = sigma_tWminus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TWminusto4Q_2023.year           = 2023
TWminusto4Q_2023.dataset        = "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
TWminusto4Q_2023.process        = 'TW_2023'
TWminusto4Q_2023.EE             = 0

TWminusto2L2Nu_2023             = sample(ROOT.kViolet, 1, 1001, "tW", "TWminusto2L2Nu_2023")
TWminusto2L2Nu_2023.sigma       = sigma_tWminus_13p6TeV * (BR_t_to_blv_13p6TeV * BR_W_to_lv_13p6TeV) #pb
TWminusto2L2Nu_2023.year        = 2023
TWminusto2L2Nu_2023.dataset     = "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
TWminusto2L2Nu_2023.process     = 'TW_2023'
TWminusto2L2Nu_2023.EE          = 0

TbarWplustoLNu2Q_2023           = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplustoLNu2Q_2023")
TbarWplustoLNu2Q_2023.sigma     = sigma_tbarWplus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_lv_13p6TeV + BR_t_to_blv_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TbarWplustoLNu2Q_2023.year      = 2023
TbarWplustoLNu2Q_2023.dataset   = "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v6/NANOAODSIM"
TbarWplustoLNu2Q_2023.process   = 'TW_2023'
TbarWplustoLNu2Q_2023.EE        = 0

TbarWplusto4Q_2023              = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplusto4Q_2023")
TbarWplusto4Q_2023.sigma        = sigma_tbarWplus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TbarWplusto4Q_2023.year         = 2023
TbarWplusto4Q_2023.dataset      = "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM"
TbarWplusto4Q_2023.process      = 'TW_2023'
TbarWplusto4Q_2023.EE           = 0

TbarWplusto2L2Nu_2023           = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplusto2L2Nu_2023")
TbarWplusto2L2Nu_2023.sigma     = sigma_tbarWplus_13p6TeV * (BR_t_to_blv_13p6TeV * BR_W_to_lv_13p6TeV) #pb
TbarWplusto2L2Nu_2023.year      = 2023
TbarWplusto2L2Nu_2023.dataset   = "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM"
TbarWplusto2L2Nu_2023.process   = 'TW_2023'
TbarWplusto2L2Nu_2023.EE        = 0

TW_2023                         = sample(ROOT.kViolet, 1, 1001, "tW", "TW_2023")
TW_2023.year                    = 2023
TW_2023.components              = [
                                    TWminustoLNu2Q_2023,
                                    TWminusto4Q_2023,
                                    TWminusto2L2Nu_2023,
                                    TbarWplustoLNu2Q_2023,
                                    TbarWplusto4Q_2023,
                                    TbarWplusto2L2Nu_2023
                                ]

################################ ZJets ################################
ZJetsToNuNu_HT100to200_2023             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT100to200_2023")
ZJetsToNuNu_HT100to200_2023.sigma       = 273.7 #pb
ZJetsToNuNu_HT100to200_2023.year        = 2023
ZJetsToNuNu_HT100to200_2023.dataset     = "/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
ZJetsToNuNu_HT100to200_2023.process     = 'ZJetsToNuNu_2023'
ZJetsToNuNu_HT100to200_2023.unix_code   = 31200
ZJetsToNuNu_HT100to200_2023.EE          = 0

ZJetsToNuNu_HT200to400_2023             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT200to400_2023")
ZJetsToNuNu_HT200to400_2023.sigma       = 75.96 #pb
ZJetsToNuNu_HT200to400_2023.year        = 2023
ZJetsToNuNu_HT200to400_2023.dataset     = "/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
ZJetsToNuNu_HT200to400_2023.process     = 'ZJetsToNuNu_2023'
ZJetsToNuNu_HT200to400_2023.unix_code   = 31201
ZJetsToNuNu_HT200to400_2023.EE          = 0

ZJetsToNuNu_HT400to800_2023             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT400to800_2023")
ZJetsToNuNu_HT400to800_2023.sigma       = 13.19 #pb
ZJetsToNuNu_HT400to800_2023.year        = 2023
ZJetsToNuNu_HT400to800_2023.dataset     = "/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
ZJetsToNuNu_HT400to800_2023.process     = 'ZJetsToNuNu_2023'
ZJetsToNuNu_HT400to800_2023.unix_code   = 31202
ZJetsToNuNu_HT400to800_2023.EE          = 0

ZJetsToNuNu_HT800to1500_2023            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT800to1500_2023")
ZJetsToNuNu_HT800to1500_2023.sigma      = 1.364 #pb
ZJetsToNuNu_HT800to1500_2023.year       = 2023
ZJetsToNuNu_HT800to1500_2023.dataset    = "/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
ZJetsToNuNu_HT800to1500_2023.process    = 'ZJetsToNuNu_2023'
ZJetsToNuNu_HT800to1500_2023.unix_code  = 31203
ZJetsToNuNu_HT800to1500_2023.EE         = 0

ZJetsToNuNu_HT1500to2500_2023           = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT1500to2500_2023")
ZJetsToNuNu_HT1500to2500_2023.sigma     = 0.09865 #pb
ZJetsToNuNu_HT1500to2500_2023.year      = 2023
ZJetsToNuNu_HT1500to2500_2023.dataset   = "/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
ZJetsToNuNu_HT1500to2500_2023.process   = 'ZJetsToNuNu_2023'
ZJetsToNuNu_HT1500to2500_2023.unix_code = 31204
ZJetsToNuNu_HT1500to2500_2023.EE        = 0

ZJetsToNuNu_HT2500_2023                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT2500_2023")
ZJetsToNuNu_HT2500_2023.sigma           = 0.006699 #pb
ZJetsToNuNu_HT2500_2023.year            = 2023
ZJetsToNuNu_HT2500_2023.dataset         = "/Zto2Nu-4Jets_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
ZJetsToNuNu_HT2500_2023.process         = 'ZJetsToNuNu_2023'
ZJetsToNuNu_HT2500_2023.unix_code       = 31205
ZJetsToNuNu_HT2500_2023.EE              = 0

ZJetsToNuNu_2023                        = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2023")
ZJetsToNuNu_2023.year                   = 2023
ZJetsToNuNu_2023.components             = [
                                            ZJetsToNuNu_HT100to200_2023,
                                            ZJetsToNuNu_HT200to400_2023,
                                            ZJetsToNuNu_HT400to800_2023,
                                            ZJetsToNuNu_HT800to1500_2023,
                                            ZJetsToNuNu_HT1500to2500_2023,
                                            ZJetsToNuNu_HT2500_2023 
                                            ]

ZJetsToNuNu_2jets_PT40to100_1J_2023            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_1J_2023")
ZJetsToNuNu_2jets_PT40to100_1J_2023.sigma      = 929.8	
ZJetsToNuNu_2jets_PT40to100_1J_2023.year       = 2023
ZJetsToNuNu_2jets_PT40to100_1J_2023.dataset    = "/Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_1J_2023.process    = 'ZJetsToNuNu_2jets_2023'
ZJetsToNuNu_2jets_PT40to100_1J_2023.unix_code  = 31206
ZJetsToNuNu_2jets_PT40to100_1J_2023.EE         = 0

ZJetsToNuNu_2jets_PT100to200_1J_2023            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_1J_2023")
ZJetsToNuNu_2jets_PT100to200_1J_2023.sigma      = 86.38
ZJetsToNuNu_2jets_PT100to200_1J_2023.year       = 2023
ZJetsToNuNu_2jets_PT100to200_1J_2023.dataset    = "/Zto2Nu-2Jets_PTNuNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_1J_2023.process    = 'ZJetsToNuNu_2jets_2023'
ZJetsToNuNu_2jets_PT100to200_1J_2023.unix_code  = 31207
ZJetsToNuNu_2jets_PT100to200_1J_2023.EE         = 0

ZJetsToNuNu_2jets_PT200to400_1J_2023            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_1J_2023")
ZJetsToNuNu_2jets_PT200to400_1J_2023.sigma      = 6.354	
ZJetsToNuNu_2jets_PT200to400_1J_2023.year       = 2023
ZJetsToNuNu_2jets_PT200to400_1J_2023.dataset    = "/Zto2Nu-2Jets_PTNuNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_1J_2023.process    = 'ZJetsToNuNu_2jets_2023'
ZJetsToNuNu_2jets_PT200to400_1J_2023.unix_code  = 31208
ZJetsToNuNu_2jets_PT200to400_1J_2023.EE         = 0

ZJetsToNuNu_2jets_PT400to600_1J_2023            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_1J_2023")
ZJetsToNuNu_2jets_PT400to600_1J_2023.sigma      = 0.2188
ZJetsToNuNu_2jets_PT400to600_1J_2023.year       = 2023
ZJetsToNuNu_2jets_PT400to600_1J_2023.dataset    = "/Zto2Nu-2Jets_PTNuNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_1J_2023.process    = 'ZJetsToNuNu_2jets_2023'
ZJetsToNuNu_2jets_PT400to600_1J_2023.unix_code  = 31209
ZJetsToNuNu_2jets_PT400to600_1J_2023.EE         = 0

ZJetsToNuNu_2jets_PT600_1J_2023                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_1J_2023")
ZJetsToNuNu_2jets_PT600_1J_2023.sigma           = 0.02583
ZJetsToNuNu_2jets_PT600_1J_2023.year            = 2023
ZJetsToNuNu_2jets_PT600_1J_2023.dataset         = "/Zto2Nu-2Jets_PTNuNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_1J_2023.process         = 'ZJetsToNuNu_2jets_2023'
ZJetsToNuNu_2jets_PT600_1J_2023.unix_code       = 31210
ZJetsToNuNu_2jets_PT600_1J_2023.EE              = 0

ZJetsToNuNu_2jets_PT40to100_2J_2023             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_2J_2023")
ZJetsToNuNu_2jets_PT40to100_2J_2023.sigma       = 335.5
ZJetsToNuNu_2jets_PT40to100_2J_2023.year        = 2023
ZJetsToNuNu_2jets_PT40to100_2J_2023.dataset     = "/Zto2Nu-2Jets_PTNuNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_2J_2023.process     = 'ZJetsToNuNu_2jets_2023'
ZJetsToNuNu_2jets_PT40to100_2J_2023.unix_code   = 31211
ZJetsToNuNu_2jets_PT40to100_2J_2023.EE          = 0

ZJetsToNuNu_2jets_PT100to200_2J_2023            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_2J_2023")
ZJetsToNuNu_2jets_PT100to200_2J_2023.sigma      = 100.4
ZJetsToNuNu_2jets_PT100to200_2J_2023.year       = 2023
ZJetsToNuNu_2jets_PT100to200_2J_2023.dataset    = "/Zto2Nu-2Jets_PTNuNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_2J_2023.process    = 'ZJetsToNuNu_2jets_2023'
ZJetsToNuNu_2jets_PT100to200_2J_2023.unix_code  = 31212
ZJetsToNuNu_2jets_PT100to200_2J_2023.EE         = 0

ZJetsToNuNu_2jets_PT200to400_2J_2023            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_2J_2023")
ZJetsToNuNu_2jets_PT200to400_2J_2023.sigma      = 13.86
ZJetsToNuNu_2jets_PT200to400_2J_2023.year       = 2023
ZJetsToNuNu_2jets_PT200to400_2J_2023.dataset    = "/Zto2Nu-2Jets_PTNuNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_2J_2023.process    = 'ZJetsToNuNu_2jets_2023'
ZJetsToNuNu_2jets_PT200to400_2J_2023.unix_code  = 31213
ZJetsToNuNu_2jets_PT200to400_2J_2023.EE         = 0

ZJetsToNuNu_2jets_PT400to600_2J_2023            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_2J_2023")
ZJetsToNuNu_2jets_PT400to600_2J_2023.sigma      = 0.7816
ZJetsToNuNu_2jets_PT400to600_2J_2023.year       = 2023
ZJetsToNuNu_2jets_PT400to600_2J_2023.dataset    = "/Zto2Nu-2Jets_PTNuNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_2J_2023.process    = 'ZJetsToNuNu_2jets_2023'
ZJetsToNuNu_2jets_PT400to600_2J_2023.unix_code  = 31214
ZJetsToNuNu_2jets_PT400to600_2J_2023.EE         = 0

ZJetsToNuNu_2jets_PT600_2J_2023                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_2J_2023")
ZJetsToNuNu_2jets_PT600_2J_2023.sigma           = 0.1311
ZJetsToNuNu_2jets_PT600_2J_2023.year            = 2023
ZJetsToNuNu_2jets_PT600_2J_2023.dataset         = "/Zto2Nu-2Jets_PTNuNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_2J_2023.process         = 'ZJetsToNuNu_2jets_2023'
ZJetsToNuNu_2jets_PT600_2J_2023.unix_code       = 31215
ZJetsToNuNu_2jets_PT600_2J_2023.EE              = 0

ZJetsToNuNu_2jets_2023 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_2023")
ZJetsToNuNu_2jets_2023.year = 2023
ZJetsToNuNu_2jets_2023.components = [
                                        ZJetsToNuNu_2jets_PT40to100_1J_2023,
                                        ZJetsToNuNu_2jets_PT100to200_1J_2023,
                                        ZJetsToNuNu_2jets_PT200to400_1J_2023,
                                        ZJetsToNuNu_2jets_PT400to600_1J_2023,
                                        ZJetsToNuNu_2jets_PT600_1J_2023,
                                        ZJetsToNuNu_2jets_PT40to100_2J_2023,
                                        ZJetsToNuNu_2jets_PT100to200_2J_2023,
                                        ZJetsToNuNu_2jets_PT200to400_2J_2023,
                                        ZJetsToNuNu_2jets_PT400to600_2J_2023,
                                        ZJetsToNuNu_2jets_PT600_2J_2023
                                    ]

################################ WJets ################################
WJets_HT120to200_2023               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT120to200_2023") 
WJets_HT120to200_2023.dataset       = "/WtoLNu-4Jets_MLNu-120to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v5/NANOAODSIM"
WJets_HT120to200_2023.sigma         = 167
WJets_HT120to200_2023.year          = 2023
WJets_HT120to200_2023.process       = "WJets_2023"
WJets_HT120to200_2023.unix_code     = 31300
WJets_HT120to200_2023.EE            = 0

WJets_HT200to400_2023               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT200to400_2023") 
WJets_HT200to400_2023.dataset       = "/WtoLNu-4Jets_MLNu-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v5/NANOAODSIM"
WJets_HT200to400_2023.sigma         = 20.3	
WJets_HT200to400_2023.year          = 2023
WJets_HT200to400_2023.process       = "WJets_2023"
WJets_HT200to400_2023.unix_code     = 31301
WJets_HT200to400_2023.EE            = 0

WJets_HT400to800_2023               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT400to800_2023") 
WJets_HT400to800_2023.dataset       = "/WtoLNu-4Jets_MLNu-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v4/NANOAODSIM"
WJets_HT400to800_2023.sigma         = 1.596
WJets_HT400to800_2023.year          = 2023
WJets_HT400to800_2023.process       = "WJets_2023"
WJets_HT400to800_2023.unix_code     = 31302
WJets_HT400to800_2023.EE            = 0

WJets_HT800to1500_2023              = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT800to1500_2023") 
WJets_HT800to1500_2023.dataset      = "/WtoLNu-4Jets_MLNu-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v4/NANOAODSIM"
WJets_HT800to1500_2023.sigma        = 0.1095	
WJets_HT800to1500_2023.year         = 2023
WJets_HT800to1500_2023.process      = "WJets_2023"
WJets_HT800to1500_2023.unix_code    = 31303
WJets_HT800to1500_2023.EE           = 0

WJets_HT1500to2500_2023             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT1500to2500_2023") 
WJets_HT1500to2500_2023.dataset     = "/WtoLNu-4Jets_MLNu-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
WJets_HT1500to2500_2023.sigma       = 0.006365
WJets_HT1500to2500_2023.year        = 2023
WJets_HT1500to2500_2023.process     = "WJets_2023"
WJets_HT1500to2500_2023.unix_code   = 31304
WJets_HT1500to2500_2023.EE          = 0

WJets_HT2500to4000_2023             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT2500to4000_2023") 
WJets_HT2500to4000_2023.dataset     = "/WtoLNu-4Jets_MLNu-2500to4000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v5/NANOAODSIM"
WJets_HT2500to4000_2023.sigma       = 0.0003463
WJets_HT2500to4000_2023.year        = 2023
WJets_HT2500to4000_2023.process     = "WJets_2023"
WJets_HT2500to4000_2023.unix_code   = 31305
WJets_HT2500to4000_2023.EE          = 0

WJets_HT4000to6000_2023             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT4000to6000_2023") 
WJets_HT4000to6000_2023.dataset     = "/WtoLNu-4Jets_MLNu-4000to6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v5/NANOAODSIM"
WJets_HT4000to6000_2023.sigma       = 0.00001075
WJets_HT4000to6000_2023.year        = 2023
WJets_HT4000to6000_2023.process     = "WJets_2023"
WJets_HT4000to6000_2023.unix_code   = 31306
WJets_HT4000to6000_2023.EE          = 0

WJets_HT6000_2023                   = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT6000_2023") 
WJets_HT6000_2023.dataset           = "/WtoLNu-4Jets_MLNu-6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v4/NANOAODSIM"
WJets_HT6000_2023.sigma             = 4.182e-7	
WJets_HT6000_2023.year              = 2023
WJets_HT6000_2023.process           = "WJets_2023"
WJets_HT6000_2023.unix_code         = 31307
WJets_HT6000_2023.EE                = 0

WJets_2023                  = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2023")
WJets_2023.year             = 2023
WJets_2023.components       = [WJets_HT120to200_2023, WJets_HT200to400_2023, WJets_HT400to800_2023, WJets_HT800to1500_2023, WJets_HT1500to2500_2023, WJets_HT2500to4000_2023, WJets_HT4000to6000_2023, WJets_HT6000_2023]

WJets_2jets0J_2023           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets0J_2023")
WJets_2jets0J_2023.dataset   = "/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM"
WJets_2jets0J_2023.sigma     = 55760 
WJets_2jets0J_2023.year      = 2023
WJets_2jets0J_2023.process   = "WJets_2jets_2023"
WJets_2jets0J_2023.unix_code = 31308
WJets_2jets0J_2023.EE        = 0

WJets_2jets1J_2023           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets1J_2023")
WJets_2jets1J_2023.dataset   = "/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
WJets_2jets1J_2023.sigma     = 9529 
WJets_2jets1J_2023.year      = 2023
WJets_2jets1J_2023.process   = "WJets_2jets_2023"
WJets_2jets1J_2023.unix_code = 31309
WJets_2jets1J_2023.EE        = 0

WJets_2jets2J_2023           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets2J_2023")
WJets_2jets2J_2023.dataset   = "/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM"
WJets_2jets2J_2023.sigma     = 3532 
WJets_2jets2J_2023.year      = 2023
WJets_2jets2J_2023.process   = "WJets_2jets_2023"
WJets_2jets2J_2023.unix_code = 31310
WJets_2jets2J_2023.EE        = 0

WJets_2jets_2023             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_2023")
WJets_2jets_2023.year        = 2023
WJets_2jets_2023.components  = [WJets_2jets0J_2023, WJets_2jets1J_2023, WJets_2jets2J_2023]

###############################################################################################################################
##########################################                                           ##########################################
##########################################                    2023postBPix           ##########################################
##########################################                                           ##########################################
###############################################################################################################################

################################ QCD ################################
# QCD_HT40to70_2023postBPix               = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT40to70_2023postBPix")
# QCD_HT40to70_2023postBPix.sigma         = 311400000 #pb
# QCD_HT40to70_2023postBPix.year          = 2023
# QCD_HT40to70_2023postBPix.dataset       = "/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
# QCD_HT40to70_2023postBPix.process       = "QCD_2023postBPix"
# QCD_HT40to70_2023postBPix.unix_code     = 41000
# QCD_HT40to70_2023postBPix.EE            = 1
QCD_HT70to100_2023postBPix              = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT70to100_2023postBPix")
QCD_HT70to100_2023postBPix.sigma        = 58500000 #pb 3.117e+08
QCD_HT70to100_2023postBPix.year         = 2023
QCD_HT70to100_2023postBPix.dataset      = "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
QCD_HT70to100_2023postBPix.process      = "QCD_2023postBPix"
QCD_HT70to100_2023postBPix.unix_code    = 41001
QCD_HT70to100_2023postBPix.EE           = 1

QCD_HT100to200_2023postBPix             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT100to200_2023postBPix")
QCD_HT100to200_2023postBPix.sigma       = 25400000 #pb
QCD_HT100to200_2023postBPix.year        = 2023
QCD_HT100to200_2023postBPix.dataset     = "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM"
QCD_HT100to200_2023postBPix.process     = "QCD_2023postBPix"
QCD_HT100to200_2023postBPix.unix_code   = 41002
QCD_HT100to200_2023postBPix.EE          = 1

QCD_HT200to400_2023postBPix             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT200to400_2023postBPix")
QCD_HT200to400_2023postBPix.sigma       = 1961000 #pb
QCD_HT200to400_2023postBPix.year        = 2023
QCD_HT200to400_2023postBPix.dataset     = "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
QCD_HT200to400_2023postBPix.process     = "QCD_2023postBPix"
QCD_HT200to400_2023postBPix.unix_code   = 41003
QCD_HT200to400_2023postBPix.EE          = 1

QCD_HT400to600_2023postBPix             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT400to600_2023postBPix")
QCD_HT400to600_2023postBPix.sigma       = 95620 #pb
QCD_HT400to600_2023postBPix.year        = 2023
QCD_HT400to600_2023postBPix.dataset     = "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM"
QCD_HT400to600_2023postBPix.process     = "QCD_2023postBPix"
QCD_HT400to600_2023postBPix.unix_code   = 41004
QCD_HT400to600_2023postBPix.EE          = 1

QCD_HT600to800_2023postBPix             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT600to800_2023postBPix")
QCD_HT600to800_2023postBPix.sigma       = 13540 #pb
QCD_HT600to800_2023postBPix.year        = 2023
QCD_HT600to800_2023postBPix.dataset     = "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
QCD_HT600to800_2023postBPix.process     = "QCD_2023postBPix"
QCD_HT600to800_2023postBPix.unix_code   = 41005
QCD_HT600to800_2023postBPix.EE          = 1

QCD_HT800to1000_2023postBPix            = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT800to1000_2023postBPix")
QCD_HT800to1000_2023postBPix.sigma      = 3033 #pb
QCD_HT800to1000_2023postBPix.year       = 2023
QCD_HT800to1000_2023postBPix.dataset    = "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM"
QCD_HT800to1000_2023postBPix.process    = "QCD_2023postBPix"
QCD_HT800to1000_2023postBPix.unix_code  = 41006
QCD_HT800to1000_2023postBPix.EE         = 1

QCD_HT1000to1200_2023postBPix           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1000to1200_2023postBPix")
QCD_HT1000to1200_2023postBPix.sigma     = 883.7 #pb
QCD_HT1000to1200_2023postBPix.year      = 2023
QCD_HT1000to1200_2023postBPix.dataset   = "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM"
QCD_HT1000to1200_2023postBPix.process   = "QCD_2023postBPix"
QCD_HT1000to1200_2023postBPix.unix_code = 41007
QCD_HT1000to1200_2023postBPix.EE        = 1

QCD_HT1200to1500_2023postBPix           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1200to1500_2023postBPix")
QCD_HT1200to1500_2023postBPix.sigma     = 383.5 #pb
QCD_HT1200to1500_2023postBPix.year      = 2023
QCD_HT1200to1500_2023postBPix.dataset   = "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM"
QCD_HT1200to1500_2023postBPix.process   = "QCD_2023postBPix"
QCD_HT1200to1500_2023postBPix.unix_code = 41007
QCD_HT1200to1500_2023postBPix.EE        = 1

QCD_HT1500to2000_2023postBPix           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1500to2000_2023postBPix")
QCD_HT1500to2000_2023postBPix.sigma     = 125.2 #pb
QCD_HT1500to2000_2023postBPix.year      = 2023
QCD_HT1500to2000_2023postBPix.dataset   = "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
QCD_HT1500to2000_2023postBPix.process   = "QCD_2023postBPix"
QCD_HT1500to2000_2023postBPix.unix_code = 41008
QCD_HT1500to2000_2023postBPix.EE        = 1

QCD_HT2000_2023postBPix                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT2000_2023postBPix")
QCD_HT2000_2023postBPix.sigma           = 26.49 #pb
QCD_HT2000_2023postBPix.year            = 2023
QCD_HT2000_2023postBPix.dataset         = "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM"
QCD_HT2000_2023postBPix.process         = "QCD_2023postBPix"
QCD_HT2000_2023postBPix.unix_code       = 41009
QCD_HT2000_2023postBPix.EE              = 1

QCD_2023postBPix                        = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2023postBPix")
QCD_2023postBPix.year                   = 2023
QCD_2023postBPix.components             = [ 
                                    # QCD_HT40to70_2023postBPix, 
                                    QCD_HT70to100_2023postBPix, QCD_HT100to200_2023postBPix, QCD_HT200to400_2023postBPix,
                                    QCD_HT400to600_2023postBPix, QCD_HT600to800_2023postBPix, QCD_HT800to1000_2023postBPix, 
                                    QCD_HT1000to1200_2023postBPix,QCD_HT1200to1500_2023postBPix,
                                    QCD_HT1500to2000_2023postBPix, QCD_HT2000_2023postBPix
                                ]


# /QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-JMENano12p5_132X_mcRun3_2023_realistic_postEE_v4-v2/NANOAODSIM


################################ TTbar ################################
TT_semilep_2023postBPix             = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2023postBPix")
TT_semilep_2023postBPix.sigma       = sigma_ttbar_13p6TeV * BR_t_to_bqq_13p6TeV * BR_t_to_blv_13p6TeV * 2 #pb 
TT_semilep_2023postBPix.year        = 2023
TT_semilep_2023postBPix.dataset     = "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
TT_semilep_2023postBPix.process     = 'TT_2023postBPix'
TT_semilep_2023postBPix.unix_code   = 41100
TT_semilep_2023postBPix.EE          = 1

TT_hadr_2023postBPix                = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_hadr_2023postBPix")
TT_hadr_2023postBPix.sigma          = sigma_ttbar_13p6TeV * BR_t_to_bqq_13p6TeV * BR_t_to_bqq_13p6TeV
TT_hadr_2023postBPix.year           = 2023
TT_hadr_2023postBPix.dataset        = "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
TT_hadr_2023postBPix.process        = 'TT_2023postBPix'
TT_hadr_2023postBPix.unix_code      = 41101
TT_hadr_2023postBPix.EE             = 1

TT_dilep_2023postBPix               = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_dilep_2023postBPix")
TT_dilep_2023postBPix.sigma         = sigma_ttbar_13p6TeV * BR_t_to_blv_13p6TeV * BR_t_to_blv_13p6TeV
TT_dilep_2023postBPix.year          = 2023
TT_dilep_2023postBPix.dataset       = "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
TT_dilep_2023postBPix.process       = 'TT_2023postBPix'
TT_dilep_2023postBPix.unix_code     = 41102
TT_dilep_2023postBPix.EE            = 1

TT_2023postBPix                     = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_2023postBPix")
TT_2023postBPix.year                = 2023
TT_2023postBPix.components          = [
                                        TT_semilep_2023postBPix,
                                        TT_hadr_2023postBPix,
                                        TT_dilep_2023postBPix
                                        ]

################################ SingleTop ################################
TWminustoLNu2Q_2023postBPix             = sample(ROOT.kViolet, 1, 1001, "tW", "TWminustoLNu2Q_2023postBPix")
TWminustoLNu2Q_2023postBPix.sigma       = sigma_tWminus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_lv_13p6TeV + BR_t_to_blv_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TWminustoLNu2Q_2023postBPix.year        = 2023
TWminustoLNu2Q_2023postBPix.dataset     = "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
TWminustoLNu2Q_2023postBPix.process     = 'TW_2023postBPix'
TWminustoLNu2Q_2023postBPix.EE          = 1

TWminusto4Q_2023postBPix                = sample(ROOT.kViolet, 1, 1001, "tW", "TWminusto4Q_2023postBPix")
TWminusto4Q_2023postBPix.sigma          = sigma_tWminus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TWminusto4Q_2023postBPix.year           = 2023
TWminusto4Q_2023postBPix.dataset        = "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
TWminusto4Q_2023postBPix.process        = 'TW_2023postBPix'
TWminusto4Q_2023postBPix.EE             = 1

TWminusto2L2Nu_2023postBPix             = sample(ROOT.kViolet, 1, 1001, "tW", "TWminusto2L2Nu_2023postBPix")
TWminusto2L2Nu_2023postBPix.sigma       = sigma_tWminus_13p6TeV * (BR_t_to_blv_13p6TeV * BR_W_to_lv_13p6TeV) #pb
TWminusto2L2Nu_2023postBPix.year        = 2023
TWminusto2L2Nu_2023postBPix.dataset     = "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
TWminusto2L2Nu_2023postBPix.process     = 'TW_2023postBPix'
TWminusto2L2Nu_2023postBPix.EE          = 1

TbarWplustoLNu2Q_2023postBPix           = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplustoLNu2Q_2023postBPix")
TbarWplustoLNu2Q_2023postBPix.sigma     = sigma_tbarWplus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_lv_13p6TeV + BR_t_to_blv_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TbarWplustoLNu2Q_2023postBPix.year      = 2023
TbarWplustoLNu2Q_2023postBPix.dataset   = "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM"
TbarWplustoLNu2Q_2023postBPix.process   = 'TW_2023postBPix'
TbarWplustoLNu2Q_2023postBPix.EE        = 1

TbarWplusto4Q_2023postBPix              = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplusto4Q_2023postBPix")
TbarWplusto4Q_2023postBPix.sigma        = sigma_tbarWplus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TbarWplusto4Q_2023postBPix.year         = 2023
TbarWplusto4Q_2023postBPix.dataset      = "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM"
TbarWplusto4Q_2023postBPix.process      = 'TW_2023postBPix'
TbarWplusto4Q_2023postBPix.EE           = 1

TbarWplusto2L2Nu_2023postBPix           = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplusto2L2Nu_2023postBPix")
TbarWplusto2L2Nu_2023postBPix.sigma     = sigma_tbarWplus_13p6TeV * (BR_t_to_blv_13p6TeV * BR_W_to_lv_13p6TeV) #pb
TbarWplusto2L2Nu_2023postBPix.year      = 2023
TbarWplusto2L2Nu_2023postBPix.dataset   = "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM"
TbarWplusto2L2Nu_2023postBPix.process   = 'TW_2023postBPix'
TbarWplusto2L2Nu_2023postBPix.EE        = 1

TW_2023postBPix                         = sample(ROOT.kViolet, 1, 1001, "tW", "TW_2023postBPix")
TW_2023postBPix.year                    = 2023
TW_2023postBPix.components              = [
                                            TWminustoLNu2Q_2023postBPix,
                                            TWminusto4Q_2023postBPix,
                                            TWminusto2L2Nu_2023postBPix,
                                            TbarWplustoLNu2Q_2023postBPix,
                                            TbarWplusto4Q_2023postBPix,
                                            TbarWplusto2L2Nu_2023postBPix
                                        ]

################################ ZJets ################################

ZJetsToNuNu_HT100to200_2023postBPix             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT100to200_2023postBPix")
ZJetsToNuNu_HT100to200_2023postBPix.sigma       = 273.6 #pb
ZJetsToNuNu_HT100to200_2023postBPix.year        = 2023
ZJetsToNuNu_HT100to200_2023postBPix.dataset     = "/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT100to200_2023postBPix.process     = 'ZJetsToNuNu_2023postBPix'
ZJetsToNuNu_HT100to200_2023postBPix.unix_code   = 41200
ZJetsToNuNu_HT100to200_2023postBPix.EE          = 1

ZJetsToNuNu_HT200to400_2023postBPix             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT200to400_2023postBPix")
ZJetsToNuNu_HT200to400_2023postBPix.sigma       = 76.14 #pb
ZJetsToNuNu_HT200to400_2023postBPix.year        = 2023
ZJetsToNuNu_HT200to400_2023postBPix.dataset     = "/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT200to400_2023postBPix.process     = 'ZJetsToNuNu_2023postBPix'
ZJetsToNuNu_HT200to400_2023postBPix.unix_code   = 41201
ZJetsToNuNu_HT200to400_2023postBPix.EE          = 1

ZJetsToNuNu_HT400to800_2023postBPix             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT400to800_2023postBPix")
ZJetsToNuNu_HT400to800_2023postBPix.sigma       = 13.18 #pb
ZJetsToNuNu_HT400to800_2023postBPix.year        = 2023
ZJetsToNuNu_HT400to800_2023postBPix.dataset     = "/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT400to800_2023postBPix.process     = 'ZJetsToNuNu_2023postBPix'
ZJetsToNuNu_HT400to800_2023postBPix.unix_code   = 41202
ZJetsToNuNu_HT400to800_2023postBPix.EE          = 1

ZJetsToNuNu_HT800to1500_2023postBPix            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT800to1500_2023postBPix")
ZJetsToNuNu_HT800to1500_2023postBPix.sigma      = 1.366 #pb
ZJetsToNuNu_HT800to1500_2023postBPix.year       = 2023
ZJetsToNuNu_HT800to1500_2023postBPix.dataset    = "/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT800to1500_2023postBPix.process    = 'ZJetsToNuNu_2023postBPix'
ZJetsToNuNu_HT800to1500_2023postBPix.unix_code  = 41203
ZJetsToNuNu_HT800to1500_2023postBPix.EE         = 1

ZJetsToNuNu_HT1500to2500_2023postBPix           = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT1500to2500_2023postBPix")
ZJetsToNuNu_HT1500to2500_2023postBPix.sigma     = 0.09852 #pb
ZJetsToNuNu_HT1500to2500_2023postBPix.year      = 2023
ZJetsToNuNu_HT1500to2500_2023postBPix.dataset   = "/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT1500to2500_2023postBPix.process   = 'ZJetsToNuNu_2023postBPix'
ZJetsToNuNu_HT1500to2500_2023postBPix.unix_code = 41204
ZJetsToNuNu_HT1500to2500_2023postBPix.EE        = 1

ZJetsToNuNu_HT2500_2023postBPix                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT2500_2023postBPix")
ZJetsToNuNu_HT2500_2023postBPix.sigma           = 0.006699 #pb
ZJetsToNuNu_HT2500_2023postBPix.year            = 2023
ZJetsToNuNu_HT2500_2023postBPix.dataset         = "/Zto2Nu-4Jets_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
ZJetsToNuNu_HT2500_2023postBPix.process         = 'ZJetsToNuNu_2023postBPix'
ZJetsToNuNu_HT2500_2023postBPix.unix_code       = 41205
ZJetsToNuNu_HT2500_2023postBPix.EE              = 1

ZJetsToNuNu_2023postBPix                        = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2023postBPix")
ZJetsToNuNu_2023postBPix.year                   = 2023
ZJetsToNuNu_2023postBPix.components             = [
                                            ZJetsToNuNu_HT100to200_2023postBPix, ZJetsToNuNu_HT200to400_2023postBPix, ZJetsToNuNu_HT400to800_2023postBPix,
                                            ZJetsToNuNu_HT800to1500_2023postBPix, ZJetsToNuNu_HT1500to2500_2023postBPix, ZJetsToNuNu_HT2500_2023postBPix 
                                            ]

ZJetsToNuNu_2jets_PT40to100_1J_2023postBPix            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_1J_2023postBPix")
ZJetsToNuNu_2jets_PT40to100_1J_2023postBPix.sigma      = 929.8	
ZJetsToNuNu_2jets_PT40to100_1J_2023postBPix.year       = 2023
ZJetsToNuNu_2jets_PT40to100_1J_2023postBPix.dataset    = "/Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_1J_2023postBPix.process    = 'ZJetsToNuNu_2jets_2023postBPix'
ZJetsToNuNu_2jets_PT40to100_1J_2023postBPix.unix_code  = 41207
ZJetsToNuNu_2jets_PT40to100_1J_2023postBPix.EE         = 1

ZJetsToNuNu_2jets_PT100to200_1J_2023postBPix            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_1J_2023postBPix")
ZJetsToNuNu_2jets_PT100to200_1J_2023postBPix.sigma      = 86.38
ZJetsToNuNu_2jets_PT100to200_1J_2023postBPix.year       = 2023
ZJetsToNuNu_2jets_PT100to200_1J_2023postBPix.dataset    = "/Zto2Nu-2Jets_PTNuNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_1J_2023postBPix.process    = 'ZJetsToNuNu_2jets_2023postBPix'
ZJetsToNuNu_2jets_PT100to200_1J_2023postBPix.unix_code  = 41208
ZJetsToNuNu_2jets_PT100to200_1J_2023postBPix.EE         = 1

ZJetsToNuNu_2jets_PT200to400_1J_2023postBPix            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_1J_2023postBPix")
ZJetsToNuNu_2jets_PT200to400_1J_2023postBPix.sigma      = 6.354	
ZJetsToNuNu_2jets_PT200to400_1J_2023postBPix.year       = 2023
ZJetsToNuNu_2jets_PT200to400_1J_2023postBPix.dataset    = "/Zto2Nu-2Jets_PTNuNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_1J_2023postBPix.process    = 'ZJetsToNuNu_2jets_2023postBPix'
ZJetsToNuNu_2jets_PT200to400_1J_2023postBPix.unix_code  = 41209
ZJetsToNuNu_2jets_PT200to400_1J_2023postBPix.EE         = 1

ZJetsToNuNu_2jets_PT400to600_1J_2023postBPix            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_1J_2023postBPix")
ZJetsToNuNu_2jets_PT400to600_1J_2023postBPix.sigma      = 0.2188
ZJetsToNuNu_2jets_PT400to600_1J_2023postBPix.year       = 2023
ZJetsToNuNu_2jets_PT400to600_1J_2023postBPix.dataset    = "/Zto2Nu-2Jets_PTNuNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_1J_2023postBPix.process    = 'ZJetsToNuNu_2jets_2023postBPix'
ZJetsToNuNu_2jets_PT400to600_1J_2023postBPix.unix_code  = 41210
ZJetsToNuNu_2jets_PT400to600_1J_2023postBPix.EE         = 1

ZJetsToNuNu_2jets_PT600_1J_2023postBPix                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_1J_2023postBPix")
ZJetsToNuNu_2jets_PT600_1J_2023postBPix.sigma           = 0.02583
ZJetsToNuNu_2jets_PT600_1J_2023postBPix.year            = 2023
ZJetsToNuNu_2jets_PT600_1J_2023postBPix.dataset         = "/Zto2Nu-2Jets_PTNuNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_1J_2023postBPix.process         = 'ZJetsToNuNu_2jets_2023postBPix'
ZJetsToNuNu_2jets_PT600_1J_2023postBPix.unix_code       = 41211
ZJetsToNuNu_2jets_PT600_1J_2023postBPix.EE              = 1

ZJetsToNuNu_2jets_PT40to100_2J_2023postBPix             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_2J_2023postBPix")
ZJetsToNuNu_2jets_PT40to100_2J_2023postBPix.sigma       = 335.5
ZJetsToNuNu_2jets_PT40to100_2J_2023postBPix.year        = 2023
ZJetsToNuNu_2jets_PT40to100_2J_2023postBPix.dataset     = "/Zto2Nu-2Jets_PTNuNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_2J_2023postBPix.process     = 'ZJetsToNuNu_2jets_2023postBPix'
ZJetsToNuNu_2jets_PT40to100_2J_2023postBPix.unix_code   = 41212
ZJetsToNuNu_2jets_PT40to100_2J_2023postBPix.EE          = 1

ZJetsToNuNu_2jets_PT100to200_2J_2023postBPix            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_2J_2023postBPix")
ZJetsToNuNu_2jets_PT100to200_2J_2023postBPix.sigma      = 100.4
ZJetsToNuNu_2jets_PT100to200_2J_2023postBPix.year       = 2023
ZJetsToNuNu_2jets_PT100to200_2J_2023postBPix.dataset    = "/Zto2Nu-2Jets_PTNuNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_2J_2023postBPix.process    = 'ZJetsToNuNu_2jets_2023postBPix'
ZJetsToNuNu_2jets_PT100to200_2J_2023postBPix.unix_code  = 41213
ZJetsToNuNu_2jets_PT100to200_2J_2023postBPix.EE         = 1

ZJetsToNuNu_2jets_PT200to400_2J_2023postBPix            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_2J_2023postBPix")
ZJetsToNuNu_2jets_PT200to400_2J_2023postBPix.sigma      = 13.86
ZJetsToNuNu_2jets_PT200to400_2J_2023postBPix.year       = 2023
ZJetsToNuNu_2jets_PT200to400_2J_2023postBPix.dataset    = "/Zto2Nu-2Jets_PTNuNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_2J_2023postBPix.process    = 'ZJetsToNuNu_2jets_2023postBPix'
ZJetsToNuNu_2jets_PT200to400_2J_2023postBPix.unix_code  = 41214
ZJetsToNuNu_2jets_PT200to400_2J_2023postBPix.EE         = 1

ZJetsToNuNu_2jets_PT400to600_2J_2023postBPix            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_2J_2023postBPix")
ZJetsToNuNu_2jets_PT400to600_2J_2023postBPix.sigma      = 0.7816
ZJetsToNuNu_2jets_PT400to600_2J_2023postBPix.year       = 2023
ZJetsToNuNu_2jets_PT400to600_2J_2023postBPix.dataset    = "/Zto2Nu-2Jets_PTNuNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_2J_2023postBPix.process    = 'ZJetsToNuNu_2jets_2023postBPix'
ZJetsToNuNu_2jets_PT400to600_2J_2023postBPix.unix_code  = 41215
ZJetsToNuNu_2jets_PT400to600_2J_2023postBPix.EE         = 1

ZJetsToNuNu_2jets_PT600_2J_2023postBPix                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_2J_2023postBPix")
ZJetsToNuNu_2jets_PT600_2J_2023postBPix.sigma           = 0.1311
ZJetsToNuNu_2jets_PT600_2J_2023postBPix.year            = 2023
ZJetsToNuNu_2jets_PT600_2J_2023postBPix.dataset         = "/Zto2Nu-2Jets_PTNuNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_2J_2023postBPix.process         = 'ZJetsToNuNu_2jets_2023postBPix'
ZJetsToNuNu_2jets_PT600_2J_2023postBPix.unix_code       = 41216
ZJetsToNuNu_2jets_PT600_2J_2023postBPix.EE              = 1

ZJetsToNuNu_2jets_2023postBPix = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_2023postBPix")
ZJetsToNuNu_2jets_2023postBPix.year = 2023
ZJetsToNuNu_2jets_2023postBPix.components = [
                                        ZJetsToNuNu_2jets_PT40to100_1J_2023postBPix,
                                        ZJetsToNuNu_2jets_PT100to200_1J_2023postBPix,
                                        ZJetsToNuNu_2jets_PT200to400_1J_2023postBPix,
                                        ZJetsToNuNu_2jets_PT400to600_1J_2023postBPix,
                                        ZJetsToNuNu_2jets_PT600_1J_2023postBPix,
                                        ZJetsToNuNu_2jets_PT40to100_2J_2023postBPix,
                                        ZJetsToNuNu_2jets_PT100to200_2J_2023postBPix,
                                        ZJetsToNuNu_2jets_PT200to400_2J_2023postBPix,
                                        ZJetsToNuNu_2jets_PT400to600_2J_2023postBPix,
                                        ZJetsToNuNu_2jets_PT600_2J_2023postBPix
                                    ]
################################ WJets ################################

WJets_HT120to200_2023postBPix               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT120to200_2023postBPix") 
WJets_HT120to200_2023postBPix.dataset       = "/WtoLNu-4Jets_MLNu-120to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM"
WJets_HT120to200_2023postBPix.sigma         = 167
WJets_HT120to200_2023postBPix.year          = 2023
WJets_HT120to200_2023postBPix.process       = "WJets_2023"
WJets_HT120to200_2023postBPix.unix_code     = 41300
WJets_HT120to200_2023postBPix.EE            = 1

WJets_HT200to400_2023postBPix               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT200to400_2023postBPix") 
WJets_HT200to400_2023postBPix.dataset       = "/WtoLNu-4Jets_MLNu-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM"
WJets_HT200to400_2023postBPix.sigma         = 20.3
WJets_HT200to400_2023postBPix.year          = 2023
WJets_HT200to400_2023postBPix.process       = "WJets_2023"
WJets_HT200to400_2023postBPix.unix_code     = 41301
WJets_HT200to400_2023postBPix.EE            = 1

WJets_HT400to800_2023postBPix               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT400to800_2023postBPix") 
WJets_HT400to800_2023postBPix.dataset       = "/WtoLNu-4Jets_MLNu-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v5/NANOAODSIM"
WJets_HT400to800_2023postBPix.sigma         = 1.596	
WJets_HT400to800_2023postBPix.year          = 2023
WJets_HT400to800_2023postBPix.process       = "WJets_2023"
WJets_HT400to800_2023postBPix.unix_code     = 41302
WJets_HT400to800_2023postBPix.EE            = 1

WJets_HT800to1500_2023postBPix              = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT800to1500_2023postBPix") 
WJets_HT800to1500_2023postBPix.dataset      = "/WtoLNu-4Jets_MLNu-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM"
WJets_HT800to1500_2023postBPix.sigma        = 0.1095
WJets_HT800to1500_2023postBPix.year         = 2023
WJets_HT800to1500_2023postBPix.process      = "WJets_2023"
WJets_HT800to1500_2023postBPix.unix_code    = 41303
WJets_HT800to1500_2023postBPix.EE           = 1

WJets_HT1500to2500_2023postBPix             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT1500to2500_2023postBPix") 
WJets_HT1500to2500_2023postBPix.dataset     = "/WtoLNu-4Jets_MLNu-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM"
WJets_HT1500to2500_2023postBPix.sigma       = 0.006365
WJets_HT1500to2500_2023postBPix.year        = 2023
WJets_HT1500to2500_2023postBPix.process     = "WJets_2023"
WJets_HT1500to2500_2023postBPix.unix_code   = 41304
WJets_HT1500to2500_2023postBPix.EE          = 1

WJets_HT2500to4000_2023postBPix             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT2500to4000_2023postBPix") 
WJets_HT2500to4000_2023postBPix.dataset     = "/WtoLNu-4Jets_MLNu-2500to4000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v5/NANOAODSIM"
WJets_HT2500to4000_2023postBPix.sigma       = 0.0003463
WJets_HT2500to4000_2023postBPix.year        = 2023
WJets_HT2500to4000_2023postBPix.process     = "WJets_2023"
WJets_HT2500to4000_2023postBPix.unix_code   = 41305
WJets_HT2500to4000_2023postBPix.EE          = 1

WJets_HT4000to6000_2023postBPix             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT4000to6000_2023postBPix") 
WJets_HT4000to6000_2023postBPix.dataset     = "/WtoLNu-4Jets_MLNu-4000to6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM"
WJets_HT4000to6000_2023postBPix.sigma       = 0.00001075
WJets_HT4000to6000_2023postBPix.year        = 2023
WJets_HT4000to6000_2023postBPix.process     = "WJets_2023"
WJets_HT4000to6000_2023postBPix.unix_code   = 41306
WJets_HT4000to6000_2023postBPix.EE          = 1

WJets_HT6000_2023postBPix                   = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT6000_2023postBPix") 
WJets_HT6000_2023postBPix.dataset           = "/WtoLNu-4Jets_MLNu-6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v5/NANOAODSIM"
WJets_HT6000_2023postBPix.sigma             = 4.182e-7
WJets_HT6000_2023postBPix.year              = 2023
WJets_HT6000_2023postBPix.process           = "WJets_2023"
WJets_HT6000_2023postBPix.unix_code         = 41307
WJets_HT6000_2023postBPix.EE                = 1

WJets_2023postBPix                  = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2023postBPix")
WJets_2023postBPix.year             = 2023
WJets_2023postBPix.components       = [WJets_HT120to200_2023postBPix, WJets_HT200to400_2023postBPix, WJets_HT400to800_2023postBPix, WJets_HT800to1500_2023postBPix, WJets_HT1500to2500_2023postBPix, WJets_HT2500to4000_2023postBPix, WJets_HT4000to6000_2023postBPix, WJets_HT6000_2023postBPix]


WJets_2jets0J_2023postBPix           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets0J_2023postBPix")
WJets_2jets0J_2023postBPix.dataset   = "/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM"
WJets_2jets0J_2023postBPix.sigma     = 55760
WJets_2jets0J_2023postBPix.year      = 2023
WJets_2jets0J_2023postBPix.process   = "WJets_2jets_2023postBPix"
WJets_2jets0J_2023postBPix.unix_code = 41308
WJets_2jets0J_2023postBPix.EE        = 1

WJets_2jets1J_2023postBPix           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets1J_2023postBPix")
WJets_2jets1J_2023postBPix.dataset   = "/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM"
WJets_2jets1J_2023postBPix.sigma     = 9529
WJets_2jets1J_2023postBPix.year      = 2023
WJets_2jets1J_2023postBPix.process   = "WJets_2jets_2023postBPix"
WJets_2jets1J_2023postBPix.unix_code = 41309
WJets_2jets1J_2023postBPix.EE        = 1

WJets_2jets2J_2023postBPix           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets2J_2023postBPix")
WJets_2jets2J_2023postBPix.dataset   = "/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM"
WJets_2jets2J_2023postBPix.sigma     = 3532
WJets_2jets2J_2023postBPix.year      = 2023
WJets_2jets2J_2023postBPix.process   = "WJets_2jets_2023postBPix"
WJets_2jets2J_2023postBPix.unix_code = 41310
WJets_2jets2J_2023postBPix.EE        = 1

WJets_2jets_2023postBPix             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_2023postBPix")
WJets_2jets_2023postBPix.year        = 2023
WJets_2jets_2023postBPix.components  = [WJets_2jets0J_2023postBPix, WJets_2jets1J_2023postBPix, WJets_2jets2J_2023postBPix]

###############################################################################################################################
##########################################                                           ##########################################
##########################################                    2024                   ##########################################
##########################################                                           ##########################################
###############################################################################################################################
################################ QCD ################################
# QCD_HT40to70_2024               = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT40to70_2024")
# QCD_HT40to70_2024.sigma         = 311.7*(10**6) #pb
# QCD_HT40to70_2024.year          = 2024
# QCD_HT40to70_2024.dataset       = "/QCD-4Jets_Bin-HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
# QCD_HT40to70_2024.process       = "QCD_2024"
# QCD_HT40to70_2024.unix_code     = 31000
# QCD_HT40to70_2024.EE            = 0
QCD_HT70to100_2024              = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT70to100_2024")
QCD_HT70to100_2024.sigma        = 58500000 #pb
QCD_HT70to100_2024.year         = 2024
QCD_HT70to100_2024.dataset      = "/QCD-4Jets_Bin-HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
QCD_HT70to100_2024.process      = "QCD_2024"
QCD_HT70to100_2024.unix_code    = 31001
QCD_HT70to100_2024.EE           = 0
QCD_HT100to200_2024             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT100to200_2024")
QCD_HT100to200_2024.sigma       = 25400000 #pb
QCD_HT100to200_2024.year        = 2024
QCD_HT100to200_2024.dataset     = "/QCD-4Jets_Bin-HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
QCD_HT100to200_2024.process     = "QCD_2024"
QCD_HT100to200_2024.unix_code   = 31002
QCD_HT100to200_2024.EE          = 0
QCD_HT200to400_2024             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT200to400_2024")
QCD_HT200to400_2024.sigma       = 1961000 #pb
QCD_HT200to400_2024.year        = 2024
QCD_HT200to400_2024.dataset     = "/QCD-4Jets_Bin-HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
QCD_HT200to400_2024.process     = "QCD_2024"
QCD_HT200to400_2024.unix_code   = 31003
QCD_HT200to400_2024.EE          = 0
QCD_HT400to600_2024             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT400to600_2024")
QCD_HT400to600_2024.sigma       = 95620 #pb
QCD_HT400to600_2024.year        = 2024
QCD_HT400to600_2024.dataset     = "/QCD-4Jets_Bin-HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
QCD_HT400to600_2024.process     = "QCD_2024"
QCD_HT400to600_2024.unix_code   = 31004
QCD_HT400to600_2024.EE          = 0
QCD_HT600to800_2024             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT600to800_2024")
QCD_HT600to800_2024.sigma       = 13540 #pb
QCD_HT600to800_2024.year        = 2024
QCD_HT600to800_2024.dataset     = "/QCD-4Jets_Bin-HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
QCD_HT600to800_2024.process     = "QCD_2024"
QCD_HT600to800_2024.unix_code   = 31005
QCD_HT600to800_2024.EE          = 0
QCD_HT800to1000_2024            = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT800to1000_2024")
QCD_HT800to1000_2024.sigma      = 3033 #pb
QCD_HT800to1000_2024.year       = 2024
QCD_HT800to1000_2024.dataset    = "/QCD-4Jets_Bin-HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
QCD_HT800to1000_2024.process    = "QCD_2024"
QCD_HT800to1000_2024.unix_code  = 31006
QCD_HT800to1000_2024.EE         = 0
QCD_HT1000to1200_2024           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1000to1200_2024")
QCD_HT1000to1200_2024.sigma     = 883.7 #pb
QCD_HT1000to1200_2024.year      = 2024
QCD_HT1000to1200_2024.dataset   = "/QCD-4Jets_Bin-HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
QCD_HT1000to1200_2024.process   = "QCD_2024"
QCD_HT1000to1200_2024.unix_code = 31007
QCD_HT1000to1200_2024.EE        = 0
QCD_HT1200to1500_2024           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1200to1500_2024")
QCD_HT1200to1500_2024.sigma     = 383.5 #pb 
QCD_HT1200to1500_2024.year      = 2024
QCD_HT1200to1500_2024.dataset   = "/QCD-4Jets_Bin-HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
QCD_HT1200to1500_2024.process   = "QCD_2024"
QCD_HT1200to1500_2024.unix_code = 31007
QCD_HT1200to1500_2024.EE        = 0
QCD_HT1500to2000_2024           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1500to2000_2024")
QCD_HT1500to2000_2024.sigma     = 125.2 #pb
QCD_HT1500to2000_2024.year      = 2024
QCD_HT1500to2000_2024.dataset   = "/QCD-4Jets_Bin-HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
QCD_HT1500to2000_2024.process   = "QCD_2024"
QCD_HT1500to2000_2024.unix_code = 31008
QCD_HT1500to2000_2024.EE        = 0
QCD_HT2000_2024                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT2000_2024")
QCD_HT2000_2024.sigma           = 26.49 #pb
QCD_HT2000_2024.year            = 2024
QCD_HT2000_2024.dataset         = "/QCD-4Jets_Bin-HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
QCD_HT2000_2024.process         = "QCD_2024"
QCD_HT2000_2024.unix_code       = 31009
QCD_HT2000_2024.EE              = 0
QCD_2024                        = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2024")
QCD_2024.year                   = 2024
QCD_2024.components             = [ 
                                    # QCD_HT40to70_2024, 
                                    QCD_HT70to100_2024, QCD_HT100to200_2024, QCD_HT200to400_2024,
                                    QCD_HT400to600_2024, QCD_HT600to800_2024, QCD_HT800to1000_2024, 
                                    QCD_HT1000to1200_2024, QCD_HT1200to1500_2024,
                                    QCD_HT1500to2000_2024, QCD_HT2000_2024
                                ]


################################ TTbar ################################
TT_semilep_2024             = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2024")
TT_semilep_2024.sigma       = sigma_ttbar_13p6TeV * BR_t_to_bqq_13p6TeV * BR_t_to_blv_13p6TeV * 2 #pb
TT_semilep_2024.year        = 2024
TT_semilep_2024.dataset     = "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TT_semilep_2024.process     = 'TT_2024'
TT_semilep_2024.unix_code   = 31100
TT_semilep_2024.EE          = 0

TT_hadr_2024                = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_hadr_2024")
TT_hadr_2024.sigma          = sigma_ttbar_13p6TeV * BR_t_to_bqq_13p6TeV * BR_t_to_bqq_13p6TeV
TT_hadr_2024.year           = 2024
TT_hadr_2024.dataset        = "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TT_hadr_2024.process        = 'TT_2024'
TT_hadr_2024.unix_code      = 31101
TT_hadr_2024.EE             = 0

TT_dilep_2024               = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_dilep_2024")
TT_dilep_2024.sigma         = sigma_ttbar_13p6TeV * BR_t_to_blv_13p6TeV * BR_t_to_blv_13p6TeV
TT_dilep_2024.year          = 2024
TT_dilep_2024.dataset       = "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"
TT_dilep_2024.process       = 'TT_2024'
TT_dilep_2024.unix_code     = 31102
TT_dilep_2024.EE            = 0

TT_2024                     = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_2024")
TT_2024.year                = 2024
TT_2024.components          = [
                                TT_semilep_2024,
                                TT_hadr_2024,
                                TT_dilep_2024
                                ]


################################ SingleTop ################################
TWminustoLNu2Q_2024             = sample(ROOT.kViolet, 1, 1001, "tW", "TWminustoLNu2Q_2024")
TWminustoLNu2Q_2024.sigma       = sigma_tWminus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_lv_13p6TeV + BR_t_to_blv_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TWminustoLNu2Q_2024.year        = 2024
TWminustoLNu2Q_2024.dataset     = "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWminustoLNu2Q_2024.process     = 'TW_2024'
TWminustoLNu2Q_2024.EE          = 0

TWminusto4Q_2024                = sample(ROOT.kViolet, 1, 1001, "tW", "TWminusto4Q_2024")
TWminusto4Q_2024.sigma          = sigma_tWminus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TWminusto4Q_2024.year           = 2024
TWminusto4Q_2024.dataset        = "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWminusto4Q_2024.process        = 'TW_2024'
TWminusto4Q_2024.EE             = 0

TWminusto2L2Nu_2024             = sample(ROOT.kViolet, 1, 1001, "tW", "TWminusto2L2Nu_2024")
TWminusto2L2Nu_2024.sigma       = sigma_tWminus_13p6TeV * (BR_t_to_blv_13p6TeV * BR_W_to_lv_13p6TeV) #pb
TWminusto2L2Nu_2024.year        = 2024
TWminusto2L2Nu_2024.dataset     = "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWminusto2L2Nu_2024.process     = 'TW_2024'
TWminusto2L2Nu_2024.EE          = 0

TbarWplustoLNu2Q_2024           = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplustoLNu2Q_2024")
TbarWplustoLNu2Q_2024.sigma     = sigma_tbarWplus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_lv_13p6TeV + BR_t_to_blv_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TbarWplustoLNu2Q_2024.year      = 2024
TbarWplustoLNu2Q_2024.dataset   = "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TbarWplustoLNu2Q_2024.process   = 'TW_2024'
TbarWplustoLNu2Q_2024.EE        = 0

TbarWplusto4Q_2024              = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplusto4Q_2024")
TbarWplusto4Q_2024.sigma        = sigma_tbarWplus_13p6TeV * (BR_t_to_bqq_13p6TeV * BR_W_to_qq_13p6TeV) #pb
TbarWplusto4Q_2024.year         = 2024
TbarWplusto4Q_2024.dataset      = "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TbarWplusto4Q_2024.process      = 'TW_2024'
TbarWplusto4Q_2024.EE           = 0

TbarWplusto2L2Nu_2024           = sample(ROOT.kViolet, 1, 1001, "tW", "TbarWplusto2L2Nu_2024")
TbarWplusto2L2Nu_2024.sigma     = sigma_tbarWplus_13p6TeV * (BR_t_to_blv_13p6TeV * BR_W_to_lv_13p6TeV) #pb
TbarWplusto2L2Nu_2024.year      = 2024
TbarWplusto2L2Nu_2024.dataset   = "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TbarWplusto2L2Nu_2024.process   = 'TW_2024'
TbarWplusto2L2Nu_2024.EE        = 0

TW_2024                         = sample(ROOT.kViolet, 1, 1001, "tW", "TW_2024")
TW_2024.year                    = 2024
TW_2024.components              = [
                                    TWminustoLNu2Q_2024,
                                    TWminusto4Q_2024,
                                    TWminusto2L2Nu_2024,
                                    TbarWplustoLNu2Q_2024,
                                    TbarWplusto4Q_2024,
                                    TbarWplusto2L2Nu_2024
                                ]

                            
################################ ZJets ################################
ZJetsToNuNu_HT100to200_2024             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT100to200_2024")
ZJetsToNuNu_HT100to200_2024.sigma       = 273.7 #pb
ZJetsToNuNu_HT100to200_2024.year        = 2024
ZJetsToNuNu_HT100to200_2024.dataset     = "/Zto2Nu-4Jets_Bin-HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"
ZJetsToNuNu_HT100to200_2024.process     = 'ZJetsToNuNu_2024'
ZJetsToNuNu_HT100to200_2024.unix_code   = 31200
ZJetsToNuNu_HT100to200_2024.EE          = 0


ZJetsToNuNu_HT200to400_2024             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT200to400_2024")
ZJetsToNuNu_HT200to400_2024.sigma       = 75.96 #pb
ZJetsToNuNu_HT200to400_2024.year        = 2024
ZJetsToNuNu_HT200to400_2024.dataset     = "/Zto2Nu-4Jets_Bin-HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"
ZJetsToNuNu_HT200to400_2024.process     = 'ZJetsToNuNu_2024'
ZJetsToNuNu_HT200to400_2024.unix_code   = 31201
ZJetsToNuNu_HT200to400_2024.EE          = 0

ZJetsToNuNu_HT400to800_2024             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT400to800_2024")
ZJetsToNuNu_HT400to800_2024.sigma       = 13.19 #pb
ZJetsToNuNu_HT400to800_2024.year        = 2024
ZJetsToNuNu_HT400to800_2024.dataset     = "/Zto2Nu-4Jets_Bin-HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT400to800_2024.process     = 'ZJetsToNuNu_2024'
ZJetsToNuNu_HT400to800_2024.unix_code   = 31202
ZJetsToNuNu_HT400to800_2024.EE          = 0

ZJetsToNuNu_HT800to1500_2024            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT800to1500_2024")
ZJetsToNuNu_HT800to1500_2024.sigma      = 1.364 #pb
ZJetsToNuNu_HT800to1500_2024.year       = 2024
ZJetsToNuNu_HT800to1500_2024.dataset    = "/Zto2Nu-4Jets_Bin-HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT800to1500_2024.process    = 'ZJetsToNuNu_2024'
ZJetsToNuNu_HT800to1500_2024.unix_code  = 31203
ZJetsToNuNu_HT800to1500_2024.EE         = 0

ZJetsToNuNu_HT1500to2500_2024           = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT1500to2500_2024")
ZJetsToNuNu_HT1500to2500_2024.sigma     = 0.09865 #pb
ZJetsToNuNu_HT1500to2500_2024.year      = 2024
ZJetsToNuNu_HT1500to2500_2024.dataset   = "/Zto2Nu-4Jets_Bin-HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT1500to2500_2024.process   = 'ZJetsToNuNu_2024'
ZJetsToNuNu_HT1500to2500_2024.unix_code = 31204
ZJetsToNuNu_HT1500to2500_2024.EE        = 0

ZJetsToNuNu_HT2500_2024                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT2500_2024")
ZJetsToNuNu_HT2500_2024.sigma           = 0.006699 #pb
ZJetsToNuNu_HT2500_2024.year            = 2024
ZJetsToNuNu_HT2500_2024.dataset         = "/Zto2Nu-4Jets_Bin-HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT2500_2024.process         = 'ZJetsToNuNu_2024'
ZJetsToNuNu_HT2500_2024.unix_code       = 31205
ZJetsToNuNu_HT2500_2024.EE              = 0

ZJetsToNuNu_2024                        = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2024")
ZJetsToNuNu_2024.year                   = 2024
ZJetsToNuNu_2024.components             = [
                                            ZJetsToNuNu_HT100to200_2024,
                                            ZJetsToNuNu_HT200to400_2024,
                                            ZJetsToNuNu_HT400to800_2024,
                                            ZJetsToNuNu_HT800to1500_2024,
                                            ZJetsToNuNu_HT1500to2500_2024,
                                            ZJetsToNuNu_HT2500_2024 
                                            ]


ZJetsToNuNu_2jets_PT40to100_1J_2024            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_1J_2024")
ZJetsToNuNu_2jets_PT40to100_1J_2024.sigma      = 929.8	
ZJetsToNuNu_2jets_PT40to100_1J_2024.year       = 2024
ZJetsToNuNu_2jets_PT40to100_1J_2024.dataset    = "/Zto2Nu-2Jets_Bin-1J-PTNuNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_1J_2024.process    = 'ZJetsToNuNu_2jets_2024'
ZJetsToNuNu_2jets_PT40to100_1J_2024.unix_code  = 31206
ZJetsToNuNu_2jets_PT40to100_1J_2024.EE         = 0

ZJetsToNuNu_2jets_PT100to200_1J_2024            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_1J_2024")
ZJetsToNuNu_2jets_PT100to200_1J_2024.sigma      = 86.38
ZJetsToNuNu_2jets_PT100to200_1J_2024.year       = 2024
ZJetsToNuNu_2jets_PT100to200_1J_2024.dataset    = "/Zto2Nu-2Jets_Bin-1J-PTNuNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_1J_2024.process    = 'ZJetsToNuNu_2jets_2024'
ZJetsToNuNu_2jets_PT100to200_1J_2024.unix_code  = 31207
ZJetsToNuNu_2jets_PT100to200_1J_2024.EE         = 0

ZJetsToNuNu_2jets_PT200to400_1J_2024            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_1J_2024")
ZJetsToNuNu_2jets_PT200to400_1J_2024.sigma      = 6.354	
ZJetsToNuNu_2jets_PT200to400_1J_2024.year       = 2024
ZJetsToNuNu_2jets_PT200to400_1J_2024.dataset    = "/Zto2Nu-2Jets_Bin-1J-PTNuNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_1J_2024.process    = 'ZJetsToNuNu_2jets_2024'
ZJetsToNuNu_2jets_PT200to400_1J_2024.unix_code  = 31208
ZJetsToNuNu_2jets_PT200to400_1J_2024.EE         = 0

ZJetsToNuNu_2jets_PT400to600_1J_2024            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_1J_2024")
ZJetsToNuNu_2jets_PT400to600_1J_2024.sigma      = 0.2188
ZJetsToNuNu_2jets_PT400to600_1J_2024.year       = 2024
ZJetsToNuNu_2jets_PT400to600_1J_2024.dataset    = "/Zto2Nu-2Jets_Bin-1J-PTNuNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_1J_2024.process    = 'ZJetsToNuNu_2jets_2024'
ZJetsToNuNu_2jets_PT400to600_1J_2024.unix_code  = 31209
ZJetsToNuNu_2jets_PT400to600_1J_2024.EE         = 0

ZJetsToNuNu_2jets_PT600_1J_2024                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_1J_2024")
ZJetsToNuNu_2jets_PT600_1J_2024.sigma           = 0.02583
ZJetsToNuNu_2jets_PT600_1J_2024.year            = 2024
ZJetsToNuNu_2jets_PT600_1J_2024.dataset         = "/Zto2Nu-2Jets_Bin-1J-PTNuNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_1J_2024.process         = 'ZJetsToNuNu_2jets_2024'
ZJetsToNuNu_2jets_PT600_1J_2024.unix_code       = 31210
ZJetsToNuNu_2jets_PT600_1J_2024.EE              = 0

ZJetsToNuNu_2jets_PT40to100_2J_2024             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_2J_2024")
ZJetsToNuNu_2jets_PT40to100_2J_2024.sigma       = 335.5
ZJetsToNuNu_2jets_PT40to100_2J_2024.year        = 2024
ZJetsToNuNu_2jets_PT40to100_2J_2024.dataset     = "/Zto2Nu-2Jets_Bin-2J-PTNuNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_2J_2024.process     = 'ZJetsToNuNu_2jets_2024'
ZJetsToNuNu_2jets_PT40to100_2J_2024.unix_code   = 31211
ZJetsToNuNu_2jets_PT40to100_2J_2024.EE          = 0

ZJetsToNuNu_2jets_PT100to200_2J_2024            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_2J_2024")
ZJetsToNuNu_2jets_PT100to200_2J_2024.sigma      = 100.4
ZJetsToNuNu_2jets_PT100to200_2J_2024.year       = 2024
ZJetsToNuNu_2jets_PT100to200_2J_2024.dataset    = "/Zto2Nu-2Jets_Bin-2J-PTNuNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_2J_2024.process    = 'ZJetsToNuNu_2jets_2024'
ZJetsToNuNu_2jets_PT100to200_2J_2024.unix_code  = 31212
ZJetsToNuNu_2jets_PT100to200_2J_2024.EE         = 0

ZJetsToNuNu_2jets_PT200to400_2J_2024            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_2J_2024")
ZJetsToNuNu_2jets_PT200to400_2J_2024.sigma      = 13.86
ZJetsToNuNu_2jets_PT200to400_2J_2024.year       = 2024
ZJetsToNuNu_2jets_PT200to400_2J_2024.dataset    = "/Zto2Nu-2Jets_Bin-2J-PTNuNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_2J_2024.process    = 'ZJetsToNuNu_2jets_2024'
ZJetsToNuNu_2jets_PT200to400_2J_2024.unix_code  = 31213
ZJetsToNuNu_2jets_PT200to400_2J_2024.EE         = 0

ZJetsToNuNu_2jets_PT400to600_2J_2024            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_2J_2024")
ZJetsToNuNu_2jets_PT400to600_2J_2024.sigma      = 0.7816
ZJetsToNuNu_2jets_PT400to600_2J_2024.year       = 2024
ZJetsToNuNu_2jets_PT400to600_2J_2024.dataset    = "/Zto2Nu-2Jets_Bin-2J-PTNuNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_2J_2024.process    = 'ZJetsToNuNu_2jets_2024'
ZJetsToNuNu_2jets_PT400to600_2J_2024.unix_code  = 31214
ZJetsToNuNu_2jets_PT400to600_2J_2024.EE         = 0

ZJetsToNuNu_2jets_PT600_2J_2024                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_2J_2024")
ZJetsToNuNu_2jets_PT600_2J_2024.sigma           = 0.1311
ZJetsToNuNu_2jets_PT600_2J_2024.year            = 2024
ZJetsToNuNu_2jets_PT600_2J_2024.dataset         = "/Zto2Nu-2Jets_Bin-2J-PTNuNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_2J_2024.process         = 'ZJetsToNuNu_2jets_2024'
ZJetsToNuNu_2jets_PT600_2J_2024.unix_code       = 31215
ZJetsToNuNu_2jets_PT600_2J_2024.EE              = 0

ZJetsToNuNu_2jets_2024                          = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_2024")
ZJetsToNuNu_2jets_2024.year                     = 2024
ZJetsToNuNu_2jets_2024.components               = [
                                                    ZJetsToNuNu_2jets_PT40to100_1J_2024,
                                                    ZJetsToNuNu_2jets_PT100to200_1J_2024,
                                                    ZJetsToNuNu_2jets_PT200to400_1J_2024,
                                                    ZJetsToNuNu_2jets_PT400to600_1J_2024,
                                                    ZJetsToNuNu_2jets_PT600_1J_2024,
                                                    ZJetsToNuNu_2jets_PT40to100_2J_2024,
                                                    ZJetsToNuNu_2jets_PT100to200_2J_2024,
                                                    ZJetsToNuNu_2jets_PT200to400_2J_2024,
                                                    ZJetsToNuNu_2jets_PT400to600_2J_2024,
                                                    ZJetsToNuNu_2jets_PT600_2J_2024
                                                ]


################################ WJets ################################
WJets_4Jets_1J_2024         = sample(ROOT.kRed -7, 1, 1001, 'W + Jets', 'WJets_4Jets_1J_2024')
WJets_4Jets_1J_2024.dataset = "/WtoLNu-4Jets_Bin-1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_4Jets_1J_2024.sigma   = 9141
WJets_4Jets_1J_2024.year    = 2024
WJets_4Jets_1J_2024.process = 'WJets_4Jets_2024'
WJets_4Jets_1J_2024.EE      = 0

WJets_4Jets_2J_2024         = sample(ROOT.kRed -7, 1, 1001, 'W + Jets', 'WJets_4Jets_2J_2024')
WJets_4Jets_2J_2024.dataset = "/WtoLNu-4Jets_Bin-2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_4Jets_2J_2024.sigma   = 2931
WJets_4Jets_2J_2024.year    = 2024
WJets_4Jets_2J_2024.process = 'WJets_4Jets_2024'
WJets_4Jets_2J_2024.EE      = 0

WJets_4Jets_3J_2024         = sample(ROOT.kRed -7, 1, 1001, 'W + Jets', 'WJets_4Jets_3J_2024')
WJets_4Jets_3J_2024.dataset = "/WtoLNu-4Jets_Bin-3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_4Jets_3J_2024.sigma   = 864.6
WJets_4Jets_3J_2024.year    = 2024
WJets_4Jets_3J_2024.process = 'WJets_4Jets_2024'
WJets_4Jets_3J_2024.EE      = 0

WJets_4Jets_4J_2024          = sample(ROOT.kRed -7, 1, 1001, 'W + Jets', 'WJets_4Jets_4J_2024')
WJets_4Jets_4J_2024.dataset  = "/WtoLNu-4Jets_Bin-4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_4Jets_4J_2024.sigma    = 417.8
WJets_4Jets_4J_2024.year     = 2024
WJets_4Jets_4J_2024.process  = 'WJets_4Jets_2024'
WJets_4Jets_4J_2024.EE       = 0

WJets_4Jets_2024             = sample(ROOT.kRed -7,1,1001, 'W + Jets', 'WJets_4Jets_2024')
WJets_4Jets_2024.year        = 2024
WJets_4Jets_2024.components  = [WJets_4Jets_1J_2024, WJets_4Jets_2J_2024, 
                                WJets_4Jets_3J_2024, WJets_4Jets_4J_2024]


WJets_2jets_ENu_0J_2024            = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_ENu_0J_2024")
WJets_2jets_ENu_0J_2024.sigma      = 55850 * BR_W_to_ev_13p6TeV / BR_W_to_lv_13p6TeV
WJets_2jets_ENu_0J_2024.year       = 2024
WJets_2jets_ENu_0J_2024.dataset    = "/WtoENu-2Jets_Bin-0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_2jets_ENu_0J_2024.process    = "WJets_2jets_2024"
WJets_2jets_ENu_0J_2024.EE         = 0

WJets_2jets_ENu_1J_2024            = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_ENu_1J_2024")
WJets_2jets_ENu_1J_2024.sigma      = 9177 * BR_W_to_ev_13p6TeV / BR_W_to_lv_13p6TeV
WJets_2jets_ENu_1J_2024.year       = 2024
WJets_2jets_ENu_1J_2024.dataset    = "/WtoENu-2Jets_Bin-1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_2jets_ENu_1J_2024.process    = "WJets_2jets_2024"
WJets_2jets_ENu_1J_2024.EE         = 0

WJets_2jets_ENu_2J_2024            = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_ENu_2J_2024")
WJets_2jets_ENu_2J_2024.sigma      = 3474 * BR_W_to_ev_13p6TeV / BR_W_to_lv_13p6TeV
WJets_2jets_ENu_2J_2024.year       = 2024
WJets_2jets_ENu_2J_2024.dataset    = "/WtoENu-2Jets_Bin-2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_2jets_ENu_2J_2024.process    = "WJets_2jets_2024"
WJets_2jets_ENu_2J_2024.EE         = 0

WJets_2jets_MuNu_0J_2024           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_MuNu_0J_2024")
WJets_2jets_MuNu_0J_2024.sigma     = 55920 * BR_W_to_muv_13p6TeV / BR_W_to_lv_13p6TeV
WJets_2jets_MuNu_0J_2024.year      = 2024
WJets_2jets_MuNu_0J_2024.dataset   = "/WtoMuNu-2Jets_Bin-0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_2jets_MuNu_0J_2024.process   = "WJets_2jets_2024"
WJets_2jets_MuNu_0J_2024.EE        = 0

WJets_2jets_MuNu_1J_2024           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_MuNu_1J_2024")
WJets_2jets_MuNu_1J_2024.sigma     = 9202 * BR_W_to_muv_13p6TeV / BR_W_to_lv_13p6TeV
WJets_2jets_MuNu_1J_2024.year      = 2024
WJets_2jets_MuNu_1J_2024.dataset   = "/WtoMuNu-2Jets_Bin-1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_2jets_MuNu_1J_2024.process   = "WJets_2jets_2024"
WJets_2jets_MuNu_1J_2024.EE        = 0

WJets_2jets_MuNu_2J_2024           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_MuNu_2J_2024")
WJets_2jets_MuNu_2J_2024.sigma     = 3490 * BR_W_to_muv_13p6TeV / BR_W_to_lv_13p6TeV
WJets_2jets_MuNu_2J_2024.year      = 2024
WJets_2jets_MuNu_2J_2024.dataset   = "/WtoMuNu-2Jets_Bin-2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_2jets_MuNu_2J_2024.process   = "WJets_2jets_2024"
WJets_2jets_MuNu_2J_2024.EE        = 0

WJets_2jets_TauNu_0J_2024          = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_TauNu_0J_2024")
WJets_2jets_TauNu_0J_2024.sigma    = 55890 * BR_W_to_tauv_13p6TeV / BR_W_to_lv_13p6TeV
WJets_2jets_TauNu_0J_2024.year     = 2024
WJets_2jets_TauNu_0J_2024.dataset  = "/WtoTauNu-2Jets_Bin-0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_2jets_TauNu_0J_2024.process  = "WJets_2jets_2024"
WJets_2jets_TauNu_0J_2024.EE       = 0

WJets_2jets_TauNu_1J_2024          = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_TauNu_1J_2024")
WJets_2jets_TauNu_1J_2024.sigma    = 9280 * BR_W_to_tauv_13p6TeV / BR_W_to_lv_13p6TeV
WJets_2jets_TauNu_1J_2024.year     = 2024
WJets_2jets_TauNu_1J_2024.dataset  = "/WtoTauNu-2Jets_Bin-1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_2jets_TauNu_1J_2024.process  = "WJets_2jets_2024"
WJets_2jets_TauNu_1J_2024.EE       = 0

WJets_2jets_TauNu_2J_2024          = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_TauNu_2J_2024")
WJets_2jets_TauNu_2J_2024.sigma    = 3470 * BR_W_to_tauv_13p6TeV / BR_W_to_lv_13p6TeV
WJets_2jets_TauNu_2J_2024.year     = 2024
WJets_2jets_TauNu_2J_2024.dataset  = "/WtoTauNu-2Jets_Bin-2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
WJets_2jets_TauNu_2J_2024.process  = "WJets_2jets_2024"
WJets_2jets_TauNu_2J_2024.EE       = 0

WJets_2jets_2024                          = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_2024")
WJets_2jets_2024.year                     = 2024
WJets_2jets_2024.components               = [
                                                WJets_2jets_ENu_0J_2024,
                                                WJets_2jets_ENu_1J_2024,
                                                WJets_2jets_ENu_2J_2024,
                                                WJets_2jets_MuNu_0J_2024,
                                                WJets_2jets_MuNu_1J_2024,
                                                WJets_2jets_MuNu_2J_2024,
                                                WJets_2jets_TauNu_0J_2024,
                                                WJets_2jets_TauNu_1J_2024,
                                                WJets_2jets_TauNu_2J_2024
                                                ]


###############################################################################################################################
########################### DATA 2018 ############################################
###############################################################################################################################
DataMETA_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETA_2018")
DataMETA_2018.runP      = 'A'
DataMETA_2018.year      = 2018
DataMETA_2018.dataset   = '/MET/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD' #'/MET/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataMETA_2018.process   = "DataMET_2018"
DataMETA_2018.unix_code = 20000
DataMETB_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETB_2018")
DataMETB_2018.runP      = 'B'
DataMETB_2018.year      = 2018
DataMETB_2018.dataset   = '/MET/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD' #'/MET/Run2018B-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataMETB_2018.process   = "DataMET_2018"
DataMETB_2018.unix_code = 20001
DataMETC_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETC_2018")
DataMETC_2018.runP      = 'C'
DataMETC_2018.year      = 2018
DataMETC_2018.dataset   = '/MET/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'#'/MET/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataMETC_2018.process   = "DataMET_2018"
DataMETC_2018.unix_code = 20002
DataMETD_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETD_2018")
DataMETD_2018.runP      = 'D'
DataMETD_2018.year      = 2018
DataMETD_2018.dataset   = '/MET/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'#'/MET/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataMETD_2018.process   = "DataMET_2018"
DataMETD_2018.unix_code = 20003

DataMET_2018            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMET_2018")
DataMET_2018.year       = 2018
DataMET_2018.components = [DataMETA_2018, DataMETB_2018, 
                          DataMETC_2018, DataMETD_2018
                          ]

DataSingleMuA_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataSingleMuA_2018")
DataSingleMuA_2018.runP      = 'A'
DataSingleMuA_2018.year      = 2018
DataSingleMuA_2018.dataset   = '/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'
DataSingleMuA_2018.process   = "DataSingleMu_2018"
DataSingleMuA_2018.unix_code = 20100
DataSingleMuB_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataSingleMuB_2018")
DataSingleMuB_2018.runP      = 'B'
DataSingleMuB_2018.year      = 2018
DataSingleMuB_2018.dataset   = '/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'
DataSingleMuB_2018.process   = "DataSingleMu_2018"
DataSingleMuB_2018.unix_code = 20101
DataSingleMuC_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataSingleMuC_2018")
DataSingleMuC_2018.runP      = 'C'
DataSingleMuC_2018.year      = 2018
DataSingleMuC_2018.dataset   = '/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'
DataSingleMuC_2018.process   = "DataSingleMu_2018"
DataSingleMuC_2018.unix_code = 20102
DataSingleMuD_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataSingleMuD_2018")
DataSingleMuD_2018.runP      = 'D'
DataSingleMuD_2018.year      = 2018
DataSingleMuD_2018.dataset   = '/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'
DataSingleMuD_2018.process   = "DataSingleMu_2018"
DataSingleMuD_2018.unix_code = 20103

DataSingleMu_2018            = sample(ROOT.kBlack, 1, 1001, "Data", "DataSingleMu_2018")
DataSingleMu_2018.year       = 2018
DataSingleMu_2018.components = [DataSingleMuA_2018, DataSingleMuB_2018, 
                                DataSingleMuC_2018, DataSingleMuD_2018
                               ]


# DataMETA_2018          = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETA_2018")
# DataMETA_2018.runP     = 'A'
# DataMETA_2018.year     = 2018
# DataMETA_2018.dataset  = '/MET/Run2018A-02Apr2020-v1/NANOAOD' #ReRECO 2018 A

########################### DATA 2022 ############################################

DataJetMETC_2022            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC_2022")
DataJetMETC_2022.runP       = 'C'
DataJetMETC_2022.year       = 2022
DataJetMETC_2022.dataset    = '/JetMET/Run2022C-22Sep2023-v1/NANOAOD' #/JetMET/Run2022C-JMENano12p5-v1/NANOAOD da capire quale vogliono che usiamo
DataJetMETC_2022.process    = "DataJetMET_2022"
DataJetMETC_2022.unix_code  = 30000
DataJetMETC_2022.EE         = 0
DataJetMETD_2022            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETD_2022")
DataJetMETD_2022.runP       = 'D'
DataJetMETD_2022.year       = 2022
DataJetMETD_2022.dataset    = '/JetMET/Run2022D-22Sep2023-v1/NANOAOD'
DataJetMETD_2022.process    = "DataJetMET_2022"
DataJetMETD_2022.unix_code  = 30001
DataJetMETD_2022.EE         = 0
DataJetMET_2022             = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMET_2022")
DataJetMET_2022.year        = 2022
DataJetMET_2022.components  = [DataJetMETC_2022, DataJetMETD_2022]

DataJetMETE_2022EE            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETE_2022EE")
DataJetMETE_2022EE.runP       = 'E'
DataJetMETE_2022EE.year       = 2022
DataJetMETE_2022EE.dataset    = '/JetMET/Run2022E-22Sep2023-v1/NANOAOD'
DataJetMETE_2022EE.process    = "DataJetMET_2022EE"
DataJetMETE_2022EE.unix_code  = 30002
DataJetMETE_2022EE.EE         = 1
DataJetMETF_2022EE            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETF_2022EE")
DataJetMETF_2022EE.runP       = 'F'
DataJetMETF_2022EE.year       = 2022
DataJetMETF_2022EE.dataset    = '/JetMET/Run2022F-22Sep2023-v2/NANOAOD'
DataJetMETF_2022EE.process    = "DataJetMET_2022EE"
DataJetMETF_2022EE.unix_code  = 30003
DataJetMETF_2022EE.EE         = 1
DataJetMETG_2022EE            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETG_2022EE")
DataJetMETG_2022EE.runP       = 'G'
DataJetMETG_2022EE.year       = 2022
DataJetMETG_2022EE.dataset    = '/JetMET/Run2022G-22Sep2023-v2/NANOAOD'
DataJetMETG_2022EE.process    = "DataJetMET_2022EE"
DataJetMETG_2022EE.unix_code  = 30004
DataJetMETG_2022EE.EE         = 1
DataJetMET_2022EE             = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMET_2022EE")
DataJetMET_2022EE.year        = 2022
DataJetMET_2022EE.components  = [DataJetMETE_2022EE, DataJetMETF_2022EE, DataJetMETG_2022EE]

DataMuonC_2022              = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonC_2022")
DataMuonC_2022.runP         = 'C'
DataMuonC_2022.year         = 2022
DataMuonC_2022.dataset      = '/Muon/Run2022C-22Sep2023-v1/NANOAOD'
DataMuonC_2022.process     = "DataMuon_2022"
DataMuonC_2022.unix_code    = 30100
DataMuonC_2022.EE           = 0
DataMuonD_2022              = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonD_2022")
DataMuonD_2022.runP         = 'D'
DataMuonD_2022.year         = 2022
DataMuonD_2022.dataset      = '/Muon/Run2022D-22Sep2023-v1/NANOAOD'
DataMuonD_2022.process     = "DataMuon_2022"
DataMuonD_2022.unix_code    = 30101
DataMuonD_2022.EE           = 0
DataMuon_2022               = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuon_2022")
DataMuon_2022.year          = 2022
DataMuon_2022.components    = [DataMuonC_2022, DataMuonD_2022]

DataMuonE_2022EE              = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonE_2022EE")
DataMuonE_2022EE.runP         = 'E'
DataMuonE_2022EE.year         = 2022
DataMuonE_2022EE.dataset      = '/Muon/Run2022E-22Sep2023-v1/NANOAOD'
DataMuonE_2022EE.process     = "DataMuon_2022EE"
DataMuonE_2022EE.unix_code    = 30102
DataMuonE_2022EE.EE           = 1
DataMuonF_2022EE              = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonF_2022EE")
DataMuonF_2022EE.runP         = 'F'
DataMuonF_2022EE.year         = 2022
DataMuonF_2022EE.dataset      = '/Muon/Run2022F-22Sep2023-v2/NANOAOD'
DataMuonF_2022EE.process     = "DataMuon_2022EE"
DataMuonF_2022EE.unix_code    = 30103
DataMuonF_2022EE.EE           = 1
DataMuonG_2022EE              = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonG_2022EE")
DataMuonG_2022EE.runP         = 'G'
DataMuonG_2022EE.year         = 2022
DataMuonG_2022EE.dataset      = '/Muon/Run2022G-22Sep2023-v1/NANOAOD'
DataMuonG_2022EE.process     = "DataMuon_2022EE"
DataMuonG_2022EE.unix_code    = 30104
DataMuonG_2022EE.EE           = 1
DataMuon_2022EE               = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuon_2022EE")
DataMuon_2022EE.year          = 2022
DataMuon_2022EE.components    = [DataMuonE_2022EE, DataMuonF_2022EE, DataMuonG_2022EE]

DataEGammaC_2022              = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaC_2022")
DataEGammaC_2022.year         = 2022
DataEGammaC_2022.dataset      = "/EGamma/Run2022C-22Sep2023-v1/NANOAOD"
DataEGammaC_2022.process     = "DataEGamma_2022"
DataEGammaC_2022.runP         = 'C'
DataEGammaC_2022.unix_code    = 30200
DataEGammaC_2022.EE           = 0
DataEGammaD_2022              = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaD_2022")
DataEGammaD_2022.year         = 2022
DataEGammaD_2022.dataset      = "/EGamma/Run2022D-22Sep2023-v1/NANOAOD"
DataEGammaD_2022.process     = "DataEGamma_2022"
DataEGammaD_2022.runP         = 'C'
DataEGammaD_2022.unix_code    = 30201
DataEGammaD_2022.EE           = 0
DataEGamma_2022               = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGamma_2022")
DataEGamma_2022.year          = 2022
DataEGamma_2022.components    = [DataEGammaC_2022, DataEGammaD_2022]

DataEGammaE_2022EE              = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaE_2022EE")
DataEGammaE_2022EE.year         = 2022
DataEGammaE_2022EE.dataset      = "/EGamma/Run2022E-22Sep2023-v1/NANOAOD"
DataEGammaE_2022EE.process     = "DataEGamma_2022EE"
DataEGammaE_2022EE.runP         = 'E'
DataEGammaE_2022EE.unix_code    = 30202
DataEGammaE_2022EE.EE           = 1
DataEGammaF_2022EE              = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaF_2022EE")
DataEGammaF_2022EE.year         = 2022
DataEGammaF_2022EE.dataset      = "/EGamma/Run2022F-22Sep2023-v1/NANOAOD"
DataEGammaF_2022EE.process     = "DataEGamma_2022EE"
DataEGammaF_2022EE.runP         = 'F'
DataEGammaF_2022EE.unix_code    = 30203
DataEGammaF_2022EE.EE           = 1
DataEGammaG_2022EE              = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaG_2022EE")
DataEGammaG_2022EE.year         = 2022
DataEGammaG_2022EE.dataset      = "/EGamma/Run2022G-22Sep2023-v2/NANOAOD"
DataEGammaG_2022EE.process     = "DataEGamma_2022EE"
DataEGammaG_2022EE.runP         = 'G'
DataEGammaG_2022EE.unix_code    = 30204
DataEGammaG_2022EE.EE           = 1

DataEGamma_2022EE               = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGamma_2022EE")
DataEGamma_2022EE.year          = 2022
DataEGamma_2022EE.components    = [DataEGammaE_2022EE, DataEGammaF_2022EE, DataEGammaG_2022EE]


########################### DATA 2023 ############################################
DataJetMETC1_0_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC1_0_2023")
DataJetMETC1_0_2023.runP       = 'C1'
DataJetMETC1_0_2023.year       = 2023
DataJetMETC1_0_2023.dataset    = '/JetMET0/Run2023C-22Sep2023_v1-v1/NANOAOD'
DataJetMETC1_0_2023.process    = "DataJetMET_2023"
DataJetMETC1_0_2023.unix_code  = 30000
DataJetMETC1_0_2023.EE         = 0
DataJetMETC1_1_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC1_1_2023")
DataJetMETC1_1_2023.runP       = 'C1'
DataJetMETC1_1_2023.year       = 2023
DataJetMETC1_1_2023.dataset    = '/JetMET1/Run2023C-22Sep2023_v1-v1/NANOAOD'
DataJetMETC1_1_2023.process    = "DataJetMET_2023"
DataJetMETC1_1_2023.unix_code  = 30000
DataJetMETC1_1_2023.EE         = 0
DataJetMETC2_0_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC2_0_2023")
DataJetMETC2_0_2023.runP       = 'C2'
DataJetMETC2_0_2023.year       = 2023
DataJetMETC2_0_2023.dataset    = '/JetMET0/Run2023C-22Sep2023_v2-v1/NANOAOD'
DataJetMETC2_0_2023.process    = "DataJetMET_2023"
DataJetMETC2_0_2023.unix_code  = 30000
DataJetMETC2_0_2023.EE         = 0
DataJetMETC2_1_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC2_1_2023")
DataJetMETC2_1_2023.runP       = 'C2'
DataJetMETC2_1_2023.year       = 2023
DataJetMETC2_1_2023.dataset    = '/JetMET1/Run2023C-22Sep2023_v2-v1/NANOAOD'
DataJetMETC2_1_2023.process    = "DataJetMET_2023"
DataJetMETC2_1_2023.unix_code  = 30000
DataJetMETC2_1_2023.EE         = 0
DataJetMETC3_0_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC3_0_2023")
DataJetMETC3_0_2023.runP       = 'C3'
DataJetMETC3_0_2023.year       = 2023
DataJetMETC3_0_2023.dataset    = '/JetMET0/Run2023C-22Sep2023_v3-v1/NANOAOD'
DataJetMETC3_0_2023.process    = "DataJetMET_2023"
DataJetMETC3_0_2023.unix_code  = 30000
DataJetMETC3_0_2023.EE         = 0
DataJetMETC3_1_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC3_1_2023")
DataJetMETC3_1_2023.runP       = 'C3'
DataJetMETC3_1_2023.year       = 2023
DataJetMETC3_1_2023.dataset    = '/JetMET1/Run2023C-22Sep2023_v3-v1/NANOAOD'
DataJetMETC3_1_2023.process    = "DataJetMET_2023"
DataJetMETC3_1_2023.unix_code  = 30000
DataJetMETC3_1_2023.EE         = 0
DataJetMETC4_0_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC4_0_2023")
DataJetMETC4_0_2023.runP       = 'C4'
DataJetMETC4_0_2023.year       = 2023
DataJetMETC4_0_2023.dataset    = '/JetMET0/Run2023C-22Sep2023_v4-v1/NANOAOD'
DataJetMETC4_0_2023.process    = "DataJetMET_2023"
DataJetMETC4_0_2023.unix_code  = 30000
DataJetMETC4_0_2023.EE         = 0
DataJetMETC4_1_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC4_1_2023")
DataJetMETC4_1_2023.runP       = 'C4'
DataJetMETC4_1_2023.year       = 2023
DataJetMETC4_1_2023.dataset    = '/JetMET1/Run2023C-22Sep2023_v4-v1/NANOAOD'
DataJetMETC4_1_2023.process    = "DataJetMET_2023"
DataJetMETC4_1_2023.unix_code  = 30000
DataJetMETC4_1_2023.EE         = 0

DataJetMET_2023                = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMET_2023")
DataJetMET_2023.year           = 2023
DataJetMET_2023.components     = [DataJetMETC1_0_2023, DataJetMETC1_1_2023,
                                   DataJetMETC2_0_2023, DataJetMETC2_1_2023,
                                   DataJetMETC3_0_2023, DataJetMETC3_1_2023,
                                   DataJetMETC4_0_2023, DataJetMETC4_1_2023,
                                  ]

DataJetMETD1_0_2023postBPix            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETD1_0_2023postBPix")
DataJetMETD1_0_2023postBPix.runP       = 'D'
DataJetMETD1_0_2023postBPix.year       = 2023
DataJetMETD1_0_2023postBPix.dataset    = '/JetMET0/Run2023D-22Sep2023_v1-v1/NANOAOD'
DataJetMETD1_0_2023postBPix.process    = "DataJetMET_2023postBPix"
DataJetMETD1_0_2023postBPix.unix_code  = 30000
DataJetMETD1_0_2023postBPix.EE         = 1
DataJetMETD1_1_2023postBPix            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETD1_1_2023postBPix")
DataJetMETD1_1_2023postBPix.runP       = 'D'
DataJetMETD1_1_2023postBPix.year       = 2023
DataJetMETD1_1_2023postBPix.dataset    = '/JetMET1/Run2023D-22Sep2023_v1-v1/NANOAOD'
DataJetMETD1_1_2023postBPix.process    = "DataJetMET_2023postBPix"
DataJetMETD1_1_2023postBPix.unix_code  = 30000
DataJetMETD1_1_2023postBPix.EE         = 1
DataJetMETD2_0_2023postBPix            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETD2_0_2023postBPix")
DataJetMETD2_0_2023postBPix.runP       = 'D'
DataJetMETD2_0_2023postBPix.year       = 2023
DataJetMETD2_0_2023postBPix.dataset    = '/JetMET0/Run2023D-22Sep2023_v2-v1/NANOAOD'
DataJetMETD2_0_2023postBPix.process    = "DataJetMET_2023postBPix"
DataJetMETD2_0_2023postBPix.unix_code  = 30000
DataJetMETD2_0_2023postBPix.EE         = 1
DataJetMETD2_1_2023postBPix            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETD2_1_2023postBPix")
DataJetMETD2_1_2023postBPix.runP       = 'D'
DataJetMETD2_1_2023postBPix.year       = 2023
DataJetMETD2_1_2023postBPix.dataset    = '/JetMET1/Run2023D-22Sep2023_v2-v1/NANOAOD'
DataJetMETD2_1_2023postBPix.process    = "DataJetMET_2023postBPix"
DataJetMETD2_1_2023postBPix.unix_code  = 30000
DataJetMETD2_1_2023postBPix.EE         = 1

DataJetMET_2023postBPix                = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMET_2023postBPix")
DataJetMET_2023postBPix.year           = 2023
DataJetMET_2023postBPix.components     = [DataJetMETD1_0_2023postBPix, DataJetMETD1_1_2023postBPix,
                                          DataJetMETD2_0_2023postBPix, DataJetMETD2_1_2023postBPix,
                                          ]



DataMuonC1_0_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonC1_0_2023")
DataMuonC1_0_2023.runP       = 'C1'
DataMuonC1_0_2023.year       = 2023
DataMuonC1_0_2023.dataset    = '/Muon0/Run2023C-22Sep2023_v1-v1/NANOAOD'
DataMuonC1_0_2023.process    = "DataMuon_2023"
DataMuonC1_0_2023.unix_code  = 30000
DataMuonC1_0_2023.EE         = 0
DataMuonC1_1_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonC1_1_2023")
DataMuonC1_1_2023.runP       = 'C1'
DataMuonC1_1_2023.year       = 2023
DataMuonC1_1_2023.dataset    = '/Muon1/Run2023C-22Sep2023_v1-v1/NANOAOD'
DataMuonC1_1_2023.process    = "DataMuon_2023"
DataMuonC1_1_2023.unix_code  = 30000
DataMuonC1_1_2023.EE         = 0
DataMuonC2_0_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonC2_0_2023")
DataMuonC2_0_2023.runP       = 'C2'
DataMuonC2_0_2023.year       = 2023
DataMuonC2_0_2023.dataset    = '/Muon0/Run2023C-22Sep2023_v2-v1/NANOAOD'
DataMuonC2_0_2023.process    = "DataMuon_2023"
DataMuonC2_0_2023.unix_code  = 30000
DataMuonC2_0_2023.EE         = 0
DataMuonC2_1_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonC2_1_2023")
DataMuonC2_1_2023.runP       = 'C2'
DataMuonC2_1_2023.year       = 2023
DataMuonC2_1_2023.dataset    = '/Muon1/Run2023C-22Sep2023_v2-v1/NANOAOD'
DataMuonC2_1_2023.process    = "DataMuon_2023"
DataMuonC2_1_2023.unix_code  = 30000
DataMuonC2_1_2023.EE         = 0
DataMuonC3_0_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonC3_0_2023")
DataMuonC3_0_2023.runP       = 'C3'
DataMuonC3_0_2023.year       = 2023
DataMuonC3_0_2023.dataset    = '/Muon0/Run2023C-22Sep2023_v3-v1/NANOAOD'
DataMuonC3_0_2023.process    = "DataMuon_2023"
DataMuonC3_0_2023.unix_code  = 30000
DataMuonC3_0_2023.EE         = 0
DataMuonC3_1_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonC3_1_2023")
DataMuonC3_1_2023.runP       = 'C3'
DataMuonC3_1_2023.year       = 2023
DataMuonC3_1_2023.dataset    = '/Muon1/Run2023C-22Sep2023_v3-v1/NANOAOD'
DataMuonC3_1_2023.process    = "DataMuon_2023"
DataMuonC3_1_2023.unix_code  = 30000
DataMuonC3_1_2023.EE         = 0
DataMuonC4_0_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonC4_0_2023")
DataMuonC4_0_2023.runP       = 'C4'
DataMuonC4_0_2023.year       = 2023
DataMuonC4_0_2023.dataset    = '/Muon0/Run2023C-22Sep2023_v4-v1/NANOAOD'
DataMuonC4_0_2023.process    = "DataMuon_2023"
DataMuonC4_0_2023.unix_code  = 30000
DataMuonC4_0_2023.EE         = 0
DataMuonC4_1_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonC4_1_2023")
DataMuonC4_1_2023.runP       = 'C4'
DataMuonC4_1_2023.year       = 2023
DataMuonC4_1_2023.dataset    = '/Muon1/Run2023C-22Sep2023_v4-v2/NANOAOD'
DataMuonC4_1_2023.process    = "DataMuon_2023"
DataMuonC4_1_2023.unix_code  = 30000
DataMuonC4_1_2023.EE         = 0

DataMuon_2023                = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuon_2023")
DataMuon_2023.year           = 2023
DataMuon_2023.components     = [DataMuonC1_0_2023, DataMuonC1_1_2023,
                                   DataMuonC2_0_2023, DataMuonC2_1_2023,
                                   DataMuonC3_0_2023, DataMuonC3_1_2023,
                                   DataMuonC4_0_2023, DataMuonC4_1_2023
                                  ]

DataMuonD1_0_2023postBPix            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonD1_0_2023postBPix")
DataMuonD1_0_2023postBPix.runP       = 'D'
DataMuonD1_0_2023postBPix.year       = 2023
DataMuonD1_0_2023postBPix.dataset    = '/Muon0/Run2023D-22Sep2023_v1-v1/NANOAOD'
DataMuonD1_0_2023postBPix.process    = "DataMuon_2023postBPix"
DataMuonD1_0_2023postBPix.unix_code  = 30000
DataMuonD1_0_2023postBPix.EE         = 1
DataMuonD1_1_2023postBPix            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonD1_1_2023postBPix")
DataMuonD1_1_2023postBPix.runP       = 'D'
DataMuonD1_1_2023postBPix.year       = 2023
DataMuonD1_1_2023postBPix.dataset    = '/Muon1/Run2023D-22Sep2023_v1-v1/NANOAOD'
DataMuonD1_1_2023postBPix.process    = "DataMuon_2023postBPix"
DataMuonD1_1_2023postBPix.unix_code  = 30000
DataMuonD1_1_2023postBPix.EE         = 1
DataMuonD2_0_2023postBPix            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonD2_0_2023postBPix")
DataMuonD2_0_2023postBPix.runP       = 'D'
DataMuonD2_0_2023postBPix.year       = 2023
DataMuonD2_0_2023postBPix.dataset    = '/Muon0/Run2023D-22Sep2023_v2-v1/NANOAOD'
DataMuonD2_0_2023postBPix.process    = "DataMuon_2023postBPix"
DataMuonD2_0_2023postBPix.unix_code  = 30000
DataMuonD2_0_2023postBPix.EE         = 1
DataMuonD2_1_2023postBPix            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonD2_1_2023postBPix")
DataMuonD2_1_2023postBPix.runP       = 'D'
DataMuonD2_1_2023postBPix.year       = 2023
DataMuonD2_1_2023postBPix.dataset    = '/Muon1/Run2023D-22Sep2023_v2-v1/NANOAOD'
DataMuonD2_1_2023postBPix.process    = "DataMuon_2023postBPix"
DataMuonD2_1_2023postBPix.unix_code  = 30000
DataMuonD2_1_2023postBPix.EE         = 1

DataMuon_2023postBPix                = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuon_2023postBPix")
DataMuon_2023postBPix.year           = 2023
DataMuon_2023postBPix.components     = [DataMuonD1_0_2023postBPix, DataMuonD1_1_2023postBPix,
                                          DataMuonD2_0_2023postBPix, DataMuonD2_1_2023postBPix,
                                          ]



DataEGammaC1_0_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaC1_0_2023")
DataEGammaC1_0_2023.runP       = 'C1'
DataEGammaC1_0_2023.year       = 2023
DataEGammaC1_0_2023.dataset    = '/EGamma0/Run2023C-22Sep2023_v1-v1/NANOAOD'
DataEGammaC1_0_2023.process    = "DataEGamma_2023"
DataEGammaC1_0_2023.unix_code  = 30000
DataEGammaC1_0_2023.EE         = 0
DataEGammaC1_1_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaC1_1_2023")
DataEGammaC1_1_2023.runP       = 'C1'
DataEGammaC1_1_2023.year       = 2023
DataEGammaC1_1_2023.dataset    = '/EGamma1/Run2023C-22Sep2023_v1-v1/NANOAOD'
DataEGammaC1_1_2023.process    = "DataEGamma_2023"
DataEGammaC1_1_2023.unix_code  = 30000
DataEGammaC1_1_2023.EE         = 0
DataEGammaC2_0_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaC2_0_2023")
DataEGammaC2_0_2023.runP       = 'C2'
DataEGammaC2_0_2023.year       = 2023
DataEGammaC2_0_2023.dataset    = '/EGamma0/Run2023C-22Sep2023_v2-v1/NANOAOD'
DataEGammaC2_0_2023.process    = "DataEGamma_2023"
DataEGammaC2_0_2023.unix_code  = 30000
DataEGammaC2_0_2023.EE         = 0
DataEGammaC2_1_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaC2_1_2023")
DataEGammaC2_1_2023.runP       = 'C2'
DataEGammaC2_1_2023.year       = 2023
DataEGammaC2_1_2023.dataset    = '/EGamma1/Run2023C-22Sep2023_v2-v1/NANOAOD'
DataEGammaC2_1_2023.process    = "DataEGamma_2023"
DataEGammaC2_1_2023.unix_code  = 30000
DataEGammaC2_1_2023.EE         = 0
DataEGammaC3_0_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaC3_0_2023")
DataEGammaC3_0_2023.runP       = 'C3'
DataEGammaC3_0_2023.year       = 2023
DataEGammaC3_0_2023.dataset    = '/EGamma0/Run2023C-22Sep2023_v3-v1/NANOAOD'
DataEGammaC3_0_2023.process    = "DataEGamma_2023"
DataEGammaC3_0_2023.unix_code  = 30000
DataEGammaC3_0_2023.EE         = 0
DataEGammaC3_1_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaC3_1_2023")
DataEGammaC3_1_2023.runP       = 'C3'
DataEGammaC3_1_2023.year       = 2023
DataEGammaC3_1_2023.dataset    = '/EGamma1/Run2023C-22Sep2023_v3-v1/NANOAOD'
DataEGammaC3_1_2023.process    = "DataEGamma_2023"
DataEGammaC3_1_2023.unix_code  = 30000
DataEGammaC3_1_2023.EE         = 0
DataEGammaC4_0_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaC4_0_2023")
DataEGammaC4_0_2023.runP       = 'C4'
DataEGammaC4_0_2023.year       = 2023
DataEGammaC4_0_2023.dataset    = '/EGamma0/Run2023C-22Sep2023_v4-v1/NANOAOD'
DataEGammaC4_0_2023.process    = "DataEGamma_2023"
DataEGammaC4_0_2023.unix_code  = 30000
DataEGammaC4_0_2023.EE         = 0
DataEGammaC4_1_2023            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaC4_1_2023")
DataEGammaC4_1_2023.runP       = 'C4'
DataEGammaC4_1_2023.year       = 2023
DataEGammaC4_1_2023.dataset    = '/EGamma1/Run2023C-22Sep2023_v4-v1/NANOAOD'
DataEGammaC4_1_2023.process    = "DataEGamma_2023"
DataEGammaC4_1_2023.unix_code  = 30000
DataEGammaC4_1_2023.EE         = 0

DataEGamma_2023                = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGamma_2023")
DataEGamma_2023.year           = 2023
DataEGamma_2023.components     = [DataEGammaC1_0_2023, DataEGammaC1_1_2023,
                                   DataEGammaC2_0_2023, DataEGammaC2_1_2023,
                                   DataEGammaC3_0_2023, DataEGammaC3_1_2023,
                                   DataEGammaC4_0_2023, DataEGammaC4_1_2023
                                  ]

DataEGammaD1_0_2023postBPix            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaD1_0_2023postBPix")
DataEGammaD1_0_2023postBPix.runP       = 'D'
DataEGammaD1_0_2023postBPix.year       = 2023
DataEGammaD1_0_2023postBPix.dataset    = '/EGamma0/Run2023D-22Sep2023_v1-v1/NANOAOD'
DataEGammaD1_0_2023postBPix.process    = "DataEGamma_2023postBPix"
DataEGammaD1_0_2023postBPix.unix_code  = 30000
DataEGammaD1_0_2023postBPix.EE         = 1
DataEGammaD1_1_2023postBPix            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaD1_1_2023postBPix")
DataEGammaD1_1_2023postBPix.runP       = 'D'
DataEGammaD1_1_2023postBPix.year       = 2023
DataEGammaD1_1_2023postBPix.dataset    = '/EGamma1/Run2023D-22Sep2023_v1-v1/NANOAOD'
DataEGammaD1_1_2023postBPix.process    = "DataEGamma_2023postBPix"
DataEGammaD1_1_2023postBPix.unix_code  = 30000
DataEGammaD1_1_2023postBPix.EE         = 1
DataEGammaD2_0_2023postBPix            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaD2_0_2023postBPix")
DataEGammaD2_0_2023postBPix.runP       = 'D'
DataEGammaD2_0_2023postBPix.year       = 2023
DataEGammaD2_0_2023postBPix.dataset    = '/EGamma0/Run2023D-22Sep2023_v2-v1/NANOAOD'
DataEGammaD2_0_2023postBPix.process    = "DataEGamma_2023postBPix"
DataEGammaD2_0_2023postBPix.unix_code  = 30000
DataEGammaD2_0_2023postBPix.EE         = 1
DataEGammaD2_1_2023postBPix            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaD2_1_2023postBPix")
DataEGammaD2_1_2023postBPix.runP       = 'D'
DataEGammaD2_1_2023postBPix.year       = 2023
DataEGammaD2_1_2023postBPix.dataset    = '/EGamma1/Run2023D-22Sep2023_v2-v1/NANOAOD'
DataEGammaD2_1_2023postBPix.process    = "DataEGamma_2023postBPix"
DataEGammaD2_1_2023postBPix.unix_code  = 30000
DataEGammaD2_1_2023postBPix.EE         = 1

DataEGamma_2023postBPix                = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGamma_2023postBPix")
DataEGamma_2023postBPix.year           = 2023
DataEGamma_2023postBPix.components     = [DataEGammaD1_0_2023postBPix, DataEGammaD1_1_2023postBPix,
                                          DataEGammaD2_0_2023postBPix, DataEGammaD2_1_2023postBPix,
                                          ]


########################### DATA 2024 ############################################
DataJetMETC_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC_0_2024")
DataJetMETC_0_2024.runP       = 'C'
DataJetMETC_0_2024.year       = 2024
DataJetMETC_0_2024.dataset    = '/JetMET0/Run2024C-MINIv6NANOv15-v1/NANOAOD'
DataJetMETC_0_2024.process    = "DataJetMET_2024"
DataJetMETC_0_2024.EE         = 0

DataJetMETC_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC_1_2024")
DataJetMETC_1_2024.runP       = 'C'
DataJetMETC_1_2024.year       = 2024
DataJetMETC_1_2024.dataset    = '/JetMET1/Run2024C-MINIv6NANOv15-v1/NANOAOD'
DataJetMETC_1_2024.process    = "DataJetMET_2024"
DataJetMETC_1_2024.EE         = 0

DataJetMETD_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETD_0_2024")
DataJetMETD_0_2024.runP       = 'D'
DataJetMETD_0_2024.year       = 2024
DataJetMETD_0_2024.dataset    = '/JetMET0/Run2024D-MINIv6NANOv15-v1/NANOAOD'
DataJetMETD_0_2024.process    = "DataJetMET_2024"
DataJetMETD_0_2024.EE         = 0

DataJetMETD_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETD_1_2024")
DataJetMETD_1_2024.runP       = 'D'
DataJetMETD_1_2024.year       = 2024
DataJetMETD_1_2024.dataset    = '/JetMET1/Run2024D-MINIv6NANOv15-v1/NANOAOD'
DataJetMETD_1_2024.process    = "DataJetMET_2024"
DataJetMETD_1_2024.EE         = 0

DataJetMETE_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETE_0_2024")
DataJetMETE_0_2024.runP       = 'E'
DataJetMETE_0_2024.year       = 2024
DataJetMETE_0_2024.dataset    = '/JetMET0/Run2024E-MINIv6NANOv15-v1/NANOAOD'
DataJetMETE_0_2024.process    = "DataJetMET_2024"
DataJetMETE_0_2024.EE         = 0

DataJetMETE_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETE_1_2024")
DataJetMETE_1_2024.runP       = 'E'
DataJetMETE_1_2024.year       = 2024
DataJetMETE_1_2024.dataset    = '/JetMET1/Run2024E-MINIv6NANOv15-v1/NANOAOD'
DataJetMETE_1_2024.process    = "DataJetMET_2024"
DataJetMETE_1_2024.EE         = 0

DataJetMETF_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETF_0_2024")
DataJetMETF_0_2024.runP       = 'F'
DataJetMETF_0_2024.year       = 2024
DataJetMETF_0_2024.dataset    = '/JetMET0/Run2024F-MINIv6NANOv15-v2/NANOAOD'
DataJetMETF_0_2024.process    = "DataJetMET_2024"
DataJetMETF_0_2024.EE         = 0

DataJetMETF_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETF_1_2024")
DataJetMETF_1_2024.runP       = 'F'
DataJetMETF_1_2024.year       = 2024
DataJetMETF_1_2024.dataset    = '/JetMET1/Run2024F-MINIv6NANOv15-v2/NANOAOD'
DataJetMETF_1_2024.process    = "DataJetMET_2024"
DataJetMETF_1_2024.EE         = 0

DataJetMETG_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETG_0_2024")
DataJetMETG_0_2024.runP       = 'G'
DataJetMETG_0_2024.year       = 2024
DataJetMETG_0_2024.dataset    = '/JetMET0/Run2024G-MINIv6NANOv15-v2/NANOAOD'
DataJetMETG_0_2024.process    = "DataJetMET_2024"
DataJetMETG_0_2024.EE         = 0

DataJetMETG_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETG_1_2024")
DataJetMETG_1_2024.runP       = 'G'
DataJetMETG_1_2024.year       = 2024
DataJetMETG_1_2024.dataset    = '/JetMET1/Run2024G-MINIv6NANOv15-v2/NANOAOD'
DataJetMETG_1_2024.process    = "DataJetMET_2024"
DataJetMETG_1_2024.EE         = 0

DataJetMETH_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETH_0_2024")
DataJetMETH_0_2024.runP       = 'H'
DataJetMETH_0_2024.year       = 2024
DataJetMETH_0_2024.dataset    = '/JetMET0/Run2024H-MINIv6NANOv15-v2/NANOAOD'
DataJetMETH_0_2024.process    = "DataJetMET_2024"
DataJetMETH_0_2024.EE         = 0

DataJetMETH_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETH_1_2024")
DataJetMETH_1_2024.runP       = 'H'
DataJetMETH_1_2024.year       = 2024
DataJetMETH_1_2024.dataset    = '/JetMET1/Run2024H-MINIv6NANOv15-v2/NANOAOD'
DataJetMETH_1_2024.process    = "DataJetMET_2024"
DataJetMETH_1_2024.EE         = 0

DataJetMETI_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETI_0_2024")
DataJetMETI_0_2024.runP       = 'I'
DataJetMETI_0_2024.year       = 2024
DataJetMETI_0_2024.dataset    = '/JetMET0/Run2024I-MINIv6NANOv15-v2/NANOAOD'
DataJetMETI_0_2024.process    = "DataJetMET_2024"
DataJetMETI_0_2024.EE         = 0

DataJetMETI_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETI_1_2024")
DataJetMETI_1_2024.runP       = 'I'
DataJetMETI_1_2024.year       = 2024
DataJetMETI_1_2024.dataset    = '/JetMET0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD'
DataJetMETI_1_2024.process    = "DataJetMET_2024"
DataJetMETI_1_2024.EE         = 0

DataJetMETI_2_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETI_2_2024")
DataJetMETI_2_2024.runP       = 'I'
DataJetMETI_2_2024.year       = 2024
DataJetMETI_2_2024.dataset    = '/JetMET1/Run2024I-MINIv6NANOv15-v1/NANOAOD'
DataJetMETI_2_2024.process    = "DataJetMET_2024"
DataJetMETI_2_2024.EE         = 0

DataJetMETI_3_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETI_3_2024")
DataJetMETI_3_2024.runP       = 'I'
DataJetMETI_3_2024.year       = 2024
DataJetMETI_3_2024.dataset    = '/JetMET1/Run2024I-MINIv6NANOv15_v2-v2/NANOAOD'
DataJetMETI_3_2024.process    = "DataJetMET_2024"
DataJetMETI_3_2024.EE         = 0


DataJetMET_2024                = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMET_2024")
DataJetMET_2024.year           = 2024
DataJetMET_2024.components     = [
                                    DataJetMETC_0_2024,
                                    DataJetMETC_1_2024,
                                    DataJetMETD_0_2024,
                                    DataJetMETD_1_2024,
                                    DataJetMETE_0_2024,
                                    DataJetMETE_1_2024,
                                    DataJetMETF_0_2024,
                                    DataJetMETF_1_2024,
                                    DataJetMETG_0_2024,
                                    DataJetMETG_1_2024,
                                    DataJetMETH_0_2024,
                                    DataJetMETH_1_2024,
                                    DataJetMETI_0_2024,
                                    DataJetMETI_1_2024,
                                    DataJetMETI_2_2024,
                                    DataJetMETI_3_2024,
                                  ]


DataMuonC_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonC_0_2024")
DataMuonC_0_2024.runP       = 'C'
DataMuonC_0_2024.year       = 2024
DataMuonC_0_2024.dataset    = '/Muon0/Run2024C-MINIv6NANOv15-v1/NANOAOD'
DataMuonC_0_2024.process    = "DataMuon_2024"
DataMuonC_0_2024.EE         = 0

DataMuonC_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonC_1_2024")
DataMuonC_1_2024.runP       = 'C'
DataMuonC_1_2024.year       = 2024
DataMuonC_1_2024.dataset    = '/Muon1/Run2024C-MINIv6NANOv15-v1/NANOAOD'
DataMuonC_1_2024.process    = "DataMuon_2024"
DataMuonC_1_2024.EE         = 0

DataMuonD_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonD_0_2024")
DataMuonD_0_2024.runP       = 'D'
DataMuonD_0_2024.year       = 2024
DataMuonD_0_2024.dataset    = '/Muon0/Run2024D-MINIv6NANOv15-v1/NANOAOD'
DataMuonD_0_2024.process    = "DataMuon_2024"
DataMuonD_0_2024.EE         = 0

DataMuonD_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonD_1_2024")
DataMuonD_1_2024.runP       = 'D'
DataMuonD_1_2024.year       = 2024
DataMuonD_1_2024.dataset    = '/Muon1/Run2024D-MINIv6NANOv15-v1/NANOAOD'
DataMuonD_1_2024.process    = "DataMuon_2024"
DataMuonD_1_2024.EE         = 0

DataMuonE_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonE_0_2024")
DataMuonE_0_2024.runP       = 'E'
DataMuonE_0_2024.year       = 2024
DataMuonE_0_2024.dataset    = '/Muon0/Run2024E-MINIv6NANOv15-v1/NANOAOD'
DataMuonE_0_2024.process    = "DataMuon_2024"
DataMuonE_0_2024.EE         = 0

DataMuonE_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonE_1_2024")
DataMuonE_1_2024.runP       = 'E'
DataMuonE_1_2024.year       = 2024
DataMuonE_1_2024.dataset    = '/Muon1/Run2024E-MINIv6NANOv15-v1/NANOAOD'
DataMuonE_1_2024.process    = "DataMuon_2024"
DataMuonE_1_2024.EE         = 0

DataMuonF_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonF_0_2024")
DataMuonF_0_2024.runP       = 'F'
DataMuonF_0_2024.year       = 2024
DataMuonF_0_2024.dataset    = '/Muon0/Run2024F-MINIv6NANOv15-v1/NANOAOD'
DataMuonF_0_2024.process    = "DataMuon_2024"
DataMuonF_0_2024.EE         = 0

DataMuonF_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonF_1_2024")
DataMuonF_1_2024.runP       = 'F'
DataMuonF_1_2024.year       = 2024
DataMuonF_1_2024.dataset    = '/Muon1/Run2024F-MINIv6NANOv15-v1/NANOAOD'
DataMuonF_1_2024.process    = "DataMuon_2024"
DataMuonF_1_2024.EE         = 0

DataMuonG_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonG_0_2024")
DataMuonG_0_2024.runP       = 'G'
DataMuonG_0_2024.year       = 2024
DataMuonG_0_2024.dataset    = '/Muon0/Run2024G-MINIv6NANOv15-v1/NANOAOD'
DataMuonG_0_2024.process    = "DataMuon_2024"
DataMuonG_0_2024.EE         = 0

DataMuonG_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonG_1_2024")
DataMuonG_1_2024.runP       = 'G'
DataMuonG_1_2024.year       = 2024
DataMuonG_1_2024.dataset    = '/Muon1/Run2024G-MINIv6NANOv15-v2/NANOAOD'
DataMuonG_1_2024.process    = "DataMuon_2024"
DataMuonG_1_2024.EE         = 0

DataMuonH_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonH_0_2024")
DataMuonH_0_2024.runP       = 'H'
DataMuonH_0_2024.year       = 2024
DataMuonH_0_2024.dataset    = '/Muon0/Run2024H-MINIv6NANOv15-v1/NANOAOD'
DataMuonH_0_2024.process    = "DataMuon_2024"
DataMuonH_0_2024.EE         = 0

DataMuonH_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonH_1_2024")
DataMuonH_1_2024.runP       = 'H'
DataMuonH_1_2024.year       = 2024
DataMuonH_1_2024.dataset    = '/Muon1/Run2024H-MINIv6NANOv15-v2/NANOAOD'
DataMuonH_1_2024.process    = "DataMuon_2024"
DataMuonH_1_2024.EE         = 0

DataMuonI_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonI_0_2024")
DataMuonI_0_2024.runP       = 'I'
DataMuonI_0_2024.year       = 2024
DataMuonI_0_2024.dataset    = '/Muon0/Run2024I-MINIv6NANOv15-v1/NANOAOD'
DataMuonI_0_2024.process    = "DataMuon_2024"
DataMuonI_0_2024.EE         = 0

DataMuonI_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonI_1_2024")
DataMuonI_1_2024.runP       = 'I'
DataMuonI_1_2024.year       = 2024
DataMuonI_1_2024.dataset    = '/Muon0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD'
DataMuonI_1_2024.process    = "DataMuon_2024"
DataMuonI_1_2024.EE         = 0

DataMuonI_2_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonI_2_2024")
DataMuonI_2_2024.runP       = 'I'
DataMuonI_2_2024.year       = 2024
DataMuonI_2_2024.dataset    = '/Muon1/Run2024I-MINIv6NANOv15-v1/NANOAOD'
DataMuonI_2_2024.process    = "DataMuon_2024"
DataMuonI_2_2024.EE         = 0

DataMuonI_3_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonI_3_2024")
DataMuonI_3_2024.runP       = 'I'
DataMuonI_3_2024.year       = 2024
DataMuonI_3_2024.dataset    = '/Muon1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD'
DataMuonI_3_2024.process    = "DataMuon_2024"
DataMuonI_3_2024.EE         = 0


DataMuon_2024                = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuon_2024")
DataMuon_2024.year           = 2024
DataMuon_2024.components     = [
                                    DataMuonC_0_2024,
                                    DataMuonC_1_2024,
                                    DataMuonD_0_2024,
                                    DataMuonD_1_2024,
                                    DataMuonE_0_2024,
                                    DataMuonE_1_2024,
                                    DataMuonF_0_2024,
                                    DataMuonF_1_2024,
                                    DataMuonG_0_2024,
                                    DataMuonG_1_2024,
                                    DataMuonH_0_2024,
                                    DataMuonH_1_2024,
                                    DataMuonI_0_2024,
                                    DataMuonI_1_2024,
                                    DataMuonI_2_2024,
                                    DataMuonI_3_2024,
                                  ]


DataEGammaC_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaC_0_2024")
DataEGammaC_0_2024.runP       = 'C'
DataEGammaC_0_2024.year       = 2024
DataEGammaC_0_2024.dataset    = '/EGamma0/Run2024C-MINIv6NANOv15-v1/NANOAOD'
DataEGammaC_0_2024.process    = "DataEGamma_2024"
DataEGammaC_0_2024.EE         = 0

DataEGammaC_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaC_1_2024")
DataEGammaC_1_2024.runP       = 'C'
DataEGammaC_1_2024.year       = 2024
DataEGammaC_1_2024.dataset    = '/EGamma1/Run2024C-MINIv6NANOv15-v1/NANOAOD'
DataEGammaC_1_2024.process    = "DataEGamma_2024"
DataEGammaC_1_2024.EE         = 0

DataEGammaD_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaD_0_2024")
DataEGammaD_0_2024.runP       = 'D'
DataEGammaD_0_2024.year       = 2024
DataEGammaD_0_2024.dataset    = '/EGamma0/Run2024D-MINIv6NANOv15-v1/NANOAOD'
DataEGammaD_0_2024.process    = "DataEGamma_2024"
DataEGammaD_0_2024.EE         = 0

DataEGammaD_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaD_1_2024")
DataEGammaD_1_2024.runP       = 'D'
DataEGammaD_1_2024.year       = 2024
DataEGammaD_1_2024.dataset    = '/EGamma1/Run2024D-MINIv6NANOv15-v1/NANOAOD'
DataEGammaD_1_2024.process    = "DataEGamma_2024"
DataEGammaD_1_2024.EE         = 0

DataEGammaE_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaE_0_2024")
DataEGammaE_0_2024.runP       = 'E'
DataEGammaE_0_2024.year       = 2024
DataEGammaE_0_2024.dataset    = '/EGamma0/Run2024E-MINIv6NANOv15-v1/NANOAOD'
DataEGammaE_0_2024.process    = "DataEGamma_2024"
DataEGammaE_0_2024.EE         = 0

DataEGammaE_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaE_1_2024")
DataEGammaE_1_2024.runP       = 'E'
DataEGammaE_1_2024.year       = 2024
DataEGammaE_1_2024.dataset    = '/EGamma1/Run2024E-MINIv6NANOv15-v1/NANOAOD'
DataEGammaE_1_2024.process    = "DataEGamma_2024"
DataEGammaE_1_2024.EE         = 0

DataEGammaF_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaF_0_2024")
DataEGammaF_0_2024.runP       = 'F'
DataEGammaF_0_2024.year       = 2024
DataEGammaF_0_2024.dataset    = '/EGamma0/Run2024F-MINIv6NANOv15-v1/NANOAOD'
DataEGammaF_0_2024.process    = "DataEGamma_2024"
DataEGammaF_0_2024.EE         = 0

DataEGammaF_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaF_1_2024")
DataEGammaF_1_2024.runP       = 'F'
DataEGammaF_1_2024.year       = 2024
DataEGammaF_1_2024.dataset    = '/EGamma1/Run2024F-MINIv6NANOv15-v1/NANOAOD'
DataEGammaF_1_2024.process    = "DataEGamma_2024"
DataEGammaF_1_2024.EE         = 0

DataEGammaG_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaG_0_2024")
DataEGammaG_0_2024.runP       = 'G'
DataEGammaG_0_2024.year       = 2024
DataEGammaG_0_2024.dataset    = '/EGamma0/Run2024G-MINIv6NANOv15-v2/NANOAOD'
DataEGammaG_0_2024.process    = "DataEGamma_2024"
DataEGammaG_0_2024.EE         = 0

DataEGammaG_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaG_1_2024")
DataEGammaG_1_2024.runP       = 'G'
DataEGammaG_1_2024.year       = 2024
DataEGammaG_1_2024.dataset    = '/EGamma1/Run2024G-MINIv6NANOv15-v2/NANOAOD'
DataEGammaG_1_2024.process    = "DataEGamma_2024"
DataEGammaG_1_2024.EE         = 0

DataEGammaH_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaH_0_2024")
DataEGammaH_0_2024.runP       = 'H'
DataEGammaH_0_2024.year       = 2024
DataEGammaH_0_2024.dataset    = '/EGamma0/Run2024H-MINIv6NANOv15-v2/NANOAOD'
DataEGammaH_0_2024.process    = "DataEGamma_2024"
DataEGammaH_0_2024.EE         = 0

DataEGammaH_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaH_1_2024")
DataEGammaH_1_2024.runP       = 'H'
DataEGammaH_1_2024.year       = 2024
DataEGammaH_1_2024.dataset    = '/EGamma1/Run2024H-MINIv6NANOv15-v1/NANOAOD'
DataEGammaH_1_2024.process    = "DataEGamma_2024"
DataEGammaH_1_2024.EE         = 0

DataEGammaI_0_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaI_0_2024")
DataEGammaI_0_2024.runP       = 'I'
DataEGammaI_0_2024.year       = 2024
DataEGammaI_0_2024.dataset    = '/EGamma0/Run2024I-MINIv6NANOv15-v1/NANOAOD'
DataEGammaI_0_2024.process    = "DataEGamma_2024"
DataEGammaI_0_2024.EE         = 0

DataEGammaI_1_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaI_1_2024")
DataEGammaI_1_2024.runP       = 'I'
DataEGammaI_1_2024.year       = 2024
DataEGammaI_1_2024.dataset    = '/EGamma0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD'
DataEGammaI_1_2024.process    = "DataEGamma_2024"
DataEGammaI_1_2024.EE         = 0

DataEGammaI_2_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaI_2_2024")
DataEGammaI_2_2024.runP       = 'I'
DataEGammaI_2_2024.year       = 2024
DataEGammaI_2_2024.dataset    = '/EGamma1/Run2024I-MINIv6NANOv15-v1/NANOAOD'
DataEGammaI_2_2024.process    = "DataEGamma_2024"
DataEGammaI_2_2024.EE         = 0

DataEGammaI_3_2024            = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaI_3_2024")
DataEGammaI_3_2024.runP       = 'I'
DataEGammaI_3_2024.year       = 2024
DataEGammaI_3_2024.dataset    = '/EGamma1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD'
DataEGammaI_3_2024.process    = "DataEGamma_2024"
DataEGammaI_3_2024.EE         = 0


DataEGamma_2024                = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGamma_2024")
DataEGamma_2024.year           = 2024
DataEGamma_2024.components     = [
                                    DataEGammaC_0_2024,
                                    DataEGammaC_1_2024,
                                    DataEGammaD_0_2024,
                                    DataEGammaD_1_2024,
                                    DataEGammaE_0_2024,
                                    DataEGammaE_1_2024,
                                    DataEGammaF_0_2024,
                                    DataEGammaF_1_2024,
                                    DataEGammaG_0_2024,
                                    DataEGammaG_1_2024,
                                    DataEGammaH_0_2024,
                                    DataEGammaH_1_2024,
                                    DataEGammaI_0_2024,
                                    DataEGammaI_1_2024,
                                    DataEGammaI_2_2024,
                                    DataEGammaI_3_2024,
                                  ]

############### UNIX code meanings ################
# XXXXX  5 digits for each sample
# 1st digit: 0 for 2016, 1 for 2017, 2 for 2018, 3 for 2022, 4 for 2022EE, 5 for 2023, 6 for 2023BP
# 2nd digit: 0 for data, 1 for MC bkg, 2 for MC signal
# 3rd digit: for the process (QCD = 0, TT = 1, ZJets = 2, WJets = 3, 
#                             Tprime = 0, tDM = 1, 
#                             Data_MET = 0, Data_SingleMu = 1,...)
# 3rd digit and 4th digit: 2 digits identifies the sample 

# example: QCDHT_100to200_2018 == 21000, QCDHT_200to300_2018 == 21001
#          DATAHTA_2018 == 20600, DATAHTB_2018 == 20601, DATAHTC_2018 == 20602, DATAHTD_2018 == 20603  
### non diamo un codice ai sample con le components --> da capire se serve aggiungerlo


sample_dict = {

    # 'DataHTA_2018': DataHTA_2018,

    ################################## RUN II
    # Data MET 2018   
    'DataMET_2018': DataMET_2018, 'DataMETA_2018': DataMETA_2018, 'DataMETB_2018': DataMETB_2018,
    'DataMETC_2018': DataMETC_2018, 'DataMETD_2018': DataMETD_2018, 
    # 'DataMETA_2018': DataMETA_2018,
    # Data Single Muon 2018
    'DataSingleMu_2018':DataSingleMu_2018, 'DataSingleMuA_2018':DataSingleMuA_2018, 'DataSingleMuB_2018':DataSingleMuB_2018, 
    'DataSingleMuC_2018':DataSingleMuC_2018, 'DataSingleMuD_2018':DataSingleMuD_2018,
    # BKGs 2018
    'QCDHT_100to200_2018':QCDHT_100to200_2018, 'QCDHT_200to300_2018':QCDHT_200to300_2018, 
    'QCDHT_300to500_2018':QCDHT_300to500_2018, 'QCDHT_500to700_2018':QCDHT_500to700_2018, 
    'QCDHT_700to1000_2018':QCDHT_700to1000_2018, 'QCDHT_1000to1500_2018':QCDHT_1000to1500_2018, 
    'QCDHT_1500to2000_2018':QCDHT_1500to2000_2018, 'QCDHT_2000toInf_2018':QCDHT_2000toInf_2018, 
    'QCD_2018':QCD_2018,
    'TT_Mtt700to1000_2018':TT_Mtt700to1000_2018, 'TT_Mtt1000toInf_2018':TT_Mtt1000toInf_2018, 
    'TT_semilep_2018':TT_semilep_2018, 'TT_hadr_2018':TT_hadr_2018,
    'TT_2018':TT_2018,
    'ZJetsToNuNu_HT100to200_2018':ZJetsToNuNu_HT100to200_2018, 'ZJetsToNuNu_HT200to400_2018':ZJetsToNuNu_HT200to400_2018, 
    'ZJetsToNuNu_HT400to600_2018':ZJetsToNuNu_HT400to600_2018, 'ZJetsToNuNu_HT600to800_2018':ZJetsToNuNu_HT600to800_2018, 
    'ZJetsToNuNu_HT800to1200_2018':ZJetsToNuNu_HT800to1200_2018, 'ZJetsToNuNu_HT1200to2500_2018':ZJetsToNuNu_HT1200to2500_2018, 
    'ZJetsToNuNu_HT2500toInf_2018':ZJetsToNuNu_HT2500toInf_2018, 
    'ZJetsToNuNu_2018':ZJetsToNuNu_2018,
    'WJetsHT70to100_2018':WJetsHT70to100_2018,'WJetsHT100to200_2018':WJetsHT100to200_2018,
    'WJetsHT200to400_2018':WJetsHT200to400_2018,'WJetsHT400to600_2018':WJetsHT400to600_2018,
    'WJetsHT600to800_2018':WJetsHT600to800_2018,'WJetsHT800to1200_2018':WJetsHT800to1200_2018,
    'WJetsHT1200to2500_2018':WJetsHT1200to2500_2018,'WJetsHT2500toInf_2018':WJetsHT2500toInf_2018,
    'WJets_2018':WJets_2018,    
    # signals 2018

    'tDM_mPhi50_mChi1_2018' : tDM_mPhi50_mChi1_2018, 'tDM_mPhi500_mChi1_2018' : tDM_mPhi500_mChi1_2018, 'tDM_mPhi1000_mChi1_2018' : tDM_mPhi1000_mChi1_2018,
    

    "Zprime4top_500_2018":Zprime4top_500_2018, "Zprime4top_1000_2018":Zprime4top_1000_2018, "Zprime4top_2000_2018":Zprime4top_2000_2018, 
    
    #######################################
    ############# RUN III ################
    #######################################

    #####################2022
    ############ QCD
    'QCD_2022' : QCD_2022,
    # "QCD_HT40to70_2022": QCD_HT40to70_2022, 
    "QCD_HT70to100_2022": QCD_HT70to100_2022, 
    "QCD_HT100to200_2022": QCD_HT100to200_2022, "QCD_HT200to400_2022": QCD_HT200to400_2022, 
    "QCD_HT400to600_2022": QCD_HT400to600_2022, "QCD_HT600to800_2022": QCD_HT600to800_2022, 
    "QCD_HT800to1000_2022": QCD_HT800to1000_2022, "QCD_HT1000to1200_2022": QCD_HT1000to1200_2022, 
    "QCD_HT1200to1500_2022": QCD_HT1200to1500_2022, "QCD_HT1500to2000_2022": QCD_HT1500to2000_2022, "QCD_HT2000_2022": QCD_HT2000_2022,
    ########### TT
    'TT_2022': TT_2022, 'TT_semilep_2022' : TT_semilep_2022, 'TT_hadr_2022' : TT_hadr_2022, 'TT_dilep_2022' : TT_dilep_2022,
    ########## SingleTop
    "TW_2022": TW_2022,
    "TWminustoLNu2Q_2022": TWminustoLNu2Q_2022,
    "TWminusto4Q_2022": TWminusto4Q_2022,
    "TWminusto2L2Nu_2022": TWminusto2L2Nu_2022,
    "TbarWplustoLNu2Q_2022": TbarWplustoLNu2Q_2022,
    "TbarWplusto4Q_2022": TbarWplusto4Q_2022,
    "TbarWplusto2L2Nu_2022": TbarWplusto2L2Nu_2022,
    ########## WJets
    "WJets_2jets_2022": WJets_2jets_2022, 
    "WJets_2jets0J_2022": WJets_2jets0J_2022, "WJets_2jets1J_2022": WJets_2jets1J_2022, "WJets_2jets2J_2022": WJets_2jets2J_2022,

    # "WJets_2022":WJets_2022, 
    # "WJets_HT120to200_2022":WJets_HT120to200_2022, "WJets_HT200to400_2022":WJets_HT200to400_2022, 
    # "WJets_HT400to800_2022":WJets_HT400to800_2022, "WJets_HT800to1500_2022":WJets_HT800to1500_2022, 
    # "WJets_HT1500to2500_2022":WJets_HT1500to2500_2022, "WJets_HT2500to4000_2022":WJets_HT2500to4000_2022, 
    # "WJets_HT4000to6000_2022":WJets_HT4000to6000_2022, "WJets_HT6000_2022":WJets_HT6000_2022,
    ########## ZJetsToNuNu
    # "ZJetsToNuNu_2022":ZJetsToNuNu_2022, "ZJetsToNuNu_HT100to200_2022":ZJetsToNuNu_HT100to200_2022, 
    # "ZJetsToNuNu_HT200to400_2022":ZJetsToNuNu_HT200to400_2022, "ZJetsToNuNu_HT400to800_2022":ZJetsToNuNu_HT400to800_2022, 
    # "ZJetsToNuNu_HT800to1500_2022":ZJetsToNuNu_HT800to1500_2022, "ZJetsToNuNu_HT1500to2500_2022":ZJetsToNuNu_HT1500to2500_2022, 
    # "ZJetsToNuNu_HT2500_2022":ZJetsToNuNu_HT2500_2022,

    "ZJetsToNuNu_2jets_2022":ZJetsToNuNu_2jets_2022,
    "ZJetsToNuNu_2jets_PT40to100_1J_2022":ZJetsToNuNu_2jets_PT40to100_1J_2022, "ZJetsToNuNu_2jets_PT100to200_1J_2022":ZJetsToNuNu_2jets_PT100to200_1J_2022,
    "ZJetsToNuNu_2jets_PT200to400_1J_2022":ZJetsToNuNu_2jets_PT200to400_1J_2022, "ZJetsToNuNu_2jets_PT400to600_1J_2022":ZJetsToNuNu_2jets_PT400to600_1J_2022,
    "ZJetsToNuNu_2jets_PT600_1J_2022":ZJetsToNuNu_2jets_PT600_1J_2022, "ZJetsToNuNu_2jets_PT40to100_2J_2022":ZJetsToNuNu_2jets_PT40to100_2J_2022,
    "ZJetsToNuNu_2jets_PT100to200_2J_2022":ZJetsToNuNu_2jets_PT100to200_2J_2022, "ZJetsToNuNu_2jets_PT200to400_2J_2022":ZJetsToNuNu_2jets_PT200to400_2J_2022,
    "ZJetsToNuNu_2jets_PT400to600_2J_2022":ZJetsToNuNu_2jets_PT400to600_2J_2022, "ZJetsToNuNu_2jets_PT600_2J_2022":ZJetsToNuNu_2jets_PT600_2J_2022,
                                    
    ########## SIGNALS tDM

    "tDM_mPhi50_mChi1_2022": tDM_mPhi50_mChi1_2022,
    "tDM_mPhi200_mChi1_2022": tDM_mPhi200_mChi1_2022,
    "tDM_mPhi500_mChi1_2022": tDM_mPhi500_mChi1_2022,
    "tDM_mPhi1000_mChi1_2022": tDM_mPhi1000_mChi1_2022,
    "ttDM_mPhi50_mChi1_2022": ttDM_mPhi50_mChi1_2022,
    "ttDM_mPhi200_mChi1_2022": ttDM_mPhi200_mChi1_2022,
    "ttDM_mPhi500_mChi1_2022": ttDM_mPhi500_mChi1_2022,
    "ttDM_mPhi1000_mChi1_2022": ttDM_mPhi1000_mChi1_2022,

    #####################Tagger studies 4 top samples
    "Zprime4top_500_2022" : Zprime4top_500_2022, "Zprime4top_1000_2022" : Zprime4top_1000_2022, "Zprime4top_2000_2022" : Zprime4top_2000_2022,

    #####################2022EE
    ############ QCD
    'QCD_2022EE' : QCD_2022EE,
    # "QCD_HT40to70_2022EE": QCD_HT40to70_2022EE, 
    "QCD_HT70to100_2022EE": QCD_HT70to100_2022EE, 
    "QCD_HT100to200_2022EE": QCD_HT100to200_2022EE, "QCD_HT200to400_2022EE": QCD_HT200to400_2022EE, 
    "QCD_HT400to600_2022EE": QCD_HT400to600_2022EE, "QCD_HT600to800_2022EE": QCD_HT600to800_2022EE, 
    "QCD_HT800to1000_2022EE": QCD_HT800to1000_2022EE, "QCD_HT1000to1200_2022EE": QCD_HT1000to1200_2022EE, 
    "QCD_HT1200to1500_2022EE": QCD_HT1200to1500_2022EE, "QCD_HT1500to2000_2022EE": QCD_HT1500to2000_2022EE, "QCD_HT2000_2022EE": QCD_HT2000_2022EE,
    ########### TT
    'TT_2022EE': TT_2022EE, 'TT_semilep_2022EE' : TT_semilep_2022EE, 'TT_hadr_2022EE' : TT_hadr_2022EE, 'TT_dilep_2022EE' : TT_dilep_2022EE,
    ########## SingleTop
    "TW_2022EE": TW_2022EE,
    "TWminustoLNu2Q_2022EE": TWminustoLNu2Q_2022EE,
    "TWminusto4Q_2022EE": TWminusto4Q_2022EE,
    "TWminusto2L2Nu_2022EE": TWminusto2L2Nu_2022EE,
    "TbarWplustoLNu2Q_2022EE": TbarWplustoLNu2Q_2022EE,
    "TbarWplusto4Q_2022EE": TbarWplusto4Q_2022EE,
    "TbarWplusto2L2Nu_2022EE": TbarWplusto2L2Nu_2022EE,
    ########## WJets
    "WJets_2jets_2022EE": WJets_2jets_2022EE, 
    "WJets_2jets0J_2022EE": WJets_2jets0J_2022EE, "WJets_2jets1J_2022EE": WJets_2jets1J_2022EE, "WJets_2jets2J_2022EE": WJets_2jets2J_2022EE,

    "WJets_2022EE":WJets_2022EE, 
    "WJets_HT120to200_2022EE":WJets_HT120to200_2022EE, "WJets_HT200to400_2022EE":WJets_HT200to400_2022EE, 
    "WJets_HT400to800_2022EE":WJets_HT400to800_2022EE, "WJets_HT800to1500_2022EE":WJets_HT800to1500_2022EE, 
    "WJets_HT1500to2500_2022EE":WJets_HT1500to2500_2022EE, "WJets_HT2500to4000_2022EE":WJets_HT2500to4000_2022EE, 
    "WJets_HT4000to6000_2022EE":WJets_HT4000to6000_2022EE, "WJets_HT6000_2022EE":WJets_HT6000_2022EE,
    ########## ZJetsToNuNu
    "ZJetsToNuNu_2022EE":ZJetsToNuNu_2022EE, "ZJetsToNuNu_HT100to200_2022EE":ZJetsToNuNu_HT100to200_2022EE, 
    "ZJetsToNuNu_HT200to400_2022EE":ZJetsToNuNu_HT200to400_2022EE, "ZJetsToNuNu_HT400to800_2022EE":ZJetsToNuNu_HT400to800_2022EE, 
    "ZJetsToNuNu_HT800to1500_2022EE":ZJetsToNuNu_HT800to1500_2022EE, "ZJetsToNuNu_HT1500to2500_2022EE":ZJetsToNuNu_HT1500to2500_2022EE, 
    "ZJetsToNuNu_HT2500_2022EE":ZJetsToNuNu_HT2500_2022EE,

    "ZJetsToNuNu_2jets_2022EE":ZJetsToNuNu_2jets_2022EE,
    "ZJetsToNuNu_2jets_PT40to100_1J_2022EE":ZJetsToNuNu_2jets_PT40to100_1J_2022EE, "ZJetsToNuNu_2jets_PT100to200_1J_2022EE":ZJetsToNuNu_2jets_PT100to200_1J_2022EE,
    "ZJetsToNuNu_2jets_PT200to400_1J_2022EE":ZJetsToNuNu_2jets_PT200to400_1J_2022EE, "ZJetsToNuNu_2jets_PT400to600_1J_2022EE":ZJetsToNuNu_2jets_PT400to600_1J_2022EE,
    "ZJetsToNuNu_2jets_PT600_1J_2022EE":ZJetsToNuNu_2jets_PT600_1J_2022EE, "ZJetsToNuNu_2jets_PT40to100_2J_2022EE":ZJetsToNuNu_2jets_PT40to100_2J_2022EE,
    "ZJetsToNuNu_2jets_PT100to200_2J_2022EE":ZJetsToNuNu_2jets_PT100to200_2J_2022EE, "ZJetsToNuNu_2jets_PT200to400_2J_2022EE":ZJetsToNuNu_2jets_PT200to400_2J_2022EE,
    "ZJetsToNuNu_2jets_PT400to600_2J_2022EE":ZJetsToNuNu_2jets_PT400to600_2J_2022EE, "ZJetsToNuNu_2jets_PT600_2J_2022EE":ZJetsToNuNu_2jets_PT600_2J_2022EE,

    #####################Tagger studies 4 top samples
    "Zprime4top_500_2022EE" : Zprime4top_500_2022EE, "Zprime4top_1000_2022EE" : Zprime4top_1000_2022EE, "Zprime4top_2000_2022EE" : Zprime4top_2000_2022EE,

    #####################2023
    ############ QCD
    "QCD_2023" : QCD_2023,
    # "QCD_HT40to70_2023": QCD_HT40to70_2023, 
    "QCD_HT70to100_2023": QCD_HT70to100_2023, 
    "QCD_HT100to200_2023": QCD_HT100to200_2023, "QCD_HT200to400_2023": QCD_HT200to400_2023, 
    "QCD_HT400to600_2023": QCD_HT400to600_2023, "QCD_HT600to800_2023": QCD_HT600to800_2023, 
    "QCD_HT800to1000_2023": QCD_HT800to1000_2023, "QCD_HT1000to1200_2023": QCD_HT1000to1200_2023, 
    "QCD_HT1200to1500_2023": QCD_HT1200to1500_2023, "QCD_HT1500to2000_2023": QCD_HT1500to2000_2023, "QCD_HT2000_2023": QCD_HT2000_2023,
    ########### TT
    "TT_2023": TT_2023, "TT_semilep_2023" : TT_semilep_2023, "TT_hadr_2023" : TT_hadr_2023, "TT_dilep_2023" : TT_dilep_2023,
    ########## SingleTop
    "TW_2023": TW_2023,
    "TWminustoLNu2Q_2023": TWminustoLNu2Q_2023,
    "TWminusto4Q_2023": TWminusto4Q_2023,
    "TWminusto2L2Nu_2023": TWminusto2L2Nu_2023,
    "TbarWplustoLNu2Q_2023": TbarWplustoLNu2Q_2023,
    "TbarWplusto4Q_2023": TbarWplusto4Q_2023,
    "TbarWplusto2L2Nu_2023": TbarWplusto2L2Nu_2023,
    ########## WJets
    "WJets_2jets_2023": WJets_2jets_2023, 
    "WJets_2jets0J_2023": WJets_2jets0J_2023, "WJets_2jets1J_2023": WJets_2jets1J_2023, "WJets_2jets2J_2023": WJets_2jets2J_2023,

    "WJets_2023":WJets_2023, 
    "WJets_HT120to200_2023":WJets_HT120to200_2023, "WJets_HT200to400_2023":WJets_HT200to400_2023, 
    "WJets_HT400to800_2023":WJets_HT400to800_2023, "WJets_HT800to1500_2023":WJets_HT800to1500_2023, 
    "WJets_HT1500to2500_2023":WJets_HT1500to2500_2023, "WJets_HT2500to4000_2023":WJets_HT2500to4000_2023, 
    "WJets_HT4000to6000_2023":WJets_HT4000to6000_2023, "WJets_HT6000_2023":WJets_HT6000_2023,
    ########## ZJetsToNuNu
    "ZJetsToNuNu_2023":ZJetsToNuNu_2023, "ZJetsToNuNu_HT100to200_2023":ZJetsToNuNu_HT100to200_2023, 
    "ZJetsToNuNu_HT200to400_2023":ZJetsToNuNu_HT200to400_2023, "ZJetsToNuNu_HT400to800_2023":ZJetsToNuNu_HT400to800_2023, 
    "ZJetsToNuNu_HT800to1500_2023":ZJetsToNuNu_HT800to1500_2023, "ZJetsToNuNu_HT1500to2500_2023":ZJetsToNuNu_HT1500to2500_2023, 
    "ZJetsToNuNu_HT2500_2023":ZJetsToNuNu_HT2500_2023,

    "ZJetsToNuNu_2jets_2023":ZJetsToNuNu_2jets_2023,
    "ZJetsToNuNu_2jets_PT40to100_1J_2023":ZJetsToNuNu_2jets_PT40to100_1J_2023, "ZJetsToNuNu_2jets_PT100to200_1J_2023":ZJetsToNuNu_2jets_PT100to200_1J_2023,
    "ZJetsToNuNu_2jets_PT200to400_1J_2023":ZJetsToNuNu_2jets_PT200to400_1J_2023, "ZJetsToNuNu_2jets_PT400to600_1J_2023":ZJetsToNuNu_2jets_PT400to600_1J_2023,
    "ZJetsToNuNu_2jets_PT600_1J_2023":ZJetsToNuNu_2jets_PT600_1J_2023, "ZJetsToNuNu_2jets_PT40to100_2J_2023":ZJetsToNuNu_2jets_PT40to100_2J_2023,
    "ZJetsToNuNu_2jets_PT100to200_2J_2023":ZJetsToNuNu_2jets_PT100to200_2J_2023, "ZJetsToNuNu_2jets_PT200to400_2J_2023":ZJetsToNuNu_2jets_PT200to400_2J_2023,
    "ZJetsToNuNu_2jets_PT400to600_2J_2023":ZJetsToNuNu_2jets_PT400to600_2J_2023, "ZJetsToNuNu_2jets_PT600_2J_2023":ZJetsToNuNu_2jets_PT600_2J_2023,
                                    


    #####################2023postBPix
    ############ QCD
    "QCD_2023postBPix" : QCD_2023postBPix,
    # "QCD_HT40to70_2023postBPix": QCD_HT40to70_2023postBPix, 
    "QCD_HT70to100_2023postBPix": QCD_HT70to100_2023postBPix, 
    "QCD_HT100to200_2023postBPix": QCD_HT100to200_2023postBPix, "QCD_HT200to400_2023postBPix": QCD_HT200to400_2023postBPix, 
    "QCD_HT400to600_2023postBPix": QCD_HT400to600_2023postBPix, "QCD_HT600to800_2023postBPix": QCD_HT600to800_2023postBPix, 
    "QCD_HT800to1000_2023postBPix": QCD_HT800to1000_2023postBPix, "QCD_HT1000to1200_2023postBPix": QCD_HT1000to1200_2023postBPix, 
    "QCD_HT1200to1500_2023postBPix": QCD_HT1200to1500_2023postBPix, "QCD_HT1500to2000_2023postBPix": QCD_HT1500to2000_2023postBPix, "QCD_HT2000_2023postBPix": QCD_HT2000_2023postBPix,
    ########### TT
    "TT_2023postBPix": TT_2023postBPix, "TT_semilep_2023postBPix" : TT_semilep_2023postBPix, "TT_hadr_2023postBPix" : TT_hadr_2023postBPix, "TT_dilep_2023postBPix" : TT_dilep_2023postBPix,
    ########## SingleTop
    "TW_2023postBPix": TW_2023postBPix,
    "TWminustoLNu2Q_2023postBPix": TWminustoLNu2Q_2023postBPix,
    "TWminusto4Q_2023postBPix": TWminusto4Q_2023postBPix,
    "TWminusto2L2Nu_2023postBPix": TWminusto2L2Nu_2023postBPix,
    "TbarWplustoLNu2Q_2023postBPix": TbarWplustoLNu2Q_2023postBPix,
    "TbarWplusto4Q_2023postBPix": TbarWplusto4Q_2023postBPix,
    "TbarWplusto2L2Nu_2023postBPix": TbarWplusto2L2Nu_2023postBPix,
    ########## WJets
    "WJets_2jets_2023postBPix": WJets_2jets_2023postBPix, 
    "WJets_2jets0J_2023postBPix": WJets_2jets0J_2023postBPix, "WJets_2jets1J_2023postBPix": WJets_2jets1J_2023postBPix, "WJets_2jets2J_2023postBPix": WJets_2jets2J_2023postBPix,

    "WJets_2023postBPix":WJets_2023postBPix, 
    "WJets_HT120to200_2023postBPix":WJets_HT120to200_2023postBPix, "WJets_HT200to400_2023postBPix":WJets_HT200to400_2023postBPix, 
    "WJets_HT400to800_2023postBPix":WJets_HT400to800_2023postBPix, "WJets_HT800to1500_2023postBPix":WJets_HT800to1500_2023postBPix, 
    "WJets_HT1500to2500_2023postBPix":WJets_HT1500to2500_2023postBPix, "WJets_HT2500to4000_2023postBPix":WJets_HT2500to4000_2023postBPix, 
    "WJets_HT4000to6000_2023postBPix":WJets_HT4000to6000_2023postBPix, "WJets_HT6000_2023postBPix":WJets_HT6000_2023postBPix,
    ########## ZJetsToNuNu
    "ZJetsToNuNu_2023postBPix":ZJetsToNuNu_2023postBPix, "ZJetsToNuNu_HT100to200_2023postBPix":ZJetsToNuNu_HT100to200_2023postBPix, 
    "ZJetsToNuNu_HT200to400_2023postBPix":ZJetsToNuNu_HT200to400_2023postBPix, "ZJetsToNuNu_HT400to800_2023postBPix":ZJetsToNuNu_HT400to800_2023postBPix, 
    "ZJetsToNuNu_HT800to1500_2023postBPix":ZJetsToNuNu_HT800to1500_2023postBPix, "ZJetsToNuNu_HT1500to2500_2023postBPix":ZJetsToNuNu_HT1500to2500_2023postBPix, 
    "ZJetsToNuNu_HT2500_2023postBPix":ZJetsToNuNu_HT2500_2023postBPix,

    "ZJetsToNuNu_2jets_2023postBPix":ZJetsToNuNu_2jets_2023postBPix,
    "ZJetsToNuNu_2jets_PT40to100_1J_2023postBPix":ZJetsToNuNu_2jets_PT40to100_1J_2023postBPix, "ZJetsToNuNu_2jets_PT100to200_1J_2023postBPix":ZJetsToNuNu_2jets_PT100to200_1J_2023postBPix,
    "ZJetsToNuNu_2jets_PT200to400_1J_2023postBPix":ZJetsToNuNu_2jets_PT200to400_1J_2023postBPix, "ZJetsToNuNu_2jets_PT400to600_1J_2023postBPix":ZJetsToNuNu_2jets_PT400to600_1J_2023postBPix,
    "ZJetsToNuNu_2jets_PT600_1J_2023postBPix":ZJetsToNuNu_2jets_PT600_1J_2023postBPix, "ZJetsToNuNu_2jets_PT40to100_2J_2023postBPix":ZJetsToNuNu_2jets_PT40to100_2J_2023postBPix,
    "ZJetsToNuNu_2jets_PT100to200_2J_2023postBPix":ZJetsToNuNu_2jets_PT100to200_2J_2023postBPix, "ZJetsToNuNu_2jets_PT200to400_2J_2023postBPix":ZJetsToNuNu_2jets_PT200to400_2J_2023postBPix,
    "ZJetsToNuNu_2jets_PT400to600_2J_2023postBPix":ZJetsToNuNu_2jets_PT400to600_2J_2023postBPix, "ZJetsToNuNu_2jets_PT600_2J_2023postBPix":ZJetsToNuNu_2jets_PT600_2J_2023postBPix,

    #####################2024
    ############ QCD
    "QCD_2024" :                QCD_2024,
    # "QCD_HT40to70_2024": QCD_HT40to70_2024, 
    "QCD_HT70to100_2024":       QCD_HT70to100_2024,
    "QCD_HT100to200_2024":      QCD_HT100to200_2024,
    "QCD_HT200to400_2024":      QCD_HT200to400_2024, 
    "QCD_HT400to600_2024":      QCD_HT400to600_2024,
    "QCD_HT600to800_2024":      QCD_HT600to800_2024,
    "QCD_HT800to1000_2024":     QCD_HT800to1000_2024,
    "QCD_HT1000to1200_2024":    QCD_HT1000to1200_2024,
    "QCD_HT1200to1500_2024":    QCD_HT1200to1500_2024,
    "QCD_HT1500to2000_2024":    QCD_HT1500to2000_2024,
    "QCD_HT2000_2024":          QCD_HT2000_2024,
    ########### TT
    "TT_2024":                  TT_2024,
    "TT_semilep_2024":          TT_semilep_2024,
    "TT_hadr_2024":             TT_hadr_2024,
    "TT_dilep_2024":            TT_dilep_2024,
    ########## SingleTop
    "TW_2024":                  TW_2024,
    "TWminustoLNu2Q_2024":      TWminustoLNu2Q_2024,
    "TWminusto4Q_2024":         TWminusto4Q_2024,
    "TWminusto2L2Nu_2024":      TWminusto2L2Nu_2024,
    "TbarWplustoLNu2Q_2024":    TbarWplustoLNu2Q_2024,
    "TbarWplusto4Q_2024":       TbarWplusto4Q_2024,
    "TbarWplusto2L2Nu_2024":    TbarWplusto2L2Nu_2024,
    ########## WJets
    "WJets_4Jets_1J_2024":      WJets_4Jets_1J_2024,
    "WJets_4Jets_2J_2024":      WJets_4Jets_2J_2024,
    "WJets_4Jets_3J_2024":      WJets_4Jets_3J_2024,
    "WJets_4Jets_4J_2024":      WJets_4Jets_4J_2024,
    "WJets_4Jets_2024":         WJets_4Jets_2024,

    "WJets_2jets_2024":                   WJets_2jets_2024,
    "WJets_2jets_ENu_0J_2024":            WJets_2jets_ENu_0J_2024,
    "WJets_2jets_ENu_1J_2024":            WJets_2jets_ENu_1J_2024,
    "WJets_2jets_ENu_2J_2024":            WJets_2jets_ENu_2J_2024,
    "WJets_2jets_MuNu_0J_2024":           WJets_2jets_MuNu_0J_2024,
    "WJets_2jets_MuNu_1J_2024":           WJets_2jets_MuNu_1J_2024,
    "WJets_2jets_MuNu_2J_2024":           WJets_2jets_MuNu_2J_2024,
    "WJets_2jets_TauNu_0J_2024":          WJets_2jets_TauNu_0J_2024,
    "WJets_2jets_TauNu_1J_2024":          WJets_2jets_TauNu_1J_2024,
    "WJets_2jets_TauNu_2J_2024":          WJets_2jets_TauNu_2J_2024,

    ########## ZJetsToNuNu
    "ZJetsToNuNu_2024":                 ZJetsToNuNu_2024,
    "ZJetsToNuNu_HT100to200_2024":      ZJetsToNuNu_HT100to200_2024,
    "ZJetsToNuNu_HT200to400_2024":      ZJetsToNuNu_HT200to400_2024,
    "ZJetsToNuNu_HT400to800_2024":      ZJetsToNuNu_HT400to800_2024,
    "ZJetsToNuNu_HT800to1500_2024":     ZJetsToNuNu_HT800to1500_2024,
    "ZJetsToNuNu_HT1500to2500_2024":    ZJetsToNuNu_HT1500to2500_2024,
    "ZJetsToNuNu_HT2500_2024":          ZJetsToNuNu_HT2500_2024,

    "ZJetsToNuNu_2jets_2024":                   ZJetsToNuNu_2jets_2024,
    "ZJetsToNuNu_2jets_PT40to100_1J_2024":      ZJetsToNuNu_2jets_PT40to100_1J_2024,
    "ZJetsToNuNu_2jets_PT100to200_1J_2024":     ZJetsToNuNu_2jets_PT100to200_1J_2024,
    "ZJetsToNuNu_2jets_PT200to400_1J_2024":     ZJetsToNuNu_2jets_PT200to400_1J_2024,
    "ZJetsToNuNu_2jets_PT400to600_1J_2024":     ZJetsToNuNu_2jets_PT400to600_1J_2024,
    "ZJetsToNuNu_2jets_PT600_1J_2024":          ZJetsToNuNu_2jets_PT600_1J_2024,
    "ZJetsToNuNu_2jets_PT40to100_2J_2024":      ZJetsToNuNu_2jets_PT40to100_2J_2024,
    "ZJetsToNuNu_2jets_PT100to200_2J_2024":     ZJetsToNuNu_2jets_PT100to200_2J_2024,
    "ZJetsToNuNu_2jets_PT200to400_2J_2024":     ZJetsToNuNu_2jets_PT200to400_2J_2024,
    "ZJetsToNuNu_2jets_PT400to600_2J_2024":     ZJetsToNuNu_2jets_PT400to600_2J_2024,
    "ZJetsToNuNu_2jets_PT600_2J_2024":          ZJetsToNuNu_2jets_PT600_2J_2024,


    
    
    
    ############################################# DATA 
    'DataJetMET_2022': DataJetMET_2022, 'DataJetMETC_2022':DataJetMETC_2022, 'DataJetMETD_2022':DataJetMETD_2022, 
    'DataJetMET_2022EE': DataJetMET_2022EE,
    'DataJetMETE_2022EE':DataJetMETE_2022EE, 'DataJetMETF_2022EE':DataJetMETF_2022EE, 'DataJetMETG_2022EE':DataJetMETG_2022EE,

    "DataMuon_2022":DataMuon_2022, "DataMuonC_2022":DataMuonC_2022, "DataMuonD_2022":DataMuonD_2022, 
    "DataMuon_2022EE":DataMuon_2022EE,
    "DataMuonE_2022EE":DataMuonE_2022EE, "DataMuonF_2022EE":DataMuonF_2022EE, "DataMuonG_2022EE":DataMuonG_2022EE,

    "DataEGamma_2022":DataEGamma_2022, "DataEGammaC_2022":DataEGammaC_2022, "DataEGammaD_2022":DataEGammaD_2022,
    "DataEGamma_2022EE":DataEGamma_2022EE, 
    "DataEGammaE_2022EE":DataEGammaE_2022EE, "DataEGammaF_2022EE":DataEGammaF_2022EE, "DataEGammaG_2022EE":DataEGammaG_2022EE,

    "DataJetMETC1_0_2023" : DataJetMETC1_0_2023, "DataJetMETC1_1_2023" : DataJetMETC1_1_2023,
    "DataJetMETC2_0_2023" : DataJetMETC2_0_2023, "DataJetMETC2_1_2023" : DataJetMETC2_1_2023,
    "DataJetMETC3_0_2023" : DataJetMETC3_0_2023, "DataJetMETC3_1_2023" : DataJetMETC3_1_2023,
    "DataJetMETC4_0_2023" : DataJetMETC4_0_2023, "DataJetMETC4_1_2023" : DataJetMETC4_1_2023,
    "DataJetMET_2023" : DataJetMET_2023,

    "DataJetMETD1_0_2023postBPix" : DataJetMETD1_0_2023postBPix, "DataJetMETD1_1_2023postBPix" : DataJetMETD1_1_2023postBPix,
    "DataJetMETD2_0_2023postBPix" : DataJetMETD2_0_2023postBPix, "DataJetMETD2_1_2023postBPix" : DataJetMETD2_1_2023postBPix,
    "DataJetMET_2023postBPix" : DataJetMET_2023postBPix,

    "DataMuonC1_0_2023" : DataMuonC1_0_2023, "DataMuonC1_1_2023" : DataMuonC1_1_2023,
    "DataMuonC2_0_2023" : DataMuonC2_0_2023, "DataMuonC2_1_2023" : DataMuonC2_1_2023,
    "DataMuonC3_0_2023" : DataMuonC3_0_2023, "DataMuonC3_1_2023" : DataMuonC3_1_2023,
    "DataMuonC4_0_2023" : DataMuonC4_0_2023, "DataMuonC4_1_2023" : DataMuonC4_1_2023,
    "DataMuon_2023" : DataMuon_2023,

    "DataMuonD1_0_2023postBPix" : DataMuonD1_0_2023postBPix, "DataMuonD1_1_2023postBPix" : DataMuonD1_1_2023postBPix,
    "DataMuonD2_0_2023postBPix" : DataMuonD2_0_2023postBPix, "DataMuonD2_1_2023postBPix" : DataMuonD2_1_2023postBPix,
    "DataMuon_2023postBPix" : DataMuon_2023postBPix,

    "DataEGammaC1_0_2023" : DataEGammaC1_0_2023, "DataEGammaC1_1_2023" : DataEGammaC1_1_2023,
    "DataEGammaC2_0_2023" : DataEGammaC2_0_2023, "DataEGammaC2_1_2023" : DataEGammaC2_1_2023,
    "DataEGammaC3_0_2023" : DataEGammaC3_0_2023, "DataEGammaC3_1_2023" : DataEGammaC3_1_2023,
    "DataEGammaC4_0_2023" : DataEGammaC4_0_2023, "DataEGammaC4_1_2023" : DataEGammaC4_1_2023,
    "DataEGamma_2023" : DataEGamma_2023,

    "DataEGammaD1_0_2023postBPix" : DataEGammaD1_0_2023postBPix, "DataEGammaD1_1_2023postBPix" : DataEGammaD1_1_2023postBPix,
    "DataEGammaD2_0_2023postBPix" : DataEGammaD2_0_2023postBPix, "DataEGammaD2_1_2023postBPix" : DataEGammaD2_1_2023postBPix,
    "DataEGamma_2023postBPix" : DataEGamma_2023postBPix,

    "DataJetMET_2024":      DataJetMET_2024,
    "DataJetMETC_0_2024":   DataJetMETC_0_2024,
    "DataJetMETC_1_2024":   DataJetMETC_1_2024,
    "DataJetMETD_0_2024":   DataJetMETD_0_2024,
    "DataJetMETD_1_2024":   DataJetMETD_1_2024,
    "DataJetMETE_0_2024":   DataJetMETE_0_2024,
    "DataJetMETE_1_2024":   DataJetMETE_1_2024,
    "DataJetMETF_0_2024":   DataJetMETF_0_2024,
    "DataJetMETF_1_2024":   DataJetMETF_1_2024,
    "DataJetMETG_0_2024":   DataJetMETG_0_2024,
    "DataJetMETG_1_2024":   DataJetMETG_1_2024,
    "DataJetMETH_0_2024":   DataJetMETH_0_2024,
    "DataJetMETH_1_2024":   DataJetMETH_1_2024,
    "DataJetMETI_0_2024":   DataJetMETI_0_2024,
    "DataJetMETI_1_2024":   DataJetMETI_1_2024,
    "DataJetMETI_2_2024":   DataJetMETI_2_2024,
    "DataJetMETI_3_2024":   DataJetMETI_3_2024,


    "DataMuon_2024":        DataMuon_2024,
    "DataMuonC_0_2024":     DataMuonC_0_2024,
    "DataMuonC_1_2024":     DataMuonC_1_2024,
    "DataMuonD_0_2024":     DataMuonD_0_2024,
    "DataMuonD_1_2024":     DataMuonD_1_2024,
    "DataMuonE_0_2024":     DataMuonE_0_2024,
    "DataMuonE_1_2024":     DataMuonE_1_2024,
    "DataMuonF_0_2024":     DataMuonF_0_2024,
    "DataMuonF_1_2024":     DataMuonF_1_2024,
    "DataMuonG_0_2024":     DataMuonG_0_2024,
    "DataMuonG_1_2024":     DataMuonG_1_2024,
    "DataMuonH_0_2024":     DataMuonH_0_2024,
    "DataMuonH_1_2024":     DataMuonH_1_2024,
    "DataMuonI_0_2024":     DataMuonI_0_2024,
    "DataMuonI_1_2024":     DataMuonI_1_2024,
    "DataMuonI_2_2024":     DataMuonI_2_2024,
    "DataMuonI_3_2024":     DataMuonI_3_2024,


    "DataEGamma_2024":      DataEGamma_2024,
    "DataEGammaC_0_2024":   DataEGammaC_0_2024,
    "DataEGammaC_1_2024":   DataEGammaC_1_2024,
    "DataEGammaD_0_2024":   DataEGammaD_0_2024,
    "DataEGammaD_1_2024":   DataEGammaD_1_2024,
    "DataEGammaE_0_2024":   DataEGammaE_0_2024,
    "DataEGammaE_1_2024":   DataEGammaE_1_2024,
    "DataEGammaF_0_2024":   DataEGammaF_0_2024,
    "DataEGammaF_1_2024":   DataEGammaF_1_2024,
    "DataEGammaG_0_2024":   DataEGammaG_0_2024,
    "DataEGammaG_1_2024":   DataEGammaG_1_2024,
    "DataEGammaH_0_2024":   DataEGammaH_0_2024,
    "DataEGammaH_1_2024":   DataEGammaH_1_2024,
    "DataEGammaI_0_2024":   DataEGammaI_0_2024,
    "DataEGammaI_1_2024":   DataEGammaI_1_2024,
    "DataEGammaI_2_2024":   DataEGammaI_2_2024,
    "DataEGammaI_3_2024":   DataEGammaI_3_2024,
    }
from samples_TDM_signal import samples_dict_tdm_signals
sample_dict.update(samples_dict_tdm_signals)
from samples_TPrime import *
sample_dict.update(samples_dict_tprime_signals)
