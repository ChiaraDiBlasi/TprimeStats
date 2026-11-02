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

################################  t-channel + DM - scalare ################################
TBDM_s_mPhi10_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=10)", "TBDM_s_mPhi10_mChi1_2024")
TBDM_s_mPhi10_mChi1_2024.sigma = 1.0
TBDM_s_mPhi10_mChi1_2024.year = 2024
TBDM_s_mPhi10_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-10_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi10_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi10_mChi1_2024.unix_code = 24000
TBDM_s_mPhi10_mChi1_2024.EE = 0

TBDM_s_mPhi50_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=50)", "TBDM_s_mPhi50_mChi1_2024")
TBDM_s_mPhi50_mChi1_2024.sigma = 1.0
TBDM_s_mPhi50_mChi1_2024.year = 2024
TBDM_s_mPhi50_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-50_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi50_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi50_mChi1_2024.unix_code = 24001
TBDM_s_mPhi50_mChi1_2024.EE = 0

TBDM_s_mPhi100_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=100)", "TBDM_s_mPhi100_mChi1_2024")
TBDM_s_mPhi100_mChi1_2024.sigma = 1.0
TBDM_s_mPhi100_mChi1_2024.year = 2024
TBDM_s_mPhi100_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi100_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi100_mChi1_2024.unix_code = 24002
TBDM_s_mPhi100_mChi1_2024.EE = 0

TBDM_s_mPhi150_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=150)", "TBDM_s_mPhi150_mChi1_2024")
TBDM_s_mPhi150_mChi1_2024.sigma = 1.0
TBDM_s_mPhi150_mChi1_2024.year = 2024
TBDM_s_mPhi150_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-150_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi150_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi150_mChi1_2024.unix_code = 24003
TBDM_s_mPhi150_mChi1_2024.EE = 0

TBDM_s_mPhi200_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=200)", "TBDM_s_mPhi200_mChi1_2024")
TBDM_s_mPhi200_mChi1_2024.sigma = 1.0
TBDM_s_mPhi200_mChi1_2024.year = 2024
TBDM_s_mPhi200_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi200_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi200_mChi1_2024.unix_code = 24004
TBDM_s_mPhi200_mChi1_2024.EE = 0

TBDM_s_mPhi250_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=250)", "TBDM_s_mPhi250_mChi1_2024")
TBDM_s_mPhi250_mChi1_2024.sigma = 1.0
TBDM_s_mPhi250_mChi1_2024.year = 2024
TBDM_s_mPhi250_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-250_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi250_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi250_mChi1_2024.unix_code = 24005
TBDM_s_mPhi250_mChi1_2024.EE = 0

TBDM_s_mPhi300_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=300)", "TBDM_s_mPhi300_mChi1_2024")
TBDM_s_mPhi300_mChi1_2024.sigma = 1.0
TBDM_s_mPhi300_mChi1_2024.year = 2024
TBDM_s_mPhi300_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi300_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi300_mChi1_2024.unix_code = 24006
TBDM_s_mPhi300_mChi1_2024.EE = 0

TBDM_s_mPhi350_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=350)", "TBDM_s_mPhi350_mChi1_2024")
TBDM_s_mPhi350_mChi1_2024.sigma = 1.0
TBDM_s_mPhi350_mChi1_2024.year = 2024
TBDM_s_mPhi350_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi350_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi350_mChi1_2024.unix_code = 24007
TBDM_s_mPhi350_mChi1_2024.EE = 0

TBDM_s_mPhi400_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=400)", "TBDM_s_mPhi400_mChi1_2024")
TBDM_s_mPhi400_mChi1_2024.sigma = 1.0
TBDM_s_mPhi400_mChi1_2024.year = 2024
TBDM_s_mPhi400_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi400_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi400_mChi1_2024.unix_code = 24008
TBDM_s_mPhi400_mChi1_2024.EE = 0

TBDM_s_mPhi500_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=500)", "TBDM_s_mPhi500_mChi1_2024")
TBDM_s_mPhi500_mChi1_2024.sigma = 1.0
TBDM_s_mPhi500_mChi1_2024.year = 2024
TBDM_s_mPhi500_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi500_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi500_mChi1_2024.unix_code = 24009
TBDM_s_mPhi500_mChi1_2024.EE = 0

TBDM_s_mPhi600_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=600)", "TBDM_s_mPhi600_mChi1_2024")
TBDM_s_mPhi600_mChi1_2024.sigma = 1.0
TBDM_s_mPhi600_mChi1_2024.year = 2024
TBDM_s_mPhi600_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi600_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi600_mChi1_2024.unix_code = 24010
TBDM_s_mPhi600_mChi1_2024.EE = 0

TBDM_s_mPhi700_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=700)", "TBDM_s_mPhi700_mChi1_2024")
TBDM_s_mPhi700_mChi1_2024.sigma = 1.0
TBDM_s_mPhi700_mChi1_2024.year = 2024
TBDM_s_mPhi700_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi700_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi700_mChi1_2024.unix_code = 24011
TBDM_s_mPhi700_mChi1_2024.EE = 0

TBDM_s_mPhi800_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=800)", "TBDM_s_mPhi800_mChi1_2024")
TBDM_s_mPhi800_mChi1_2024.sigma = 1.0
TBDM_s_mPhi800_mChi1_2024.year = 2024
TBDM_s_mPhi800_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi800_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi800_mChi1_2024.unix_code = 24012
TBDM_s_mPhi800_mChi1_2024.EE = 0

TBDM_s_mPhi1000_mChi1_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar (m_{#Phi}=1000)", "TBDM_s_mPhi1000_mChi1_2024")
TBDM_s_mPhi1000_mChi1_2024.sigma = 1.0
TBDM_s_mPhi1000_mChi1_2024.year = 2024
TBDM_s_mPhi1000_mChi1_2024.dataset = "/TBDMsimpSpin0-s_Par-mchi-1-mphi-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_s_mPhi1000_mChi1_2024.process = "TBDM_s_2024"
TBDM_s_mPhi1000_mChi1_2024.unix_code = 24013
TBDM_s_mPhi1000_mChi1_2024.EE = 0

TBDM_s_2024 = sample(ROOT.kGreen+2, 1, 1001, "TBDM scalar", "TBDM_s_2024")
TBDM_s_2024.year = 2024
TBDM_s_2024.components = [
    TBDM_s_mPhi10_mChi1_2024,
    TBDM_s_mPhi50_mChi1_2024,
    TBDM_s_mPhi100_mChi1_2024,
    TBDM_s_mPhi150_mChi1_2024,
    TBDM_s_mPhi200_mChi1_2024,
    TBDM_s_mPhi250_mChi1_2024,
    TBDM_s_mPhi300_mChi1_2024,
    TBDM_s_mPhi350_mChi1_2024,
    TBDM_s_mPhi400_mChi1_2024,
    TBDM_s_mPhi500_mChi1_2024,
    TBDM_s_mPhi600_mChi1_2024,
    TBDM_s_mPhi700_mChi1_2024,
    TBDM_s_mPhi800_mChi1_2024,
    TBDM_s_mPhi1000_mChi1_2024,
]

################################  t-channel + DM - psudoscalare ################################
TBDM_ps_mPhi10_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=10)", "TBDM_ps_mPhi10_mChi1_2024")
TBDM_ps_mPhi10_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi10_mChi1_2024.year = 2024
TBDM_ps_mPhi10_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-10_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi10_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi10_mChi1_2024.unix_code = 24100
TBDM_ps_mPhi10_mChi1_2024.EE = 0

TBDM_ps_mPhi50_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=50)", "TBDM_ps_mPhi50_mChi1_2024")
TBDM_ps_mPhi50_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi50_mChi1_2024.year = 2024
TBDM_ps_mPhi50_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-50_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi50_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi50_mChi1_2024.unix_code = 24101
TBDM_ps_mPhi50_mChi1_2024.EE = 0

TBDM_ps_mPhi100_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=100)", "TBDM_ps_mPhi100_mChi1_2024")
TBDM_ps_mPhi100_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi100_mChi1_2024.year = 2024
TBDM_ps_mPhi100_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi100_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi100_mChi1_2024.unix_code = 24102
TBDM_ps_mPhi100_mChi1_2024.EE = 0

TBDM_ps_mPhi150_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=150)", "TBDM_ps_mPhi150_mChi1_2024")
TBDM_ps_mPhi150_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi150_mChi1_2024.year = 2024
TBDM_ps_mPhi150_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-150_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi150_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi150_mChi1_2024.unix_code = 24103
TBDM_ps_mPhi150_mChi1_2024.EE = 0

TBDM_ps_mPhi200_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=200)", "TBDM_ps_mPhi200_mChi1_2024")
TBDM_ps_mPhi200_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi200_mChi1_2024.year = 2024
TBDM_ps_mPhi200_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi200_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi200_mChi1_2024.unix_code = 24104
TBDM_ps_mPhi200_mChi1_2024.EE = 0

TBDM_ps_mPhi250_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=250)", "TBDM_ps_mPhi250_mChi1_2024")
TBDM_ps_mPhi250_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi250_mChi1_2024.year = 2024
TBDM_ps_mPhi250_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-250_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi250_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi250_mChi1_2024.unix_code = 24105
TBDM_ps_mPhi250_mChi1_2024.EE = 0

TBDM_ps_mPhi300_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=300)", "TBDM_ps_mPhi300_mChi1_2024")
TBDM_ps_mPhi300_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi300_mChi1_2024.year = 2024
TBDM_ps_mPhi300_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi300_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi300_mChi1_2024.unix_code = 24106
TBDM_ps_mPhi300_mChi1_2024.EE = 0

TBDM_ps_mPhi350_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=350)", "TBDM_ps_mPhi350_mChi1_2024")
TBDM_ps_mPhi350_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi350_mChi1_2024.year = 2024
TBDM_ps_mPhi350_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi350_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi350_mChi1_2024.unix_code = 24107
TBDM_ps_mPhi350_mChi1_2024.EE = 0

TBDM_ps_mPhi400_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=400)", "TBDM_ps_mPhi400_mChi1_2024")
TBDM_ps_mPhi400_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi400_mChi1_2024.year = 2024
TBDM_ps_mPhi400_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi400_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi400_mChi1_2024.unix_code = 24108
TBDM_ps_mPhi400_mChi1_2024.EE = 0

