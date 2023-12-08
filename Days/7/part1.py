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

cardRank = "23456789TJQKA"

def cardScores(hand):
    return tuple([cardRank.index(x) for x in hand])

def handScore(hand):
    cards = [0] * len(cardRank)
    for c in hand:
        cards[cardRank.index(c)] += 1
    cards.sort(reverse=True)

    firstScore = 0
    if cards[0] == 5:
        firstScore = 7
    elif cards[0] == 4:
        firstScore = 6
    elif cards[0] == 3 and cards[1] == 2:
        firstScore = 5
    elif cards[0] == 3:
        firstScore = 4
    elif cards[0] == 2 and cards[1] == 2:
        firstScore = 3
    elif cards[0] == 2:
        firstScore = 2
    else:
        firstScore = 1
    
    return (firstScore, *cardScores(hand))

output = []

for line in data:
    hand, bet = line.split(" ")
    output.append((handScore(hand), int(bet)))

output.sort(reverse=True)

# print(output)
total = len(output)

a = [(x[1], (total-i)) for i, x in enumerate(output)]
print(sum([x*y for x,y in a]))