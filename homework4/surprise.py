# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def printstars(targets):
    for key in targets:
        print(key)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def printspectral(targets):
    for key in targets:
        print(targets[key]["Spectral Type"])
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def findstarbig(targets):
    bigstars = []
    for key in targets:
        if targets[key]["Magnitude"]>0.1 or targets[key]["Magnitude"]<-0.1:
            bigstars.append(key)
    return bigstars
# 4) Look up another target, add all the necessary information to the targets list. 
targets["Andromeda_Galaxy"]={
    "RA": "00h 42m 44.3s",
    "Dec": "+41° 16′ 09″",
    "Magnitude": 3.44,
    "Spectral Type": "SA(s)b"
}
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def brighteststar(targets):
    brighteststar = list(targets.keys())[0]
    for key in targets:
        current_dec = int(targets[key]["Dec"][1:3]) - 20
        best_dec = int(targets[brighteststar]["Dec"][1:3]) - 20
        if current_dec < best_dec:
            brighteststar=key
    return brighteststar
# 6) What is your favorite constellation?
# Ursa Major
print(printstars(targets),printspectral(targets),findstarbig(targets),brighteststar(targets))