TBDM_ps_mPhi500_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=500)", "TBDM_ps_mPhi500_mChi1_2024")
TBDM_ps_mPhi500_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi500_mChi1_2024.year = 2024
TBDM_ps_mPhi500_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi500_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi500_mChi1_2024.unix_code = 24109
TBDM_ps_mPhi500_mChi1_2024.EE = 0

TBDM_ps_mPhi600_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=600)", "TBDM_ps_mPhi600_mChi1_2024")
TBDM_ps_mPhi600_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi600_mChi1_2024.year = 2024
TBDM_ps_mPhi600_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi600_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi600_mChi1_2024.unix_code = 24110
TBDM_ps_mPhi600_mChi1_2024.EE = 0

TBDM_ps_mPhi700_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=700)", "TBDM_ps_mPhi700_mChi1_2024")
TBDM_ps_mPhi700_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi700_mChi1_2024.year = 2024
TBDM_ps_mPhi700_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi700_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi700_mChi1_2024.unix_code = 24111
TBDM_ps_mPhi700_mChi1_2024.EE = 0

TBDM_ps_mPhi800_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=800)", "TBDM_ps_mPhi800_mChi1_2024")
TBDM_ps_mPhi800_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi800_mChi1_2024.year = 2024
TBDM_ps_mPhi800_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi800_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi800_mChi1_2024.unix_code = 24112
TBDM_ps_mPhi800_mChi1_2024.EE = 0

TBDM_ps_mPhi1000_mChi1_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar (m_{#Phi}=1000)", "TBDM_ps_mPhi1000_mChi1_2024")
TBDM_ps_mPhi1000_mChi1_2024.sigma = 1.0
TBDM_ps_mPhi1000_mChi1_2024.year = 2024
TBDM_ps_mPhi1000_mChi1_2024.dataset = "/TBDMsimpSpin0-ps_Par-mchi-1-mphi-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TBDM_ps_mPhi1000_mChi1_2024.process = "TBDM_ps_2024"
TBDM_ps_mPhi1000_mChi1_2024.unix_code = 24113
TBDM_ps_mPhi1000_mChi1_2024.EE = 0

TBDM_ps_2024 = sample(ROOT.kGreen+3, 1, 1001, "TBDM pseudoscalar", "TBDM_ps_2024")
TBDM_ps_2024.year = 2024
TBDM_ps_2024.components = [
    TBDM_ps_mPhi10_mChi1_2024,
    TBDM_ps_mPhi50_mChi1_2024,
    TBDM_ps_mPhi100_mChi1_2024,
    TBDM_ps_mPhi150_mChi1_2024,
    TBDM_ps_mPhi200_mChi1_2024,
    TBDM_ps_mPhi250_mChi1_2024,
    TBDM_ps_mPhi300_mChi1_2024,
    TBDM_ps_mPhi350_mChi1_2024,
    TBDM_ps_mPhi400_mChi1_2024,
    TBDM_ps_mPhi500_mChi1_2024,
    TBDM_ps_mPhi600_mChi1_2024,
    TBDM_ps_mPhi700_mChi1_2024,
    TBDM_ps_mPhi800_mChi1_2024,
    TBDM_ps_mPhi1000_mChi1_2024,
]



################################  TW + DM - scalare ################################
TWDM_s_mPhi10_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=10)", "TWDM_s_mPhi10_mChi1_2024")
TWDM_s_mPhi10_mChi1_2024.sigma = 1.0
TWDM_s_mPhi10_mChi1_2024.year = 2024
TWDM_s_mPhi10_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-10_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi10_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi10_mChi1_2024.unix_code = 24200
TWDM_s_mPhi10_mChi1_2024.EE = 0

TWDM_s_mPhi50_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=50)", "TWDM_s_mPhi50_mChi1_2024")
TWDM_s_mPhi50_mChi1_2024.sigma = 1.0
TWDM_s_mPhi50_mChi1_2024.year = 2024
TWDM_s_mPhi50_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-50_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi50_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi50_mChi1_2024.unix_code = 24201
TWDM_s_mPhi50_mChi1_2024.EE = 0

TWDM_s_mPhi100_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=100)", "TWDM_s_mPhi100_mChi1_2024")
TWDM_s_mPhi100_mChi1_2024.sigma = 1.0
TWDM_s_mPhi100_mChi1_2024.year = 2024
TWDM_s_mPhi100_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi100_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi100_mChi1_2024.unix_code = 24202
TWDM_s_mPhi100_mChi1_2024.EE = 0

TWDM_s_mPhi150_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=150)", "TWDM_s_mPhi150_mChi1_2024")
TWDM_s_mPhi150_mChi1_2024.sigma = 1.0
TWDM_s_mPhi150_mChi1_2024.year = 2024
TWDM_s_mPhi150_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-150_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi150_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi150_mChi1_2024.unix_code = 24203
TWDM_s_mPhi150_mChi1_2024.EE = 0

TWDM_s_mPhi200_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=200)", "TWDM_s_mPhi200_mChi1_2024")
TWDM_s_mPhi200_mChi1_2024.sigma = 1.0
TWDM_s_mPhi200_mChi1_2024.year = 2024
TWDM_s_mPhi200_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi200_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi200_mChi1_2024.unix_code = 24204
TWDM_s_mPhi200_mChi1_2024.EE = 0

TWDM_s_mPhi250_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=250)", "TWDM_s_mPhi250_mChi1_2024")
TWDM_s_mPhi250_mChi1_2024.sigma = 1.0
TWDM_s_mPhi250_mChi1_2024.year = 2024
TWDM_s_mPhi250_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-250_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi250_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi250_mChi1_2024.unix_code = 24205
TWDM_s_mPhi250_mChi1_2024.EE = 0

TWDM_s_mPhi300_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=300)", "TWDM_s_mPhi300_mChi1_2024")
TWDM_s_mPhi300_mChi1_2024.sigma = 1.0
TWDM_s_mPhi300_mChi1_2024.year = 2024
TWDM_s_mPhi300_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi300_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi300_mChi1_2024.unix_code = 24206
TWDM_s_mPhi300_mChi1_2024.EE = 0

TWDM_s_mPhi350_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=350)", "TWDM_s_mPhi350_mChi1_2024")
TWDM_s_mPhi350_mChi1_2024.sigma = 1.0
TWDM_s_mPhi350_mChi1_2024.year = 2024
TWDM_s_mPhi350_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi350_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi350_mChi1_2024.unix_code = 24207
TWDM_s_mPhi350_mChi1_2024.EE = 0

TWDM_s_mPhi400_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=400)", "TWDM_s_mPhi400_mChi1_2024")
TWDM_s_mPhi400_mChi1_2024.sigma = 1.0
TWDM_s_mPhi400_mChi1_2024.year = 2024
TWDM_s_mPhi400_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi400_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi400_mChi1_2024.unix_code = 24208
TWDM_s_mPhi400_mChi1_2024.EE = 0

TWDM_s_mPhi500_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=500)", "TWDM_s_mPhi500_mChi1_2024")
TWDM_s_mPhi500_mChi1_2024.sigma = 1.0
TWDM_s_mPhi500_mChi1_2024.year = 2024
TWDM_s_mPhi500_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi500_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi500_mChi1_2024.unix_code = 24209
TWDM_s_mPhi500_mChi1_2024.EE = 0

TWDM_s_mPhi600_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=600)", "TWDM_s_mPhi600_mChi1_2024")
TWDM_s_mPhi600_mChi1_2024.sigma = 1.0
TWDM_s_mPhi600_mChi1_2024.year = 2024
TWDM_s_mPhi600_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi600_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi600_mChi1_2024.unix_code = 24210
TWDM_s_mPhi600_mChi1_2024.EE = 0

TWDM_s_mPhi700_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=700)", "TWDM_s_mPhi700_mChi1_2024")
TWDM_s_mPhi700_mChi1_2024.sigma = 1.0
TWDM_s_mPhi700_mChi1_2024.year = 2024
TWDM_s_mPhi700_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi700_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi700_mChi1_2024.unix_code = 24211
TWDM_s_mPhi700_mChi1_2024.EE = 0

TWDM_s_mPhi800_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=800)", "TWDM_s_mPhi800_mChi1_2024")
TWDM_s_mPhi800_mChi1_2024.sigma = 1.0
TWDM_s_mPhi800_mChi1_2024.year = 2024
TWDM_s_mPhi800_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi800_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi800_mChi1_2024.unix_code = 24212
TWDM_s_mPhi800_mChi1_2024.EE = 0

TWDM_s_mPhi1000_mChi1_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar (m_{#Phi}=1000)", "TWDM_s_mPhi1000_mChi1_2024")
TWDM_s_mPhi1000_mChi1_2024.sigma = 1.0
TWDM_s_mPhi1000_mChi1_2024.year = 2024
TWDM_s_mPhi1000_mChi1_2024.dataset = "/TWDMsimpSpin0-s_Par-mchi-1-mphi-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_s_mPhi1000_mChi1_2024.process = "TWDM_s_2024"
TWDM_s_mPhi1000_mChi1_2024.unix_code = 24213
TWDM_s_mPhi1000_mChi1_2024.EE = 0

TWDM_s_2024 = sample(ROOT.kBlue+1, 1, 1001, "TWDM scalar", "TWDM_s_2024")
TWDM_s_2024.year = 2024
TWDM_s_2024.components = [
    TWDM_s_mPhi10_mChi1_2024,
    TWDM_s_mPhi50_mChi1_2024,
    TWDM_s_mPhi100_mChi1_2024,
    TWDM_s_mPhi150_mChi1_2024,
    TWDM_s_mPhi200_mChi1_2024,
    TWDM_s_mPhi250_mChi1_2024,
    TWDM_s_mPhi300_mChi1_2024,
    TWDM_s_mPhi350_mChi1_2024,
    TWDM_s_mPhi400_mChi1_2024,
    TWDM_s_mPhi500_mChi1_2024,
    TWDM_s_mPhi600_mChi1_2024,
    TWDM_s_mPhi700_mChi1_2024,
    TWDM_s_mPhi800_mChi1_2024,
    TWDM_s_mPhi1000_mChi1_2024,
]

################################  TW + DM - psudoscalare ################################

TWDM_ps_mPhi10_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=10)", "TWDM_ps_mPhi10_mChi1_2024")
TWDM_ps_mPhi10_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi10_mChi1_2024.year = 2024
TWDM_ps_mPhi10_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-10_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi10_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi10_mChi1_2024.unix_code = 24300
TWDM_ps_mPhi10_mChi1_2024.EE = 0

TWDM_ps_mPhi50_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=50)", "TWDM_ps_mPhi50_mChi1_2024")
TWDM_ps_mPhi50_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi50_mChi1_2024.year = 2024
TWDM_ps_mPhi50_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-50_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi50_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi50_mChi1_2024.unix_code = 24301
TWDM_ps_mPhi50_mChi1_2024.EE = 0

