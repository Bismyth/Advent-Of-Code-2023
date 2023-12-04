import os, sys
sys.path.append(os.path.abspath('../..'))
from library import readInput

fileName = None
useSample = False

if useSample:
    fileName = "sample.txt"
else:
    fileName = "input.txt"

data = readInput(fileName)

output = 0

def parseNumberInput(s):
    numberConversion = [int(x) for x in s.split(" ") if x != ""]
    numberConversion.sort()
    return numberConversion

cardTotals = [1] * len(data)
maxCards = len(data)

for i, line in enumerate(data):
    test, numbers = line.split(": ")
    winning, rest = numbers.split(" | ")
    winningNumbers = set(parseNumberInput(winning))
    restNumbers = parseNumberInput(rest)
    
    matches = sum([1 for x in restNumbers if x in winningNumbers])
    
    for x in range(i+1, min(i+1+matches, maxCards)):
        cardTotals[x] += cardTotals[i]

print(sum(cardTotals))
