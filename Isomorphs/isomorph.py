with open("isomorphIn.txt", "r") as I:
    N = int(I.readline().strip())
    Input = []
    for n in xrange(N):
        Input.append(I.readline().strip().split(" "))

O = open("isomorphOut.txt", "w")

def compareLength(l):
    return len(l[0]) == len(l[1])

def generatePattern(string):
    l = list(string)
    answer = []
    for i in xrange(len(l)):
        letter = l.pop(0)
        if letter in l:
            answer.append("+" + str(l.index(letter)+1))
        else:
            answer.append("0")
    return " ".join(answer)

for words in Input:
    a,b = words
    if compareLength(words) == True:
        patternA = generatePattern(a)
        patternB = generatePattern(b)
        if patternA == patternB:
            O.write("%s, %s are isomorphs with repetition pattern %s\n" % (a,b,patternA))
        else:
            O.write("%s, %s are not isomorphs\n" % (a,b))
    else:
        O.write("%s, %s have different lengths\n" % (a,b))
        
O.close()