TWDM_ps_mPhi100_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=100)", "TWDM_ps_mPhi100_mChi1_2024")
TWDM_ps_mPhi100_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi100_mChi1_2024.year = 2024
TWDM_ps_mPhi100_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi100_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi100_mChi1_2024.unix_code = 24302
TWDM_ps_mPhi100_mChi1_2024.EE = 0

TWDM_ps_mPhi150_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=150)", "TWDM_ps_mPhi150_mChi1_2024")
TWDM_ps_mPhi150_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi150_mChi1_2024.year = 2024
TWDM_ps_mPhi150_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-150_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi150_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi150_mChi1_2024.unix_code = 24303
TWDM_ps_mPhi150_mChi1_2024.EE = 0

TWDM_ps_mPhi200_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=200)", "TWDM_ps_mPhi200_mChi1_2024")
TWDM_ps_mPhi200_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi200_mChi1_2024.year = 2024
TWDM_ps_mPhi200_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi200_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi200_mChi1_2024.unix_code = 24304
TWDM_ps_mPhi200_mChi1_2024.EE = 0

TWDM_ps_mPhi250_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=250)", "TWDM_ps_mPhi250_mChi1_2024")
TWDM_ps_mPhi250_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi250_mChi1_2024.year = 2024
TWDM_ps_mPhi250_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-250_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi250_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi250_mChi1_2024.unix_code = 24305
TWDM_ps_mPhi250_mChi1_2024.EE = 0

TWDM_ps_mPhi300_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=300)", "TWDM_ps_mPhi300_mChi1_2024")
TWDM_ps_mPhi300_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi300_mChi1_2024.year = 2024
TWDM_ps_mPhi300_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi300_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi300_mChi1_2024.unix_code = 24306
TWDM_ps_mPhi300_mChi1_2024.EE = 0

TWDM_ps_mPhi350_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=350)", "TWDM_ps_mPhi350_mChi1_2024")
TWDM_ps_mPhi350_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi350_mChi1_2024.year = 2024
TWDM_ps_mPhi350_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi350_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi350_mChi1_2024.unix_code = 24307
TWDM_ps_mPhi350_mChi1_2024.EE = 0

TWDM_ps_mPhi400_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=400)", "TWDM_ps_mPhi400_mChi1_2024")
TWDM_ps_mPhi400_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi400_mChi1_2024.year = 2024
TWDM_ps_mPhi400_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi400_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi400_mChi1_2024.unix_code = 24308
TWDM_ps_mPhi400_mChi1_2024.EE = 0

TWDM_ps_mPhi500_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=500)", "TWDM_ps_mPhi500_mChi1_2024")
TWDM_ps_mPhi500_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi500_mChi1_2024.year = 2024
TWDM_ps_mPhi500_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi500_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi500_mChi1_2024.unix_code = 24309
TWDM_ps_mPhi500_mChi1_2024.EE = 0

TWDM_ps_mPhi600_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=600)", "TWDM_ps_mPhi600_mChi1_2024")
TWDM_ps_mPhi600_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi600_mChi1_2024.year = 2024
TWDM_ps_mPhi600_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi600_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi600_mChi1_2024.unix_code = 24310
TWDM_ps_mPhi600_mChi1_2024.EE = 0

TWDM_ps_mPhi700_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=700)", "TWDM_ps_mPhi700_mChi1_2024")
TWDM_ps_mPhi700_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi700_mChi1_2024.year = 2024
TWDM_ps_mPhi700_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi700_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi700_mChi1_2024.unix_code = 24311
TWDM_ps_mPhi700_mChi1_2024.EE = 0

TWDM_ps_mPhi800_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=800)", "TWDM_ps_mPhi800_mChi1_2024")
TWDM_ps_mPhi800_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi800_mChi1_2024.year = 2024
TWDM_ps_mPhi800_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi800_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi800_mChi1_2024.unix_code = 24312
TWDM_ps_mPhi800_mChi1_2024.EE = 0

TWDM_ps_mPhi1000_mChi1_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar (m_{#Phi}=1000)", "TWDM_ps_mPhi1000_mChi1_2024")
TWDM_ps_mPhi1000_mChi1_2024.sigma = 1.0
TWDM_ps_mPhi1000_mChi1_2024.year = 2024
TWDM_ps_mPhi1000_mChi1_2024.dataset = "/TWDMsimpSpin0-ps_Par-mchi-1-mphi-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWDM_ps_mPhi1000_mChi1_2024.process = "TWDM_ps_2024"
TWDM_ps_mPhi1000_mChi1_2024.unix_code = 24313
TWDM_ps_mPhi1000_mChi1_2024.EE = 0

TWDM_ps_2024 = sample(ROOT.kBlue+2, 1, 1001, "TWDM pseudoscalar", "TWDM_ps_2024")
TWDM_ps_2024.year = 2024
TWDM_ps_2024.components = [
    TWDM_ps_mPhi10_mChi1_2024,
    TWDM_ps_mPhi50_mChi1_2024,
    TWDM_ps_mPhi100_mChi1_2024,
    TWDM_ps_mPhi150_mChi1_2024,
    TWDM_ps_mPhi200_mChi1_2024,
    TWDM_ps_mPhi250_mChi1_2024,
    TWDM_ps_mPhi300_mChi1_2024,
    TWDM_ps_mPhi350_mChi1_2024,
    TWDM_ps_mPhi400_mChi1_2024,
    TWDM_ps_mPhi500_mChi1_2024,
    TWDM_ps_mPhi600_mChi1_2024,
    TWDM_ps_mPhi700_mChi1_2024,
    TWDM_ps_mPhi800_mChi1_2024,
    TWDM_ps_mPhi1000_mChi1_2024,
]

################################  TW + DM - dileptonico - scalare ################################

TWto2LDM_s_mPhi10_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=10)", "TWto2LDM_s_mPhi10_mChi1_2024")
TWto2LDM_s_mPhi10_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi10_mChi1_2024.year = 2024
TWto2LDM_s_mPhi10_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-10_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi10_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi10_mChi1_2024.unix_code = 24400
TWto2LDM_s_mPhi10_mChi1_2024.EE = 0

TWto2LDM_s_mPhi50_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=50)", "TWto2LDM_s_mPhi50_mChi1_2024")
TWto2LDM_s_mPhi50_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi50_mChi1_2024.year = 2024
TWto2LDM_s_mPhi50_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-50_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi50_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi50_mChi1_2024.unix_code = 24401
TWto2LDM_s_mPhi50_mChi1_2024.EE = 0

TWto2LDM_s_mPhi100_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=100)", "TWto2LDM_s_mPhi100_mChi1_2024")
TWto2LDM_s_mPhi100_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi100_mChi1_2024.year = 2024
TWto2LDM_s_mPhi100_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi100_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi100_mChi1_2024.unix_code = 24402
TWto2LDM_s_mPhi100_mChi1_2024.EE = 0

TWto2LDM_s_mPhi150_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=150)", "TWto2LDM_s_mPhi150_mChi1_2024")
TWto2LDM_s_mPhi150_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi150_mChi1_2024.year = 2024
TWto2LDM_s_mPhi150_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-150_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi150_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi150_mChi1_2024.unix_code = 24403
TWto2LDM_s_mPhi150_mChi1_2024.EE = 0

TWto2LDM_s_mPhi200_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=200)", "TWto2LDM_s_mPhi200_mChi1_2024")
TWto2LDM_s_mPhi200_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi200_mChi1_2024.year = 2024
TWto2LDM_s_mPhi200_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi200_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi200_mChi1_2024.unix_code = 24404
TWto2LDM_s_mPhi200_mChi1_2024.EE = 0

TWto2LDM_s_mPhi250_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=250)", "TWto2LDM_s_mPhi250_mChi1_2024")
TWto2LDM_s_mPhi250_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi250_mChi1_2024.year = 2024
TWto2LDM_s_mPhi250_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-250_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi250_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi250_mChi1_2024.unix_code = 24405
TWto2LDM_s_mPhi250_mChi1_2024.EE = 0

TWto2LDM_s_mPhi300_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=300)", "TWto2LDM_s_mPhi300_mChi1_2024")
TWto2LDM_s_mPhi300_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi300_mChi1_2024.year = 2024
TWto2LDM_s_mPhi300_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi300_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi300_mChi1_2024.unix_code = 24406
TWto2LDM_s_mPhi300_mChi1_2024.EE = 0

TWto2LDM_s_mPhi350_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=350)", "TWto2LDM_s_mPhi350_mChi1_2024")
TWto2LDM_s_mPhi350_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi350_mChi1_2024.year = 2024
TWto2LDM_s_mPhi350_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi350_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi350_mChi1_2024.unix_code = 24407
TWto2LDM_s_mPhi350_mChi1_2024.EE = 0

TWto2LDM_s_mPhi400_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=400)", "TWto2LDM_s_mPhi400_mChi1_2024")
TWto2LDM_s_mPhi400_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi400_mChi1_2024.year = 2024
TWto2LDM_s_mPhi400_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi400_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi400_mChi1_2024.unix_code = 24408
TWto2LDM_s_mPhi400_mChi1_2024.EE = 0

TWto2LDM_s_mPhi500_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=500)", "TWto2LDM_s_mPhi500_mChi1_2024")
TWto2LDM_s_mPhi500_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi500_mChi1_2024.year = 2024
TWto2LDM_s_mPhi500_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi500_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi500_mChi1_2024.unix_code = 24409
TWto2LDM_s_mPhi500_mChi1_2024.EE = 0

