import os, sys
sys.path.append(os.path.abspath('../..'))
from library import readInput

fileName = None
useSample = False

if useSample:
    fileName = "sample.txt"
else:
    fileName = "input.txt"

data = readInput(fileName, newLine = False)

output = 0

lineLength = data.find("\n") + 1

for i, c in enumerate(data):
    if c == "*":
        seen = set()
        product = 1
        for x in range(-1,2):
            for y in range(-1,2):
                index = i + x + (y * lineLength)
                if data[index] in "0123456789":
                    while data[index - 1] in "0123456789":
                        index -= 1
                    if index in seen:
                        continue
                    seen.add(index)
                    num = data[index]
                    while data[index + 1] in "0123456789":
                        index += 1
                        num += data[index]
                    product *= int(num)
        if len(seen) == 2:
            output += product
print(output)
