import os, sys
sys.path.append(os.path.abspath('../..'))
from library import readInput

fileName = None
useSample = True

if useSample:
    fileName = "sample.txt"
else:
    fileName = "input.txt"

data = readInput(fileName)

output = 0