TWto2LDM_s_mPhi600_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=600)", "TWto2LDM_s_mPhi600_mChi1_2024")
TWto2LDM_s_mPhi600_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi600_mChi1_2024.year = 2024
TWto2LDM_s_mPhi600_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi600_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi600_mChi1_2024.unix_code = 24410
TWto2LDM_s_mPhi600_mChi1_2024.EE = 0

TWto2LDM_s_mPhi700_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=700)", "TWto2LDM_s_mPhi700_mChi1_2024")
TWto2LDM_s_mPhi700_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi700_mChi1_2024.year = 2024
TWto2LDM_s_mPhi700_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi700_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi700_mChi1_2024.unix_code = 24411
TWto2LDM_s_mPhi700_mChi1_2024.EE = 0

TWto2LDM_s_mPhi800_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=800)", "TWto2LDM_s_mPhi800_mChi1_2024")
TWto2LDM_s_mPhi800_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi800_mChi1_2024.year = 2024
TWto2LDM_s_mPhi800_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi800_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi800_mChi1_2024.unix_code = 24412
TWto2LDM_s_mPhi800_mChi1_2024.EE = 0

TWto2LDM_s_mPhi1000_mChi1_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar (m_{#Phi}=1000)", "TWto2LDM_s_mPhi1000_mChi1_2024")
TWto2LDM_s_mPhi1000_mChi1_2024.sigma = 1.0
TWto2LDM_s_mPhi1000_mChi1_2024.year = 2024
TWto2LDM_s_mPhi1000_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-s_Par-mchi-1-mphi-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_s_mPhi1000_mChi1_2024.process = "TWto2LDM_s_2024"
TWto2LDM_s_mPhi1000_mChi1_2024.unix_code = 24413
TWto2LDM_s_mPhi1000_mChi1_2024.EE = 0

TWto2LDM_s_2024 = sample(ROOT.kMagenta+1, 1, 1001, "TW to 2L DM scalar", "TWto2LDM_s_2024")
TWto2LDM_s_2024.year = 2024
TWto2LDM_s_2024.components = [
    TWto2LDM_s_mPhi10_mChi1_2024,
    TWto2LDM_s_mPhi50_mChi1_2024,
    TWto2LDM_s_mPhi100_mChi1_2024,
    TWto2LDM_s_mPhi150_mChi1_2024,
    TWto2LDM_s_mPhi200_mChi1_2024,
    TWto2LDM_s_mPhi250_mChi1_2024,
    TWto2LDM_s_mPhi300_mChi1_2024,
    TWto2LDM_s_mPhi350_mChi1_2024,
    TWto2LDM_s_mPhi400_mChi1_2024,
    TWto2LDM_s_mPhi500_mChi1_2024,
    TWto2LDM_s_mPhi600_mChi1_2024,
    TWto2LDM_s_mPhi700_mChi1_2024,
    TWto2LDM_s_mPhi800_mChi1_2024,
    TWto2LDM_s_mPhi1000_mChi1_2024,
]

################################  TW + DM - dileptonico - psudoscalare ################################
TWto2LDM_ps_mPhi10_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=10)", "TWto2LDM_ps_mPhi10_mChi1_2024")
TWto2LDM_ps_mPhi10_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi10_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi10_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-10_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi10_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi10_mChi1_2024.unix_code = 24500
TWto2LDM_ps_mPhi10_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi50_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=50)", "TWto2LDM_ps_mPhi50_mChi1_2024")
TWto2LDM_ps_mPhi50_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi50_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi50_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-50_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi50_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi50_mChi1_2024.unix_code = 24501
TWto2LDM_ps_mPhi50_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi100_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=100)", "TWto2LDM_ps_mPhi100_mChi1_2024")
TWto2LDM_ps_mPhi100_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi100_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi100_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi100_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi100_mChi1_2024.unix_code = 24502
TWto2LDM_ps_mPhi100_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi150_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=150)", "TWto2LDM_ps_mPhi150_mChi1_2024")
TWto2LDM_ps_mPhi150_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi150_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi150_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-150_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi150_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi150_mChi1_2024.unix_code = 24503
TWto2LDM_ps_mPhi150_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi200_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=200)", "TWto2LDM_ps_mPhi200_mChi1_2024")
TWto2LDM_ps_mPhi200_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi200_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi200_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi200_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi200_mChi1_2024.unix_code = 24504
TWto2LDM_ps_mPhi200_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi250_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=250)", "TWto2LDM_ps_mPhi250_mChi1_2024")
TWto2LDM_ps_mPhi250_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi250_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi250_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-250_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi250_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi250_mChi1_2024.unix_code = 24505
TWto2LDM_ps_mPhi250_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi300_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=300)", "TWto2LDM_ps_mPhi300_mChi1_2024")
TWto2LDM_ps_mPhi300_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi300_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi300_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi300_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi300_mChi1_2024.unix_code = 24506
TWto2LDM_ps_mPhi300_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi350_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=350)", "TWto2LDM_ps_mPhi350_mChi1_2024")
TWto2LDM_ps_mPhi350_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi350_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi350_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi350_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi350_mChi1_2024.unix_code = 24507
TWto2LDM_ps_mPhi350_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi400_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=400)", "TWto2LDM_ps_mPhi400_mChi1_2024")
TWto2LDM_ps_mPhi400_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi400_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi400_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi400_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi400_mChi1_2024.unix_code = 24508
TWto2LDM_ps_mPhi400_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi500_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=500)", "TWto2LDM_ps_mPhi500_mChi1_2024")
TWto2LDM_ps_mPhi500_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi500_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi500_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi500_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi500_mChi1_2024.unix_code = 24509
TWto2LDM_ps_mPhi500_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi600_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=600)", "TWto2LDM_ps_mPhi600_mChi1_2024")
TWto2LDM_ps_mPhi600_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi600_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi600_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi600_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi600_mChi1_2024.unix_code = 24510
TWto2LDM_ps_mPhi600_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi700_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=700)", "TWto2LDM_ps_mPhi700_mChi1_2024")
TWto2LDM_ps_mPhi700_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi700_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi700_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi700_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi700_mChi1_2024.unix_code = 24511
TWto2LDM_ps_mPhi700_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi800_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=800)", "TWto2LDM_ps_mPhi800_mChi1_2024")
TWto2LDM_ps_mPhi800_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi800_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi800_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi800_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi800_mChi1_2024.unix_code = 24512
TWto2LDM_ps_mPhi800_mChi1_2024.EE = 0

TWto2LDM_ps_mPhi1000_mChi1_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar (m_{#Phi}=1000)", "TWto2LDM_ps_mPhi1000_mChi1_2024")
TWto2LDM_ps_mPhi1000_mChi1_2024.sigma = 1.0
TWto2LDM_ps_mPhi1000_mChi1_2024.year = 2024
TWto2LDM_ps_mPhi1000_mChi1_2024.dataset = "/TWto2LDMsimpSpin0-ps_Par-mchi-1-mphi-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TWto2LDM_ps_mPhi1000_mChi1_2024.process = "TWto2LDM_ps_2024"
TWto2LDM_ps_mPhi1000_mChi1_2024.unix_code = 24513
TWto2LDM_ps_mPhi1000_mChi1_2024.EE = 0

TWto2LDM_ps_2024 = sample(ROOT.kMagenta+2, 1, 1001, "TW to 2L DM pseudoscalar", "TWto2LDM_ps_2024")
TWto2LDM_ps_2024.year = 2024
TWto2LDM_ps_2024.components = [
    TWto2LDM_ps_mPhi10_mChi1_2024,
    TWto2LDM_ps_mPhi50_mChi1_2024,
    TWto2LDM_ps_mPhi100_mChi1_2024,
    TWto2LDM_ps_mPhi150_mChi1_2024,
    TWto2LDM_ps_mPhi200_mChi1_2024,
    TWto2LDM_ps_mPhi250_mChi1_2024,
    TWto2LDM_ps_mPhi300_mChi1_2024,
    TWto2LDM_ps_mPhi350_mChi1_2024,
    TWto2LDM_ps_mPhi400_mChi1_2024,
    TWto2LDM_ps_mPhi500_mChi1_2024,
    TWto2LDM_ps_mPhi600_mChi1_2024,
    TWto2LDM_ps_mPhi700_mChi1_2024,
    TWto2LDM_ps_mPhi800_mChi1_2024,
    TWto2LDM_ps_mPhi1000_mChi1_2024,
]

##################### TTDM_s_2024

TTDM_s_mPhi10_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=10)", "TTDM_s_mPhi10_mChi1_2024")
TTDM_s_mPhi10_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi10_mChi1_2024.year = 2024
TTDM_s_mPhi10_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-10_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi10_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi10_mChi1_2024.unix_code = 24600
TTDM_s_mPhi10_mChi1_2024.EE = 0

TTDM_s_mPhi50_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=50)", "TTDM_s_mPhi50_mChi1_2024")
TTDM_s_mPhi50_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi50_mChi1_2024.year = 2024
TTDM_s_mPhi50_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi50_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi50_mChi1_2024.unix_code = 24601
TTDM_s_mPhi50_mChi1_2024.EE = 0

TTDM_s_mPhi100_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=100)", "TTDM_s_mPhi100_mChi1_2024")
TTDM_s_mPhi100_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi100_mChi1_2024.year = 2024
TTDM_s_mPhi100_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-100_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi100_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi100_mChi1_2024.unix_code = 24602
TTDM_s_mPhi100_mChi1_2024.EE = 0

TTDM_s_mPhi150_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=150)", "TTDM_s_mPhi150_mChi1_2024")
TTDM_s_mPhi150_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi150_mChi1_2024.year = 2024
TTDM_s_mPhi150_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-150_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi150_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi150_mChi1_2024.unix_code = 24603
TTDM_s_mPhi150_mChi1_2024.EE = 0

TTDM_s_mPhi200_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=200)", "TTDM_s_mPhi200_mChi1_2024")
TTDM_s_mPhi200_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi200_mChi1_2024.year = 2024
TTDM_s_mPhi200_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi200_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi200_mChi1_2024.unix_code = 24604
TTDM_s_mPhi200_mChi1_2024.EE = 0

