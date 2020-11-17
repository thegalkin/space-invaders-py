with open("youWin.map", "r") as mapFile:
    f = mapFile.read()
    f = f.replace("[", '')
    #f = f.replace("]", "\n")
    out = ''
    for line in f:
        tempLine = list(line.split(","))
        for i in range(len(tempLine)):
            tempLine[i] = int(tempLine[i])
        out += tempLine + '\n'
    
with open("youWin.map", "w") as mapFile:
    mapFile.write(f)