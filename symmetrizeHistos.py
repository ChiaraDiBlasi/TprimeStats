import ROOT
import argparse
from loadHists import loadHists

parser  = argparse.ArgumentParser(description='Process ROOT files to symmetrize the up/down variations of some systematics.')
parser.add_argument("-i", "--infile", type=str, help='Input ROOT file', required=True)
parser.add_argument("-s", "--systs",  type=str, help='Comma separated systematics to symmetrize, e.g. jesTotal,jer', required=True)
args    = parser.parse_args()

infilename      = args.infile
outfilename     = infilename.replace(".root","_symmetrized.root")
systs           = args.systs.split(",")
histo_dict      = loadHists(infilename)
outfile         = ROOT.TFile.Open(outfilename, "RECREATE")
thrOutput       = 0.000001 # negative symmetrized contents are set to this (same value as makePositiveHistos.py)

# up/down variations to symmetrize, taken from the nominal histograms: <base>_nominal, <base>_<syst>Up, <base>_<syst>Down
symmetrized_dict = {}
for histo_name in histo_dict:
    if not histo_name.endswith("_nominal"):
        continue
    base = histo_name[:-len("_nominal")]
    for syst in systs:
        histo_name_up   = f"{base}_{syst}Up"
        histo_name_down = f"{base}_{syst}Down"
        if (histo_name_up not in histo_dict) or (histo_name_down not in histo_dict):
            print(f"Histograms {histo_name_up} or {histo_name_down} not found, skipping")
            continue

        hnom    = histo_dict[histo_name]
        hup     = histo_dict[histo_name_up].Clone(histo_name_up)
        hdown   = histo_dict[histo_name_down].Clone(histo_name_down)
        for b in range(1, hnom.GetNbinsX()+1):
            bnom        = hnom.GetBinContent(b)
            bup         = hup.GetBinContent(b)
            bdown       = hdown.GetBinContent(b)
            delta       = (abs(bup-bnom) + abs(bdown-bnom))/2.0 # up always above the nominal, down always below
            bupnew      = bnom + delta
            bdownnew    = bnom - delta
            if bupnew < 0:
                bupnew = thrOutput
            if bdownnew < 0:
                bdownnew = thrOutput
            print(f"Histogram {base} {syst}, bin {b}: nom {bnom}, up {bup}, down {bdown} --> up {bupnew}, down {bdownnew}")
            hup.SetBinContent(b, bupnew)
            hdown.SetBinContent(b, bdownnew)
        symmetrized_dict[histo_name_up]     = hup
        symmetrized_dict[histo_name_down]   = hdown

outfile.cd()
for histo_name,histo in histo_dict.items():
    tmp = symmetrized_dict.get(histo_name, histo) # histograms not symmetrized are kept as they are
    tmp.Write(histo_name, ROOT.TObject.kOverwrite)

outfile.Close()
print(f"Histograms with symmetrized {systs} saved to {outfilename}")