TTDM_s_mPhi250_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=250)", "TTDM_s_mPhi250_mChi1_2024")
TTDM_s_mPhi250_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi250_mChi1_2024.year = 2024
TTDM_s_mPhi250_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-250_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi250_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi250_mChi1_2024.unix_code = 24605
TTDM_s_mPhi250_mChi1_2024.EE = 0

TTDM_s_mPhi300_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=300)", "TTDM_s_mPhi300_mChi1_2024")
TTDM_s_mPhi300_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi300_mChi1_2024.year = 2024
TTDM_s_mPhi300_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-300_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi300_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi300_mChi1_2024.unix_code = 24606
TTDM_s_mPhi300_mChi1_2024.EE = 0

TTDM_s_mPhi350_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=350)", "TTDM_s_mPhi350_mChi1_2024")
TTDM_s_mPhi350_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi350_mChi1_2024.year = 2024
TTDM_s_mPhi350_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-350_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi350_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi350_mChi1_2024.unix_code = 24607
TTDM_s_mPhi350_mChi1_2024.EE = 0

TTDM_s_mPhi400_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=400)", "TTDM_s_mPhi400_mChi1_2024")
TTDM_s_mPhi400_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi400_mChi1_2024.year = 2024
TTDM_s_mPhi400_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi400_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi400_mChi1_2024.unix_code = 24608
TTDM_s_mPhi400_mChi1_2024.EE = 0

TTDM_s_mPhi500_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=500)", "TTDM_s_mPhi500_mChi1_2024")
TTDM_s_mPhi500_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi500_mChi1_2024.year = 2024
TTDM_s_mPhi500_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi500_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi500_mChi1_2024.unix_code = 24609
TTDM_s_mPhi500_mChi1_2024.EE = 0

TTDM_s_mPhi600_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=600)", "TTDM_s_mPhi600_mChi1_2024")
TTDM_s_mPhi600_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi600_mChi1_2024.year = 2024
TTDM_s_mPhi600_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi600_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi600_mChi1_2024.unix_code = 24610
TTDM_s_mPhi600_mChi1_2024.EE = 0

TTDM_s_mPhi700_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=700)", "TTDM_s_mPhi700_mChi1_2024")
TTDM_s_mPhi700_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi700_mChi1_2024.year = 2024
TTDM_s_mPhi700_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-700_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi700_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi700_mChi1_2024.unix_code = 24611
TTDM_s_mPhi700_mChi1_2024.EE = 0

TTDM_s_mPhi800_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=800)", "TTDM_s_mPhi800_mChi1_2024")
TTDM_s_mPhi800_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi800_mChi1_2024.year = 2024
TTDM_s_mPhi800_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi800_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi800_mChi1_2024.unix_code = 24612
TTDM_s_mPhi800_mChi1_2024.EE = 0

TTDM_s_mPhi1000_mChi1_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar (m_{#Phi}=1000)", "TTDM_s_mPhi1000_mChi1_2024")
TTDM_s_mPhi1000_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_s_mPhi1000_mChi1_2024.year = 2024
TTDM_s_mPhi1000_mChi1_2024.dataset = "/TTDMsimpSpin0-s_Par-mchi-1-mphi-1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_s_mPhi1000_mChi1_2024.process = "TTDM_s_2024"
TTDM_s_mPhi1000_mChi1_2024.unix_code = 24613
TTDM_s_mPhi1000_mChi1_2024.EE = 0

##################### TTDM_ps_2024

TTDM_ps_mPhi10_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=10)", "TTDM_ps_mPhi10_mChi1_2024")
TTDM_ps_mPhi10_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi10_mChi1_2024.year = 2024
TTDM_ps_mPhi10_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-10_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi10_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi10_mChi1_2024.unix_code = 24700
TTDM_ps_mPhi10_mChi1_2024.EE = 0

TTDM_ps_mPhi50_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=50)", "TTDM_ps_mPhi50_mChi1_2024")
TTDM_ps_mPhi50_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi50_mChi1_2024.year = 2024
TTDM_ps_mPhi50_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi50_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi50_mChi1_2024.unix_code = 24701
TTDM_ps_mPhi50_mChi1_2024.EE = 0

TTDM_ps_mPhi100_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=100)", "TTDM_ps_mPhi100_mChi1_2024")
TTDM_ps_mPhi100_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi100_mChi1_2024.year = 2024
TTDM_ps_mPhi100_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-100_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi100_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi100_mChi1_2024.unix_code = 24702
TTDM_ps_mPhi100_mChi1_2024.EE = 0

TTDM_ps_mPhi150_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=150)", "TTDM_ps_mPhi150_mChi1_2024")
TTDM_ps_mPhi150_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi150_mChi1_2024.year = 2024
TTDM_ps_mPhi150_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-150_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi150_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi150_mChi1_2024.unix_code = 24703
TTDM_ps_mPhi150_mChi1_2024.EE = 0

TTDM_ps_mPhi200_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=200)", "TTDM_ps_mPhi200_mChi1_2024")
TTDM_ps_mPhi200_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi200_mChi1_2024.year = 2024
TTDM_ps_mPhi200_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi200_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi200_mChi1_2024.unix_code = 24704
TTDM_ps_mPhi200_mChi1_2024.EE = 0

TTDM_ps_mPhi250_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=250)", "TTDM_ps_mPhi250_mChi1_2024")
TTDM_ps_mPhi250_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi250_mChi1_2024.year = 2024
TTDM_ps_mPhi250_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-250_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi250_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi250_mChi1_2024.unix_code = 24705
TTDM_ps_mPhi250_mChi1_2024.EE = 0

TTDM_ps_mPhi300_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=300)", "TTDM_ps_mPhi300_mChi1_2024")
TTDM_ps_mPhi300_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi300_mChi1_2024.year = 2024
TTDM_ps_mPhi300_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-300_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi300_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi300_mChi1_2024.unix_code = 24706
TTDM_ps_mPhi300_mChi1_2024.EE = 0

TTDM_ps_mPhi350_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=350)", "TTDM_ps_mPhi350_mChi1_2024")
TTDM_ps_mPhi350_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi350_mChi1_2024.year = 2024
TTDM_ps_mPhi350_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-350_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi350_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi350_mChi1_2024.unix_code = 24707
TTDM_ps_mPhi350_mChi1_2024.EE = 0

TTDM_ps_mPhi400_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=400)", "TTDM_ps_mPhi400_mChi1_2024")
TTDM_ps_mPhi400_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi400_mChi1_2024.year = 2024
TTDM_ps_mPhi400_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi400_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi400_mChi1_2024.unix_code = 24708
TTDM_ps_mPhi400_mChi1_2024.EE = 0

TTDM_ps_mPhi500_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=500)", "TTDM_ps_mPhi500_mChi1_2024")
TTDM_ps_mPhi500_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi500_mChi1_2024.year = 2024
TTDM_ps_mPhi500_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi500_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi500_mChi1_2024.unix_code = 24709
TTDM_ps_mPhi500_mChi1_2024.EE = 0

TTDM_ps_mPhi600_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=600)", "TTDM_ps_mPhi600_mChi1_2024")
TTDM_ps_mPhi600_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi600_mChi1_2024.year = 2024
TTDM_ps_mPhi600_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi600_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi600_mChi1_2024.unix_code = 24710
TTDM_ps_mPhi600_mChi1_2024.EE = 0

TTDM_ps_mPhi700_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=700)", "TTDM_ps_mPhi700_mChi1_2024")
TTDM_ps_mPhi700_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi700_mChi1_2024.year = 2024
TTDM_ps_mPhi700_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-700_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi700_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi700_mChi1_2024.unix_code = 24711
TTDM_ps_mPhi700_mChi1_2024.EE = 0

TTDM_ps_mPhi800_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=800)", "TTDM_ps_mPhi800_mChi1_2024")
TTDM_ps_mPhi800_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi800_mChi1_2024.year = 2024
TTDM_ps_mPhi800_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi800_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi800_mChi1_2024.unix_code = 24712
TTDM_ps_mPhi800_mChi1_2024.EE = 0

TTDM_ps_mPhi1000_mChi1_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar (m_{#Phi}=1000)", "TTDM_ps_mPhi1000_mChi1_2024")
TTDM_ps_mPhi1000_mChi1_2024.sigma = 1.0  # pb: placeholder
TTDM_ps_mPhi1000_mChi1_2024.year = 2024
TTDM_ps_mPhi1000_mChi1_2024.dataset = "/TTDMsimpSpin0-ps_Par-mchi-1-mphi-1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTDM_ps_mPhi1000_mChi1_2024.process = "TTDM_ps_2024"
TTDM_ps_mPhi1000_mChi1_2024.unix_code = 24713
TTDM_ps_mPhi1000_mChi1_2024.EE = 0

##################### TTto2LDM_s_2024

TTto2LDM_s_mPhi10_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=10)", "TTto2LDM_s_mPhi10_mChi1_2024")
TTto2LDM_s_mPhi10_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi10_mChi1_2024.year = 2024
TTto2LDM_s_mPhi10_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-10_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi10_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi10_mChi1_2024.unix_code = 24800
TTto2LDM_s_mPhi10_mChi1_2024.EE = 0

TTto2LDM_s_mPhi50_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=50)", "TTto2LDM_s_mPhi50_mChi1_2024")
TTto2LDM_s_mPhi50_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi50_mChi1_2024.year = 2024
TTto2LDM_s_mPhi50_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi50_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi50_mChi1_2024.unix_code = 24801
TTto2LDM_s_mPhi50_mChi1_2024.EE = 0

TTto2LDM_s_mPhi100_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=100)", "TTto2LDM_s_mPhi100_mChi1_2024")
TTto2LDM_s_mPhi100_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi100_mChi1_2024.year = 2024
TTto2LDM_s_mPhi100_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-100_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi100_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi100_mChi1_2024.unix_code = 24802
TTto2LDM_s_mPhi100_mChi1_2024.EE = 0

TTto2LDM_s_mPhi150_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=150)", "TTto2LDM_s_mPhi150_mChi1_2024")
TTto2LDM_s_mPhi150_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi150_mChi1_2024.year = 2024
TTto2LDM_s_mPhi150_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-150_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi150_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi150_mChi1_2024.unix_code = 24803
TTto2LDM_s_mPhi150_mChi1_2024.EE = 0

