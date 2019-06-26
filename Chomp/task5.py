r = 3 # r pieces per row
c = 5 # c pieces per column

def makeChoc(r,c):
    choc = []
    for i in range(c):
        choc.append(r)

    return choc

def moveA(choc):
    
    # if block is in a losing position
        # eat poison
    if isLosing(choc):
        return [0,0]
    
    # if it can leave opponent in a losing position, take it
    strategy = winningMove(choc)
    if strategy != None:
        return strategy

    # default stragety
    i = len(choc)-1
    while i >= 1:
        if choc[i] >= 2:
            return [i,choc[i]-1]

        i -= 1

    return [0, max(0, choc[0]-1)]

def moveB(choc):
    # if block is in a losing position
        # eat poison
    if isLosing(choc):
        return [0,0]

    # if it can leave opponent in a losing position, take it
    strategy = winningMove(choc)
    if strategy != None:
        return strategy

    # default stragety
    if len(choc) >= 2:
        return [1, choc[1]-1]

    return [0, max(0, choc[0]-1)]

def eatBlock(choc, square):
    x,y = square

    for i in range(x, len(choc)):
        if choc[i] > y:
            choc[i] = y

    while choc[-1] == 0:
        choc.pop(-1)

    return choc

def printBlock(choc):
    for i in range(len(choc)):
        row = ""
        
        for j in range(choc[i]):
            if j == 0 and i == 0:
                row += "@"
            else:
                row += "#"

        if row != "":
            print(row)

    print ""

def isLosing(choc):
    losingPos = {(2,2,1),(3,2),(4,2,2),(3,3,1,1)}
    
    if len(choc) == choc[0] or tuple(choc) in losingPos:
        return True

    return False

def winningMove(choc):
    n = len(choc)

    # special cases
    if choc == [4,4,4]:
        return [1,2]

    if choc == [3,3,3,3]:
        return [2,1]

    if choc == [2,2,2]:
        return [2,1]

    if choc == [3,3]:
        return [1,2]

    # more general cases, but still hardcoded because HA
    if n > 2 and choc[0:2] == [3,2]:
        return [2,0]
    if n == 2 and (choc[0]>3 and choc[1] == 2):
        return [0,3]

    if n > 3 and choc[0:3] == [2,2,1]:
        return [3,0]
    if n == 3 and (choc[0] > 2 and choc[1] > 2 and choc[2] == 1):
        return [0,2]

    if n > 4 and choc[0:4] == [3,3,1,1]:
        return [4,0]
    if n == 4 and (choc[0] > 3 and choc[1] > 3 and choc[2] == 1 and choc[3] == 1):
        return [0,3]

    if n > 3 and choc[0:3] == [4,2,2]:
        return [3,0]
    if n == 3 and (choc[0] > 4 and choc[1] == 2 and choc[2] == 2):
        return [0,4]

    # last couple of things to check
    if choc[0] == len(choc) and choc != [1]:
        return [1,1]
    
    return None


block = makeChoc(r,c)
printBlock(block)

while True:
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
