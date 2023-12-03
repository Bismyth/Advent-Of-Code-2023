import os, sys
sys.path.append(os.path.abspath('../..'))
from library import readInput

data = readInput("input.txt")

maxReds = 12
maxGreens = 13
maxBlues = 14

output = 0

for line in data:
    game, gameData = line.split(": ")
    _, gameId = game.split(" ")
    gameId = int(gameId)
    rounds = gameData.split("; ")

    gamePossible = True

    maxFoundReds = 1
    maxFoundGreens = 1
    maxFoundBlues = 1

    for roun in rounds:
        dictValues = {}
        values = roun.split(', ')
        for v in values:
            n, c = v.split(" ")
            dictValues[c] = int(n)
        
        if dictValues.get("red", 0) > maxFoundReds:
            maxFoundReds = dictValues.get("red", 0)
        if dictValues.get("green", 0) > maxFoundGreens:
            maxFoundGreens = dictValues.get("green", 0)
        if dictValues.get("blue", 0) > maxFoundBlues:
            maxFoundBlues = dictValues.get("blue", 0)
    output += maxFoundReds * maxFoundGreens * maxFoundBlues

print(output)