TTto2LDM_s_mPhi200_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=200)", "TTto2LDM_s_mPhi200_mChi1_2024")
TTto2LDM_s_mPhi200_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi200_mChi1_2024.year = 2024
TTto2LDM_s_mPhi200_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi200_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi200_mChi1_2024.unix_code = 24804
TTto2LDM_s_mPhi200_mChi1_2024.EE = 0

TTto2LDM_s_mPhi250_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=250)", "TTto2LDM_s_mPhi250_mChi1_2024")
TTto2LDM_s_mPhi250_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi250_mChi1_2024.year = 2024
TTto2LDM_s_mPhi250_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-250_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi250_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi250_mChi1_2024.unix_code = 24805
TTto2LDM_s_mPhi250_mChi1_2024.EE = 0

TTto2LDM_s_mPhi300_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=300)", "TTto2LDM_s_mPhi300_mChi1_2024")
TTto2LDM_s_mPhi300_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi300_mChi1_2024.year = 2024
TTto2LDM_s_mPhi300_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-300_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi300_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi300_mChi1_2024.unix_code = 24806
TTto2LDM_s_mPhi300_mChi1_2024.EE = 0

TTto2LDM_s_mPhi350_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=350)", "TTto2LDM_s_mPhi350_mChi1_2024")
TTto2LDM_s_mPhi350_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi350_mChi1_2024.year = 2024
TTto2LDM_s_mPhi350_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-350_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi350_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi350_mChi1_2024.unix_code = 24807
TTto2LDM_s_mPhi350_mChi1_2024.EE = 0

TTto2LDM_s_mPhi400_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=400)", "TTto2LDM_s_mPhi400_mChi1_2024")
TTto2LDM_s_mPhi400_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi400_mChi1_2024.year = 2024
TTto2LDM_s_mPhi400_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi400_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi400_mChi1_2024.unix_code = 24808
TTto2LDM_s_mPhi400_mChi1_2024.EE = 0

TTto2LDM_s_mPhi500_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=500)", "TTto2LDM_s_mPhi500_mChi1_2024")
TTto2LDM_s_mPhi500_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi500_mChi1_2024.year = 2024
TTto2LDM_s_mPhi500_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi500_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi500_mChi1_2024.unix_code = 24809
TTto2LDM_s_mPhi500_mChi1_2024.EE = 0

TTto2LDM_s_mPhi600_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=600)", "TTto2LDM_s_mPhi600_mChi1_2024")
TTto2LDM_s_mPhi600_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi600_mChi1_2024.year = 2024
TTto2LDM_s_mPhi600_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi600_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi600_mChi1_2024.unix_code = 24810
TTto2LDM_s_mPhi600_mChi1_2024.EE = 0

TTto2LDM_s_mPhi700_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=700)", "TTto2LDM_s_mPhi700_mChi1_2024")
TTto2LDM_s_mPhi700_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi700_mChi1_2024.year = 2024
TTto2LDM_s_mPhi700_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-700_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi700_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi700_mChi1_2024.unix_code = 24811
TTto2LDM_s_mPhi700_mChi1_2024.EE = 0

TTto2LDM_s_mPhi800_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=800)", "TTto2LDM_s_mPhi800_mChi1_2024")
TTto2LDM_s_mPhi800_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi800_mChi1_2024.year = 2024
TTto2LDM_s_mPhi800_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi800_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi800_mChi1_2024.unix_code = 24812
TTto2LDM_s_mPhi800_mChi1_2024.EE = 0

TTto2LDM_s_mPhi1000_mChi1_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar (m_{#Phi}=1000)", "TTto2LDM_s_mPhi1000_mChi1_2024")
TTto2LDM_s_mPhi1000_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_s_mPhi1000_mChi1_2024.year = 2024
TTto2LDM_s_mPhi1000_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-s_Par-mchi-1-mphi-1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_s_mPhi1000_mChi1_2024.process = "TTto2LDM_s_2024"
TTto2LDM_s_mPhi1000_mChi1_2024.unix_code = 24813
TTto2LDM_s_mPhi1000_mChi1_2024.EE = 0

##################### TTto2LDM_ps_2024

TTto2LDM_ps_mPhi10_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=10)", "TTto2LDM_ps_mPhi10_mChi1_2024")
TTto2LDM_ps_mPhi10_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi10_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi10_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-10_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi10_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi10_mChi1_2024.unix_code = 24900
TTto2LDM_ps_mPhi10_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi50_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=50)", "TTto2LDM_ps_mPhi50_mChi1_2024")
TTto2LDM_ps_mPhi50_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi50_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi50_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi50_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi50_mChi1_2024.unix_code = 24901
TTto2LDM_ps_mPhi50_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi100_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=100)", "TTto2LDM_ps_mPhi100_mChi1_2024")
TTto2LDM_ps_mPhi100_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi100_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi100_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-100_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi100_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi100_mChi1_2024.unix_code = 24902
TTto2LDM_ps_mPhi100_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi150_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=150)", "TTto2LDM_ps_mPhi150_mChi1_2024")
TTto2LDM_ps_mPhi150_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi150_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi150_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-150_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi150_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi150_mChi1_2024.unix_code = 24903
TTto2LDM_ps_mPhi150_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi200_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=200)", "TTto2LDM_ps_mPhi200_mChi1_2024")
TTto2LDM_ps_mPhi200_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi200_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi200_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi200_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi200_mChi1_2024.unix_code = 24904
TTto2LDM_ps_mPhi200_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi250_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=250)", "TTto2LDM_ps_mPhi250_mChi1_2024")
TTto2LDM_ps_mPhi250_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi250_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi250_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-250_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi250_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi250_mChi1_2024.unix_code = 24905
TTto2LDM_ps_mPhi250_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi300_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=300)", "TTto2LDM_ps_mPhi300_mChi1_2024")
TTto2LDM_ps_mPhi300_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi300_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi300_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-300_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi300_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi300_mChi1_2024.unix_code = 24906
TTto2LDM_ps_mPhi300_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi350_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=350)", "TTto2LDM_ps_mPhi350_mChi1_2024")
TTto2LDM_ps_mPhi350_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi350_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi350_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-350_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi350_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi350_mChi1_2024.unix_code = 24907
TTto2LDM_ps_mPhi350_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi400_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=400)", "TTto2LDM_ps_mPhi400_mChi1_2024")
TTto2LDM_ps_mPhi400_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi400_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi400_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi400_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi400_mChi1_2024.unix_code = 24908
TTto2LDM_ps_mPhi400_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi500_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=500)", "TTto2LDM_ps_mPhi500_mChi1_2024")
TTto2LDM_ps_mPhi500_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi500_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi500_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi500_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi500_mChi1_2024.unix_code = 24909
TTto2LDM_ps_mPhi500_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi600_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=600)", "TTto2LDM_ps_mPhi600_mChi1_2024")
TTto2LDM_ps_mPhi600_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi600_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi600_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi600_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi600_mChi1_2024.unix_code = 24910
TTto2LDM_ps_mPhi600_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi700_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=700)", "TTto2LDM_ps_mPhi700_mChi1_2024")
TTto2LDM_ps_mPhi700_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi700_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi700_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-700_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi700_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi700_mChi1_2024.unix_code = 24911
TTto2LDM_ps_mPhi700_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi800_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=800)", "TTto2LDM_ps_mPhi800_mChi1_2024")
TTto2LDM_ps_mPhi800_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi800_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi800_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi800_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi800_mChi1_2024.unix_code = 24912
TTto2LDM_ps_mPhi800_mChi1_2024.EE = 0

