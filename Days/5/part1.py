import os, sys
sys.path.append(os.path.abspath('../..'))
from library import readInput

fileName = None
useSample = False

if useSample:
    fileName = "sample.txt"
else:
    fileName = "input.txt"

data = readInput(fileName, newLine=False)

output = 0

dataSections = data.split("\n\n")

currentIds = [int(x) for x in dataSections[0].split(": ")[1].split(" ")]

for section in dataSections[1:]:
    sectionName, *sectionRanges = section.split("\n")
    touched = set()
    for rang in sectionRanges:
        d, s, r = [int(x) for x in rang.split()]
        for x, i in enumerate(currentIds):
            if x in touched:
                continue
            if i >= s and i <= s + r:
                touched.add(x)
                currentIds[x] = d + (i - s)
                
print(min(currentIds))