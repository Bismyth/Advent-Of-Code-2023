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


path = data[0]

directions = {}

print(path)

for line in data[2:]:
    node, points = line.split(" = ")
    points = points[1:-1].split(", ")
    directions[node] = tuple(points)

currentNode = "AAA"
traverse = 0
while currentNode != "ZZZ":
    direction = 0 if path[traverse % len(path)] == "L" else 1
    currentNode = directions[currentNode][direction]
    traverse += 1

print(traverse)