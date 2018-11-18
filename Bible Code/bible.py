with open("bibleIn.txt", "r") as I:
    InputLines = I.read() #str object

def isAlpha(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z')

def realIndex(string,index):
    #passes in a virtual index and
    #returns the real index of that letter in string

    letterCount = 0
    for indices, char in enumerate(string):
        if isAlpha(char):
            letterCount += 1
        if letterCount == index:
            return indices

def findStart(index,Input):
    while Input[index] != '\n' and index >= 0:
        index -= 1

    return (index+1)

def findEnd(index,Input):
    while Input[index] != '\n' and index < len(Input)-1:
        index += 1
        
    return (index)

def ELS(offset,cycle,n):
    global InputLines
    
    elsIndex = []
    
    startingIndex = realIndex(InputLines,offset)
    elsIndex.append(startingIndex)
    
    i = 1
    while i < n:
        offset += cycle 
        index = realIndex(InputLines, offset)
        elsIndex.append(index)
        i += 1

    return elsIndex

O = open("bibleOut.txt", "w")

def formatInput(elsIndexList, Input):
    ELS = [Input[i] for i in elsIndexList]
    ELS = "".join(ELS)

    elsIndexList.sort()

    l = list()

    startingIndex = findStart(elsIndexList[0],Input)
    endingIndex = findEnd(elsIndexList[-1],Input)
    
    for index in xrange(startingIndex,endingIndex):
        if (index) in elsIndexList:
            l.append("[")

        l.append(Input[index])
        
        if (index) in elsIndexList:
            l.append("]")
            
    Output = "".join(l)
    O.write(Output)
    O.write(ELS+'\n'+'\n')

formatInput(ELS(72,1,6),InputLines)
formatInput(ELS(416,12,4),InputLines)
formatInput(ELS(465,-36,5),InputLines)
formatInput(ELS(427,-100,5),InputLines)

O.close()