TTto2LDM_ps_mPhi1000_mChi1_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar (m_{#Phi}=1000)", "TTto2LDM_ps_mPhi1000_mChi1_2024")
TTto2LDM_ps_mPhi1000_mChi1_2024.sigma = 1.0  # pb: placeholder
TTto2LDM_ps_mPhi1000_mChi1_2024.year = 2024
TTto2LDM_ps_mPhi1000_mChi1_2024.dataset = "/TTto2LDMsimpSpin0-ps_Par-mchi-1-mphi-1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TTto2LDM_ps_mPhi1000_mChi1_2024.process = "TTto2LDM_ps_2024"
TTto2LDM_ps_mPhi1000_mChi1_2024.unix_code = 24913
TTto2LDM_ps_mPhi1000_mChi1_2024.EE = 0

##################### Aggregate samples and components

TTDM_s_2024 = sample(ROOT.kRed+1, 1, 1001, "t#bar{t}+DM scalar", "TTDM_s_2024")
TTDM_s_2024.year = 2024
TTDM_s_2024.components = [
    TTDM_s_mPhi10_mChi1_2024,
    TTDM_s_mPhi50_mChi1_2024,
    TTDM_s_mPhi100_mChi1_2024,
    TTDM_s_mPhi150_mChi1_2024,
    TTDM_s_mPhi200_mChi1_2024,
    TTDM_s_mPhi250_mChi1_2024,
    TTDM_s_mPhi300_mChi1_2024,
    TTDM_s_mPhi350_mChi1_2024,
    TTDM_s_mPhi400_mChi1_2024,
    TTDM_s_mPhi500_mChi1_2024,
    TTDM_s_mPhi600_mChi1_2024,
    TTDM_s_mPhi700_mChi1_2024,
    TTDM_s_mPhi800_mChi1_2024,
    TTDM_s_mPhi1000_mChi1_2024,
]

TTDM_ps_2024 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t}+DM pseudoscalar", "TTDM_ps_2024")
TTDM_ps_2024.year = 2024
TTDM_ps_2024.components = [
    TTDM_ps_mPhi10_mChi1_2024,
    TTDM_ps_mPhi50_mChi1_2024,
    TTDM_ps_mPhi100_mChi1_2024,
    TTDM_ps_mPhi150_mChi1_2024,
    TTDM_ps_mPhi200_mChi1_2024,
    TTDM_ps_mPhi250_mChi1_2024,
    TTDM_ps_mPhi300_mChi1_2024,
    TTDM_ps_mPhi350_mChi1_2024,
    TTDM_ps_mPhi400_mChi1_2024,
    TTDM_ps_mPhi500_mChi1_2024,
    TTDM_ps_mPhi600_mChi1_2024,
    TTDM_ps_mPhi700_mChi1_2024,
    TTDM_ps_mPhi800_mChi1_2024,
    TTDM_ps_mPhi1000_mChi1_2024,
]

TTto2LDM_s_2024 = sample(ROOT.kOrange+1, 1, 1001, "t#bar{t} to 2L+DM scalar", "TTto2LDM_s_2024")
TTto2LDM_s_2024.year = 2024
TTto2LDM_s_2024.components = [
    TTto2LDM_s_mPhi10_mChi1_2024,
    TTto2LDM_s_mPhi50_mChi1_2024,
    TTto2LDM_s_mPhi100_mChi1_2024,
    TTto2LDM_s_mPhi150_mChi1_2024,
    TTto2LDM_s_mPhi200_mChi1_2024,
    TTto2LDM_s_mPhi250_mChi1_2024,
    TTto2LDM_s_mPhi300_mChi1_2024,
    TTto2LDM_s_mPhi350_mChi1_2024,
    TTto2LDM_s_mPhi400_mChi1_2024,
    TTto2LDM_s_mPhi500_mChi1_2024,
    TTto2LDM_s_mPhi600_mChi1_2024,
    TTto2LDM_s_mPhi700_mChi1_2024,
    TTto2LDM_s_mPhi800_mChi1_2024,
    TTto2LDM_s_mPhi1000_mChi1_2024,
]

TTto2LDM_ps_2024 = sample(ROOT.kOrange+2, 1, 1001, "t#bar{t} to 2L+DM pseudoscalar", "TTto2LDM_ps_2024")
TTto2LDM_ps_2024.year = 2024
TTto2LDM_ps_2024.components = [
    TTto2LDM_ps_mPhi10_mChi1_2024,
    TTto2LDM_ps_mPhi50_mChi1_2024,
    TTto2LDM_ps_mPhi100_mChi1_2024,
    TTto2LDM_ps_mPhi150_mChi1_2024,
    TTto2LDM_ps_mPhi200_mChi1_2024,
    TTto2LDM_ps_mPhi250_mChi1_2024,
    TTto2LDM_ps_mPhi300_mChi1_2024,
    TTto2LDM_ps_mPhi350_mChi1_2024,
    TTto2LDM_ps_mPhi400_mChi1_2024,
    TTto2LDM_ps_mPhi500_mChi1_2024,
    TTto2LDM_ps_mPhi600_mChi1_2024,
    TTto2LDM_ps_mPhi700_mChi1_2024,
    TTto2LDM_ps_mPhi800_mChi1_2024,
    TTto2LDM_ps_mPhi1000_mChi1_2024,
]


samples_dict_tdm_signals={
    

    ##################### Dark Matter samples 2024

    # Gruppi con components
    "TBDM_s_2024": TBDM_s_2024,
    "TBDM_ps_2024": TBDM_ps_2024,
    "TWDM_s_2024": TWDM_s_2024,
    "TWDM_ps_2024": TWDM_ps_2024,
    "TWto2LDM_s_2024": TWto2LDM_s_2024,
    "TWto2LDM_ps_2024": TWto2LDM_ps_2024,

    # TBDM scalar
    "TBDM_s_mPhi10_mChi1_2024": TBDM_s_mPhi10_mChi1_2024,
    "TBDM_s_mPhi50_mChi1_2024": TBDM_s_mPhi50_mChi1_2024,
    "TBDM_s_mPhi100_mChi1_2024": TBDM_s_mPhi100_mChi1_2024,
    "TBDM_s_mPhi150_mChi1_2024": TBDM_s_mPhi150_mChi1_2024,
    "TBDM_s_mPhi200_mChi1_2024": TBDM_s_mPhi200_mChi1_2024,
    "TBDM_s_mPhi250_mChi1_2024": TBDM_s_mPhi250_mChi1_2024,
    "TBDM_s_mPhi300_mChi1_2024": TBDM_s_mPhi300_mChi1_2024,
    "TBDM_s_mPhi350_mChi1_2024": TBDM_s_mPhi350_mChi1_2024,
    "TBDM_s_mPhi400_mChi1_2024": TBDM_s_mPhi400_mChi1_2024,
    "TBDM_s_mPhi500_mChi1_2024": TBDM_s_mPhi500_mChi1_2024,
    "TBDM_s_mPhi600_mChi1_2024": TBDM_s_mPhi600_mChi1_2024,
    "TBDM_s_mPhi700_mChi1_2024": TBDM_s_mPhi700_mChi1_2024,
    "TBDM_s_mPhi800_mChi1_2024": TBDM_s_mPhi800_mChi1_2024,
    "TBDM_s_mPhi1000_mChi1_2024": TBDM_s_mPhi1000_mChi1_2024,

    # TBDM pseudoscalar
    "TBDM_ps_mPhi10_mChi1_2024": TBDM_ps_mPhi10_mChi1_2024,
    "TBDM_ps_mPhi50_mChi1_2024": TBDM_ps_mPhi50_mChi1_2024,
    "TBDM_ps_mPhi100_mChi1_2024": TBDM_ps_mPhi100_mChi1_2024,
    "TBDM_ps_mPhi150_mChi1_2024": TBDM_ps_mPhi150_mChi1_2024,
    "TBDM_ps_mPhi200_mChi1_2024": TBDM_ps_mPhi200_mChi1_2024,
    "TBDM_ps_mPhi250_mChi1_2024": TBDM_ps_mPhi250_mChi1_2024,
    "TBDM_ps_mPhi300_mChi1_2024": TBDM_ps_mPhi300_mChi1_2024,
    "TBDM_ps_mPhi350_mChi1_2024": TBDM_ps_mPhi350_mChi1_2024,
    "TBDM_ps_mPhi400_mChi1_2024": TBDM_ps_mPhi400_mChi1_2024,
    "TBDM_ps_mPhi500_mChi1_2024": TBDM_ps_mPhi500_mChi1_2024,
    "TBDM_ps_mPhi600_mChi1_2024": TBDM_ps_mPhi600_mChi1_2024,
    "TBDM_ps_mPhi700_mChi1_2024": TBDM_ps_mPhi700_mChi1_2024,
    "TBDM_ps_mPhi800_mChi1_2024": TBDM_ps_mPhi800_mChi1_2024,
    "TBDM_ps_mPhi1000_mChi1_2024": TBDM_ps_mPhi1000_mChi1_2024,

    # TWDM scalar
    "TWDM_s_mPhi10_mChi1_2024": TWDM_s_mPhi10_mChi1_2024,
    "TWDM_s_mPhi50_mChi1_2024": TWDM_s_mPhi50_mChi1_2024,
    "TWDM_s_mPhi100_mChi1_2024": TWDM_s_mPhi100_mChi1_2024,
    "TWDM_s_mPhi150_mChi1_2024": TWDM_s_mPhi150_mChi1_2024,
    "TWDM_s_mPhi200_mChi1_2024": TWDM_s_mPhi200_mChi1_2024,
    "TWDM_s_mPhi250_mChi1_2024": TWDM_s_mPhi250_mChi1_2024,
    "TWDM_s_mPhi300_mChi1_2024": TWDM_s_mPhi300_mChi1_2024,
    "TWDM_s_mPhi350_mChi1_2024": TWDM_s_mPhi350_mChi1_2024,
    "TWDM_s_mPhi400_mChi1_2024": TWDM_s_mPhi400_mChi1_2024,
    "TWDM_s_mPhi500_mChi1_2024": TWDM_s_mPhi500_mChi1_2024,
    "TWDM_s_mPhi600_mChi1_2024": TWDM_s_mPhi600_mChi1_2024,
    "TWDM_s_mPhi700_mChi1_2024": TWDM_s_mPhi700_mChi1_2024,
    "TWDM_s_mPhi800_mChi1_2024": TWDM_s_mPhi800_mChi1_2024,
    "TWDM_s_mPhi1000_mChi1_2024": TWDM_s_mPhi1000_mChi1_2024,

    # TWDM pseudoscalar
    "TWDM_ps_mPhi10_mChi1_2024": TWDM_ps_mPhi10_mChi1_2024,
    "TWDM_ps_mPhi50_mChi1_2024": TWDM_ps_mPhi50_mChi1_2024,
    "TWDM_ps_mPhi100_mChi1_2024": TWDM_ps_mPhi100_mChi1_2024,
    "TWDM_ps_mPhi150_mChi1_2024": TWDM_ps_mPhi150_mChi1_2024,
    "TWDM_ps_mPhi200_mChi1_2024": TWDM_ps_mPhi200_mChi1_2024,
    "TWDM_ps_mPhi250_mChi1_2024": TWDM_ps_mPhi250_mChi1_2024,
    "TWDM_ps_mPhi300_mChi1_2024": TWDM_ps_mPhi300_mChi1_2024,
    "TWDM_ps_mPhi350_mChi1_2024": TWDM_ps_mPhi350_mChi1_2024,
    "TWDM_ps_mPhi400_mChi1_2024": TWDM_ps_mPhi400_mChi1_2024,
    "TWDM_ps_mPhi500_mChi1_2024": TWDM_ps_mPhi500_mChi1_2024,
    "TWDM_ps_mPhi600_mChi1_2024": TWDM_ps_mPhi600_mChi1_2024,
    "TWDM_ps_mPhi700_mChi1_2024": TWDM_ps_mPhi700_mChi1_2024,
    "TWDM_ps_mPhi800_mChi1_2024": TWDM_ps_mPhi800_mChi1_2024,
    "TWDM_ps_mPhi1000_mChi1_2024": TWDM_ps_mPhi1000_mChi1_2024,

    # TW to 2L DM scalar
    "TWto2LDM_s_mPhi10_mChi1_2024": TWto2LDM_s_mPhi10_mChi1_2024,
    "TWto2LDM_s_mPhi50_mChi1_2024": TWto2LDM_s_mPhi50_mChi1_2024,
    "TWto2LDM_s_mPhi100_mChi1_2024": TWto2LDM_s_mPhi100_mChi1_2024,
    "TWto2LDM_s_mPhi150_mChi1_2024": TWto2LDM_s_mPhi150_mChi1_2024,
    "TWto2LDM_s_mPhi200_mChi1_2024": TWto2LDM_s_mPhi200_mChi1_2024,
    "TWto2LDM_s_mPhi250_mChi1_2024": TWto2LDM_s_mPhi250_mChi1_2024,
    "TWto2LDM_s_mPhi300_mChi1_2024": TWto2LDM_s_mPhi300_mChi1_2024,
    "TWto2LDM_s_mPhi350_mChi1_2024": TWto2LDM_s_mPhi350_mChi1_2024,
    "TWto2LDM_s_mPhi400_mChi1_2024": TWto2LDM_s_mPhi400_mChi1_2024,
    "TWto2LDM_s_mPhi500_mChi1_2024": TWto2LDM_s_mPhi500_mChi1_2024,
    "TWto2LDM_s_mPhi600_mChi1_2024": TWto2LDM_s_mPhi600_mChi1_2024,
    "TWto2LDM_s_mPhi700_mChi1_2024": TWto2LDM_s_mPhi700_mChi1_2024,
    "TWto2LDM_s_mPhi800_mChi1_2024": TWto2LDM_s_mPhi800_mChi1_2024,
    "TWto2LDM_s_mPhi1000_mChi1_2024": TWto2LDM_s_mPhi1000_mChi1_2024,

    # TW to 2L DM pseudoscalar
    "TWto2LDM_ps_mPhi10_mChi1_2024": TWto2LDM_ps_mPhi10_mChi1_2024,
    "TWto2LDM_ps_mPhi50_mChi1_2024": TWto2LDM_ps_mPhi50_mChi1_2024,
    "TWto2LDM_ps_mPhi100_mChi1_2024": TWto2LDM_ps_mPhi100_mChi1_2024,
    "TWto2LDM_ps_mPhi150_mChi1_2024": TWto2LDM_ps_mPhi150_mChi1_2024,
    "TWto2LDM_ps_mPhi200_mChi1_2024": TWto2LDM_ps_mPhi200_mChi1_2024,
    "TWto2LDM_ps_mPhi250_mChi1_2024": TWto2LDM_ps_mPhi250_mChi1_2024,
    "TWto2LDM_ps_mPhi300_mChi1_2024": TWto2LDM_ps_mPhi300_mChi1_2024,
    "TWto2LDM_ps_mPhi350_mChi1_2024": TWto2LDM_ps_mPhi350_mChi1_2024,
    "TWto2LDM_ps_mPhi400_mChi1_2024": TWto2LDM_ps_mPhi400_mChi1_2024,
    "TWto2LDM_ps_mPhi500_mChi1_2024": TWto2LDM_ps_mPhi500_mChi1_2024,
    "TWto2LDM_ps_mPhi600_mChi1_2024": TWto2LDM_ps_mPhi600_mChi1_2024,
    "TWto2LDM_ps_mPhi700_mChi1_2024": TWto2LDM_ps_mPhi700_mChi1_2024,
    "TWto2LDM_ps_mPhi800_mChi1_2024": TWto2LDM_ps_mPhi800_mChi1_2024,
    "TWto2LDM_ps_mPhi1000_mChi1_2024": TWto2LDM_ps_mPhi1000_mChi1_2024,

    #double top

    "TTDM_s_2024": TTDM_s_2024,
    "TTDM_s_mPhi10_mChi1_2024": TTDM_s_mPhi10_mChi1_2024,
    "TTDM_s_mPhi50_mChi1_2024": TTDM_s_mPhi50_mChi1_2024,
    "TTDM_s_mPhi100_mChi1_2024": TTDM_s_mPhi100_mChi1_2024,
    "TTDM_s_mPhi150_mChi1_2024": TTDM_s_mPhi150_mChi1_2024,
    "TTDM_s_mPhi200_mChi1_2024": TTDM_s_mPhi200_mChi1_2024,
    "TTDM_s_mPhi250_mChi1_2024": TTDM_s_mPhi250_mChi1_2024,
    "TTDM_s_mPhi300_mChi1_2024": TTDM_s_mPhi300_mChi1_2024,
    "TTDM_s_mPhi350_mChi1_2024": TTDM_s_mPhi350_mChi1_2024,
    "TTDM_s_mPhi400_mChi1_2024": TTDM_s_mPhi400_mChi1_2024,
    "TTDM_s_mPhi500_mChi1_2024": TTDM_s_mPhi500_mChi1_2024,
    "TTDM_s_mPhi600_mChi1_2024": TTDM_s_mPhi600_mChi1_2024,
    "TTDM_s_mPhi700_mChi1_2024": TTDM_s_mPhi700_mChi1_2024,
    "TTDM_s_mPhi800_mChi1_2024": TTDM_s_mPhi800_mChi1_2024,
    "TTDM_s_mPhi1000_mChi1_2024": TTDM_s_mPhi1000_mChi1_2024,
    "TTDM_ps_2024": TTDM_ps_2024,
    "TTDM_ps_mPhi10_mChi1_2024": TTDM_ps_mPhi10_mChi1_2024,
    "TTDM_ps_mPhi50_mChi1_2024": TTDM_ps_mPhi50_mChi1_2024,
    "TTDM_ps_mPhi100_mChi1_2024": TTDM_ps_mPhi100_mChi1_2024,
    "TTDM_ps_mPhi150_mChi1_2024": TTDM_ps_mPhi150_mChi1_2024,
    "TTDM_ps_mPhi200_mChi1_2024": TTDM_ps_mPhi200_mChi1_2024,
    "TTDM_ps_mPhi250_mChi1_2024": TTDM_ps_mPhi250_mChi1_2024,
    "TTDM_ps_mPhi300_mChi1_2024": TTDM_ps_mPhi300_mChi1_2024,
    "TTDM_ps_mPhi350_mChi1_2024": TTDM_ps_mPhi350_mChi1_2024,
    "TTDM_ps_mPhi400_mChi1_2024": TTDM_ps_mPhi400_mChi1_2024,
    "TTDM_ps_mPhi500_mChi1_2024": TTDM_ps_mPhi500_mChi1_2024,
    "TTDM_ps_mPhi600_mChi1_2024": TTDM_ps_mPhi600_mChi1_2024,
    "TTDM_ps_mPhi700_mChi1_2024": TTDM_ps_mPhi700_mChi1_2024,
    "TTDM_ps_mPhi800_mChi1_2024": TTDM_ps_mPhi800_mChi1_2024,
    "TTDM_ps_mPhi1000_mChi1_2024": TTDM_ps_mPhi1000_mChi1_2024,
    "TTto2LDM_s_2024": TTto2LDM_s_2024,
    "TTto2LDM_s_mPhi10_mChi1_2024": TTto2LDM_s_mPhi10_mChi1_2024,
    "TTto2LDM_s_mPhi50_mChi1_2024": TTto2LDM_s_mPhi50_mChi1_2024,
    "TTto2LDM_s_mPhi100_mChi1_2024": TTto2LDM_s_mPhi100_mChi1_2024,
    "TTto2LDM_s_mPhi150_mChi1_2024": TTto2LDM_s_mPhi150_mChi1_2024,
    "TTto2LDM_s_mPhi200_mChi1_2024": TTto2LDM_s_mPhi200_mChi1_2024,
    "TTto2LDM_s_mPhi250_mChi1_2024": TTto2LDM_s_mPhi250_mChi1_2024,
    "TTto2LDM_s_mPhi300_mChi1_2024": TTto2LDM_s_mPhi300_mChi1_2024,
    "TTto2LDM_s_mPhi350_mChi1_2024": TTto2LDM_s_mPhi350_mChi1_2024,
    "TTto2LDM_s_mPhi400_mChi1_2024": TTto2LDM_s_mPhi400_mChi1_2024,
    "TTto2LDM_s_mPhi500_mChi1_2024": TTto2LDM_s_mPhi500_mChi1_2024,
    "TTto2LDM_s_mPhi600_mChi1_2024": TTto2LDM_s_mPhi600_mChi1_2024,
    "TTto2LDM_s_mPhi700_mChi1_2024": TTto2LDM_s_mPhi700_mChi1_2024,
    "TTto2LDM_s_mPhi800_mChi1_2024": TTto2LDM_s_mPhi800_mChi1_2024,
    "TTto2LDM_s_mPhi1000_mChi1_2024": TTto2LDM_s_mPhi1000_mChi1_2024,
    "TTto2LDM_ps_2024": TTto2LDM_ps_2024,
    "TTto2LDM_ps_mPhi10_mChi1_2024": TTto2LDM_ps_mPhi10_mChi1_2024,
    "TTto2LDM_ps_mPhi50_mChi1_2024": TTto2LDM_ps_mPhi50_mChi1_2024,
    "TTto2LDM_ps_mPhi100_mChi1_2024": TTto2LDM_ps_mPhi100_mChi1_2024,
    "TTto2LDM_ps_mPhi150_mChi1_2024": TTto2LDM_ps_mPhi150_mChi1_2024,
    "TTto2LDM_ps_mPhi200_mChi1_2024": TTto2LDM_ps_mPhi200_mChi1_2024,
    "TTto2LDM_ps_mPhi250_mChi1_2024": TTto2LDM_ps_mPhi250_mChi1_2024,
    "TTto2LDM_ps_mPhi300_mChi1_2024": TTto2LDM_ps_mPhi300_mChi1_2024,
    "TTto2LDM_ps_mPhi350_mChi1_2024": TTto2LDM_ps_mPhi350_mChi1_2024,
    "TTto2LDM_ps_mPhi400_mChi1_2024": TTto2LDM_ps_mPhi400_mChi1_2024,
    "TTto2LDM_ps_mPhi500_mChi1_2024": TTto2LDM_ps_mPhi500_mChi1_2024,
    "TTto2LDM_ps_mPhi600_mChi1_2024": TTto2LDM_ps_mPhi600_mChi1_2024,
    "TTto2LDM_ps_mPhi700_mChi1_2024": TTto2LDM_ps_mPhi700_mChi1_2024,
    "TTto2LDM_ps_mPhi800_mChi1_2024": TTto2LDM_ps_mPhi800_mChi1_2024,
    "TTto2LDM_ps_mPhi1000_mChi1_2024": TTto2LDM_ps_mPhi1000_mChi1_2024,
}
