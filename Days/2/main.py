with open("input.txt", "r") as f:
    data = f.read().split("\n")


# data = [
# "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
# "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
# "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
# "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
# "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
# ]


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