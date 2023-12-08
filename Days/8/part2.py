import os, sys
sys.path.append(os.path.abspath('../..'))
from library import readInput
import functools

fileName = None
useSample = True

if useSample:
    fileName = "sample2.txt"
else:
    fileName = "input.txt"

data = readInput(fileName)

output = 0


path = data[0]

directions = {}

for line in data[2:]:
    node, points = line.split(" = ")
    points = points[1:-1].split(", ")
    directions[node] = tuple(points)


def allEnd(arr):
    for x in arr:
        if x[2] != "Z":
            return False
    return True


currentNodes = []

for key in directions:
    if key[2] == "A":
        currentNodes.append(key)

traverse = 0

convertedPath = [0 if x == "L" else 1 for x in path]
totalPathLength = len(path)

offsets = []
cycles = []

def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

for i, node in enumerate(currentNodes):
    found = False
    currentNode = node
    offset = 0
    cycle = 0
    traverse = 0
    while not (found and currentNode[2] == "Z"):
        if currentNode[2] == "Z":
            found = True
            offset = traverse
        currentNode = directions[currentNode][convertedPath[traverse % totalPathLength]]
        traverse += 1
    cycle = traverse - offset
    offsets.append(offset)
    cycles.append(cycle)

print(functools.reduce(lambda x, y: compute_lcm(x, y), cycles))