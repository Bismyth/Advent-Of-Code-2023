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
    return numberConversion

for line in data:
    test, numbers = line.split(": ")
    winning, rest = numbers.split(" | ")
    winningNumbers = set(parseNumberInput(winning))
    restNumbers = parseNumberInput(rest)
    
    matches = sum([1 for x in restNumbers if x in winningNumbers])
    score = (1 << matches - 1) if matches else 0
    output += score
    


print(output)