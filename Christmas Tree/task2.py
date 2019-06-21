import random

def printTree(n):
    bWidth = 2*n - 1
    for r in range(n):
        rWidth = 2*r+1
        row = buildRow(r, rWidth)
        s = (bWidth - rWidth)/2
        print(" "*s + row)
    s = (bWidth - 1)/2
    print(" "*s + "#")
    if n >= 12:
        print(" "*s + "#")
    base = int(2*max(1,int(n/6))+1)
    s = (bWidth - base)/2
    print(" " *s + "="*base)

def buildRow(r, rWidth):
    if r == 0:
        return "+"
    row = "*"
    i = 1
    while i < rWidth - 1:
        if random.randint(0,10) < 4:
            row += "o*"
            i += 2
        else:
            row += "*"
            i += 1
    if len(row) < rWidth:
        row += "*"
    return row

printTree(7)
print
printTree(22)
        
