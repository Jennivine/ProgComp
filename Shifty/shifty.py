with open("decipher.txt","r") as I:
    text = list(I.read())

def decipher(a,s,text):
    newText = ""
    allChar = [chr(n) for n in xrange(32,127)]
    counter = 0
    shiftLength = 0
    resetValue = s
    for i in xrange(len(text)):
        if counter == shiftLength:
            counter = 0
            s = resetValue
            shiftLength = (a*s+1) % 95
            resetValue = (a*shiftLength+1) % 95
        
        oldChar = text[i]
        if oldChar == '\n' or oldChar == '\r':
            continue
        
        loc = allChar.index(oldChar)
        newChar = allChar[(loc-s)%95]
        newText += newChar
        s +=1
        counter +=1
        
    return newText

for a in xrange(1,96):
    if (42*a+1) % 95 == 28:
        print a

print decipher(21,42,text)
