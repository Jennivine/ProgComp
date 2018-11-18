def generateEven(oddL):
    evenL = [0]
    for i in xrange(1,len(oddL)+1):
        evenL.append(evenL[i-1] + oddL[-i])

    evenL.reverse()
    return evenL

def generateOdd(evenL):
    oddL = [0]
    for i in xrange(1,len(evenL)+1):
        oddL.append(oddL[i-1] + evenL[i-1])

    return oddL

        
zigs = [1]
zags = []

prevL = [1]
for i in xrange(1,16):
    if i % 2 == 0:
        newL = generateEven(prevL)
        zigs.append(newL[0])
    else:
        newL = generateOdd(prevL)
        zags.append(newL[-1])
    prevL = newL

print "Zigs: " + " ".join(str(x) for x in zigs)
print "Zags: " + " ".join(str(x) for x in zags)
print " >> ".join(str(x) for x in prevL)
