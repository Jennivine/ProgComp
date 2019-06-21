r = 3
c = 5

def makeChoc(r,c):
    choc = []
    for i in range(c):
        row = []
        for j in range(r):
            if i == 0 and j ==0:
                row.append(-1)
            else:
                row.append(1)
        choc.append(row)
    return choc

def moveA(choc):
    global r
    global c
    for i in range(c-1, 0, -1):
        if choc[i].count(1) >= 2:
            return [i, choc[i].count(1)-1]
    return [0, max(0, choc[0].count(1)-1)]

def moveB(choc):
    global r
    global c
    if r >= 2:
        if choc[1].count(1) > 0:
            return [1, choc[1].count(1)-1]
    return [0, max(0, choc[0].count(1)-1)]

def eatBlock(choc, square):
    global r
    global c
    x,y = square
    for i in range(x, c):
        for j in range(y, r):
            choc[i][j] = 0
    return choc

def printBlock(block):
    for i in range(len(block)):
        row = ""
        for j in block[i]:
            if j == 1:
                row += "#"
            if j == -1:
                row += "@"
        print(row)

block = makeChoc(r,c)
printBlock(block)
i = 0
while i <5:
    a = moveA(block)
    print("A eats (%d, %d)" % (a[0]+1, a[1]+1))
    if a == [0,0]:
        print("Player A loses")
        break
    block = eatBlock(block, a)
    printBlock(block)
    
    b = moveB(block)
    print("B eats (%d, %d)" % (b[0]+1, b[1]+1))
    if b == [0,0]:
        print("Player B loses")
        break
    block = eatBlock(block, b)
    printBlock(block)
    i+=1
    
