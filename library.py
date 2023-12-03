def readInput(fileName, *, newLine = True):
    with open(fileName, "r") as f:
        input = f.read()
        if newLine:
            return input.split('\n')
        else:
            return input