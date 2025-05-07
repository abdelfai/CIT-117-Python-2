import pickle

# dictionary with the gravity for each planet
PLANET_GRAVITY =  {
    'Mercury': 0.38, 'Venus': 0.91, 'Moon': 0.165, 'Mars': 0.38, 'Jupiter': 2.34,
    'Saturn': 0.93, 'Uranus': 0.92, 'Neptune': 1.12, 'Pluto': 0.066
}
# storing the history data
DB_FILE = "afPlanetaryWeights.db"
#load history data from pickle
def LOAD_HISTORY():
    try:
        with open(DB_FILE, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}
#saving the history
def SAVE_HISTORY(dictPlanetHistory): 
    with open(DB_FILE, "wb") as file:
        pickle.dump(dictPlanetHistory, file)
#calculating the weight on each planet
def CALCULATE_WEIGHTS(fEarthWeight):
    return {planet: fEarthWeight * factor for planet, factor in PLANET_GRAVITY.items()}
#displaying weight
def DISPLAY_WEIGHTS(sName, dictWeights):
    print(f"\n{sName}, here are your weights on our Solar System's planets.")
    for planet, weight in dictWeights.items():
        print(f"Weight on {planet:<10}: {weight:10.2f}")
    print()
#asking if they want to see history
def main():
    dictPlanetHistory = LOAD_HISTORY()
    
    sViewHistory = input("Would you like to see the history (y/n): ").lower()
    if sViewHistory == 'y':
        for sName, weights in dictPlanetHistory.items():
            DISPLAY_WEIGHTS(sName, weights)
    #getting unique name
    while True:
        while True:
            sName = input("What is your name (enter key to quit): ")
            if not sName:
                SAVE_HISTORY(dictPlanetHistory)
                return
            sName = sName.title()
            if sName not in dictPlanetHistory:
                break
            print(f"{sName} is already in the history file. Enter a unique name.")

        # getting the right earth weight
        while True:
            try:
                fEarthWeight = float(input("What is your weight: "))
                break
            except ValueError:
                print("Please enter a numeric weight.")
        
        
        dictPersonWeights = CALCULATE_WEIGHTS(fEarthWeight)
        dictPlanetHistory[sName] = dictPersonWeights
        
        # output
        DISPLAY_WEIGHTS(sName, dictPersonWeights)

if __name__ == "__main__":
    main()
#favorite assignment so far
