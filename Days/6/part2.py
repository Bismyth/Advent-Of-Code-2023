import os, sys
sys.path.append(os.path.abspath('../..'))
from library import readInput
import math

fileName = None
useSample = False

if useSample:
    fileName = "sample.txt"
else:
    fileName = "input.txt"

data = readInput(fileName)

output = 0

def parseNumbers(l):
    return int("".join([x.strip() for x in l.split(": ")[1].split(" ") if x != ""]))


time = parseNumbers(data[0])
distance = parseNumbers(data[1])

output = 0

def calculateQuadratic(a, b, c):
    d = (b**2) - (4*a*c)
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    return (x1, x2)

def calculateMatches(t, d):
    x1, x2 = calculateQuadratic(-1, t, -d)
    return (math.floor(x1) - math.ceil(x2)) + 1

print(calculateMatches(time, distance))