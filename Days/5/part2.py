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

rawIds = [int(x) for x in dataSections[0].split(": ")[1].split(" ")]
idRanges = [(x,y) for x,y in zip(rawIds[::2], rawIds[1::2])]


for section in dataSections[1:]:
    sectionName, *sectionRanges = section.split("\n")
    newRange = []
    for line in sectionRanges:
        destinationMin, sourceMin, mapRange = [int(x) for x in line.split()]
        unMappedRange = []
        for groupMin, groupRange in idRanges:
            startOffset = groupMin - sourceMin
            if -startOffset >= groupRange or startOffset >= mapRange:
                unMappedRange.append((groupMin, groupRange))
                continue
            if startOffset < 0:
                unMappedRange.append((groupMin, -startOffset))
            if -startOffset < groupRange:
                if groupRange > mapRange:
                    unMappedRange.append(((sourceMin + mapRange), groupRange + startOffset - mapRange))
                destStart = destinationMin if startOffset < 0 else destinationMin + startOffset
                newRange.append((destStart, min(groupRange, mapRange)))
        idRanges = unMappedRange
    idRanges = newRange + idRanges
print(min([x for x, _ in idRanges]))
                
# print(min(currentIds))