# input found here: https://adventofcode.com/2023/day/1/input

with open("input.txt", "r") as f:
    data = f.read().split("\n")

numbers = "0123456789"

total = 0

numberLetters = [
  "zero",
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine"
]

replaceNumberLetters = True

for row in data:
  first = ""
  last = ""
  firstIndex = -1
  lastIndex = -1
  for i, l in enumerate(row):
    if l in numbers:
      last = l
      lastIndex = i
      if first == "":
        first = l
        firstIndex = i
  if replaceNumberLetters:
    for numberLetter in numberLetters:
      fIndex = row.find(numberLetter)
      lIndex = row.rfind(numberLetter)
      if (fIndex != -1) and (fIndex < firstIndex or firstIndex == -1):
        first = str(numberLetters.index(numberLetter))
        firstIndex = fIndex
      if (lIndex != -1) and lIndex > lastIndex:
        last = str(numberLetters.index(numberLetter))
        lastIndex = lIndex
  total += int(first+last)

print(total)