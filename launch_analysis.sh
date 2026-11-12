####################################################################################################
#How to use perform-statistical-analysis:
# ### ==> Main features: 
# You can launch all steps of the analysis from this file.
# it takes the input from a settings.json that you need to prepare and give with the -j mySettings.json command
# There are several working options that you can select with the -m (or --mode) option, and you can select multiple.  
# The main working options are:
# -m c --> collects histograms from the repository 
# -m s --> symmetrizes the jesTotal and jer up/down variations around the nominal. This adds "symmetrized" to the suffix.
# -m m --> modifies the histograms to fix the zeros and the systematics. Note that this also changes the name of the output to reflect that, by adding "fixZeros" to the suffix.
# -m d --> creates the datacards for the fit according to your settings.json
# -m l --> evaluates the limits
# -m p --> does the brazil plot
# There are also 3 possible options for performing statistical tests:
# -m g --> perform goodness of fit tests
# -m i --> make impact plots
# -m b --> make bias tests
# Without specifying anything, this will run the full chain (cmdlpbig)
### ==> Output:
# This will create, besides the obvious output of the commands:
# - A remote folder in your settings that will contain the datacards for each signal process.
# - Limits_era_suffix.json file with the limits result, in the dc-folder.
# - A shell configuration file (.sh) file with all the executed commands, in the dc-folder.
### ==> Other options:
# --variant(-v): you can start from a given histo<suffix>.root and produce the next steps from the datacard onwards without re-generating the histo file
# --dryrun: runs only the commands without executing them. The .sh file will be produced.
# --verbose: sets verbosity level (0: minimum, >1 maximum)
### ==> Examples of operations:
# You can make a single string to run multiple options to gether, for example:
# 1) python3 perform-statistical-analysis.py -m cdlpm -i mysettings.json --e 2024
#    => This will collect histograms, modify them, make the datacards, the limit, and the brazil plot 
# 2) python3 perform-statistical-analysis.py -m dlp -i mysettings.json --e 2024
#    => This will not re-collect the histograms and NOT modify them, but make the fit to the original plots.
# Note this will work only if you previously collected the histograms, e.g. if you ran the command in 1)
####################################################################################################
#python3 perform-statistical-analysis.py -j settingsOrsoNominalFit_reduced.json -e 2024 -s test -m cmdlp 
#python3 perform-statistical-analysis.py -j settingsOrsoNominalFit.json -e 2024 -s TOPXT_loose_lepVeto_zerosFixed -m i
#python3 perform-statistical-analysis.py -j settingsOrsoNominalFit.json -e 2024 --folder TOPXT_tight_lepVeto -s TOPXT_tight_lepVeto_zerosFixed -m i
#python3 perform-statistical-analysis.py -j settingsOrsoNominalFit.json -e 2024 --folder TOPtightNotXT_loose_lepVeto -s TOPtightNotXT_loose_lepVeto_zerosFixed -m dlp
#python3 perform-statistical-analysis.py -j settingsOrsoNominalFit.json -e 2024 --folder TOPlooseNotTight_loose_lepVeto -s TOPlooseNotTight_loose_lepVeto_zerosFixed -m i
#python3 perform-statistical-analysis.py -j settingsOrsoNominalFit.json -e 2024 --folder TOPlooseNotTight_tight_lepVeto -s TOPlooseNotTight_tight_lepVeto_zerosFixed -m dlp

#python3 perform-statistical-analysis.py -j settingsOrsoNominalFit.json -e 2024 --folder TOPXT_TNotXT_LNotT_tight_lepVeto -s TOPXT_TNotXT_LNotT_tight_lepVeto_zerosFixed -m dlp
#python3 perform-statistical-analysis.py -j settingsOrsoNominalFit.json -e 2024 --folder TOPXT_TNotXT_tight_lepVeto -s TOPXT_TNotXT_tight_lepVet_zerosfixed -m dlp
python3 perform-statistical-analysis.py -j settingsOrsoNominalFit.json -e 2024 --folder TOPT_LNotT_tight_lepVeto_old -s TOPT_LNotT_tight_lepVeto_old_zerosFixed_zerosFixed -m dlp