def encode(fourDigitNumber):
    count = 0
    r = 0
    for digit in fourDigitNumber:
        digit = int(digit)
        digit = int(digit)
        d = (3*digit + 7) % 10
        r += (2 ** (3*d+2)) + (count*(8**d))
        count += 1
    return r


def match(codeOne,codeTwo):
    bulls = ""
    cows = ""
    for pos in range(10):
        p = (codeOne/(8**pos)) % 8
        q = (codeTwo/(8**pos)) % 8
        r = p-q
        s = 2*r + 3*q
        if s > 11 and s > 2*r:
            if s == 3*p:
                bulls += ('B')
            else:
                cows += ('C')
    return bulls+cows

def buildCandidates():
    candidateList = []

    for number in xrange(100,9900):
        number = str(number)
        likely = True
        for digit in number:
            if number.count(digit) > 1:
                likely = False
            if digit == "0" and len(number) == 3:
                likely = False

        if likely:
            if len(number) == 3:
                number = "0"+number
            candidateList.append(number)
    
    return candidateList

O = open("mooOut.txt","w")

def findSolution(secret):
    candidateList = buildCandidates()
    O.write("Initial candidate list size = %d.\n" % len(candidateList))

    turnNum = 0
    score = ""

    while len(candidateList) > 0:
        turnNum += 1

        #generating the guess of each turn        
        if len(candidateList) == 1:
            guess = candidateList[0]
        else:
            index = (len(candidateList) +1) / 2
            guess = candidateList[index]

        score = match(secret,encode(guess))
        if score == "BBBB":
            #found the secret number!
            break

        #removing numbers from the candidacy list
        toRemove = []
        for candidate in candidateList:
            compare = match(encode(guess), encode(candidate)) 
            if compare != score:
                toRemove.append(candidate)

        for candidate in toRemove:
            candidateList.remove(candidate)

        #formatting output
        O.write("Guess %d %s gives %-4s Candidates remaining: %d\n" %
                (turnNum, guess, score, len(candidateList)))

    O.write("Solution: %s\n\n" % guess)

secretNumbers = [216616, 12748856]

for number in secretNumbers:
    findSolution(number)


print encode("0586")
print match(941099524, 939547652)
print match(encode("6438"),encode("0638"))

O.close()
