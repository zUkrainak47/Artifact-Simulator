# Genshin Impact Simulator
Welcome to the ultimate (command-line interface) Genshin Impact simulator. \
With this project, I did my best to replicate Genshin Impact's two major gacha systems: the Wishing System and the Artifact System.

## How do I start simulating Genshin Impact?

First you need to download or clone the repository on your device (i know) \
Next, locate `simulator.py`. You can access both simulators from there! \
Alternatively, you can run `wish_simulator.py` or `artifact_simulator.py` to access the respective simulator directly.


---
## Artifact Simulator
### About
Ever wanted to know how long it *actually* takes to get a 50CV artifact? \
Are you out of resin but crave that lovely RNG?

This Artifact Simulator can help you with that.
## Using `Artifact Simulator`

### Mode 1:
- Allows you to generate and upgrade artifacts one by one. Basically like running domains or using the strongbox, but you have unlimited resin.
- If there's an artifact that you like, you can add it to your inventory. It also carries over sessions.
- Commands include:
  - leveling artifact (to next tier or to +20)
  - re-rolling artifact
  - viewing inventory
  - etc.

### Mode 2: 
- Will continuously generate artifacts until your desired Crit Value is reached.
- Will tell you how many days (or years) of continuous farming that took.
- You can choose to run multiple tests, the program will show the average time.
- It will use 1 Transient Resin per week, assumes unlimited fodder and throws all artifacts in the Strongbox.
- It also assumes a 33.3% (1/3) chance to get a 4-liner from strongbox and 20% from domains, as well as a 6.66% (2/30) chance to get double artifact drops from a domain run. 

## Plotting with `simulator_for_plotting.py`

This program will run Mode 2 of `simulator.py`, but will create a graph to visualize the results. \
Right now only CV is supported as a stat, but I might add more in the future.

---

## Wish Simulator
### About
You're out of primogems? You watched a friend whale? You just lost your 50/50? \
I've got you covered! Hop on and spend any amount of pulls on any banner that's ever existed (yes, even the Keqing banner)
## Using `Wish Simulator`
As stated above, this part of the project is still WIP, however I'm actively working on it. \
By using Wish Simulator, you may
- Do virtually any amount of pulls on ~~any banner~~ a currently hardcoded character banner
- Check your wish history!
- Check your inventory containing every character's constellations and weapon refinements
- Make a "5-stars VS Pity" graph based on your results
