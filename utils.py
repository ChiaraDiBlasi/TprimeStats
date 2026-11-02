def unpackLabel(l,verbose=0):#function to extract the model from the label
    mass = ""
    model = ""

    if "TBDM" in l or "TTDM"in l or "TWDM" in l:
        mass=0.001*int((l.split("mPhi")[1]).split("_mChi")[0])
        model=(l.split("_mPhi")[0])
    if "Tprime" in l:
        mass=0.001*int((l.split("TprimeToTZ_")[1]))
        model=("TprimeToTZNW")
    if(verbose>0):print(f"label: {l}, mass: {mass}, model: {model}" )    
    return mass,model
