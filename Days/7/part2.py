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

cardRank = "J23456789TQKA"

def cardScores(hand):
    return tuple([cardRank.index(x) for x in hand])

def handScore(hand):
    cards = [0] * len(cardRank)
    for c in hand:
        cards[cardRank.index(c)] += 1
    jacks = cards[0]
    del cards[0]
    cards.sort(reverse=True)
    
    firstScore = 0
    if cards[0] + jacks == 5:
        firstScore = 7
    elif cards[0] + jacks == 4:
        firstScore = 6
    elif sum(cards[0:2]) + jacks == 5:
        firstScore = 5
    elif cards[0] + jacks == 3:
        firstScore = 4
    elif sum(cards[0:2]) + jacks >= 4:
        firstScore = 3
    elif cards[0] + jacks == 2:
        firstScore = 2
    else:
        firstScore = 1
    
    return (firstScore, *cardScores(hand))

output = []

translate = {
    7: "5K",
    6: "4K",
    5: "FH",
    4: "3K",
    3: "2P",
    2: "2K",
    1: "1K"
}

for line in data:
    hand, bet = line.split(" ")
    newInput = (handScore(hand), int(bet))
    output.append(newInput)



output.sort(reverse=True)

# print(output)
total = len(output)

a = [(x[1], (total-i)) for i, x in enumerate(output)]
print(sum([x*y for x,y in a]))