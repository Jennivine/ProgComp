with open("numeromanIn.txt", "r") as I:
    N = int(I.readline().strip())
    Input = []
    for n in xrange(N):
        Input.append(I.readline().strip())

O = open("numeromanOut.txt", "w")

symbolDict = {"M": 1000,
              "D": 500,
              "C": 100,
              "L": 50,
              "X": 10,
              "V": 5,
              "I": 1,      }

def breakIntoTerms(romanNum):
    List = []
    i = 0
    while i < (len(romanNum) - 1):
        symbol = romanNum[i]
        if (symbol == "C" or symbol == "X" or symbol == "I") and (symbolDict[symbol] < symbolDict[romanNum[i+1]]):
            List.append("".join([symbol,romanNum[i+1]]))
            i += 2
        else:
            List.append(symbol)
            i += 1

    if len(romanNum) == 0:
        return " "
    elif len("".join(List)) < len(romanNum):
        List.append(romanNum[-1])            
    return List

def isValid(romanNumList):
    # given a list of roman numbers
    # either returns True or a string indicating which rule it broke
    if not ruleOne(romanNumList):
        return "Bad1"
    elif not ruleTwo(romanNumList):
        return "Bad2"
    elif not ruleThree(romanNumList):
        return "Bad3"
    elif not ruleFour(romanNumList):
        return "Bad4"
    else:
        return True
    
def ruleOne(romanNumList):
    # returns True if satisfies rule one:
    # it must have at least one symbol, and only combinations of the seven symbols may occur.
    for term in romanNumList:
        for letter in term:
            if not letter in symbolDict:
                return False
    return True
    #return all([[letter in symbolDict for letter in terms] for terms in romanNumList])

def ruleTwo(romanNumList):
    # returns True if satisfies rule two
    list1 = makeDecimal(romanNumList)
    list2 = sorted(list1)[::-1]
    return (list1 == list2)
    

def ruleThree(romanNumList):
    # returns True if satisfies rule three
    for i in xrange(len(romanNumList)-1):
        term = romanNumList[i]
        if len(term) > 1 and symbolDict[romanNumList[i+1][0]] >= symbolDict[term[0]]:
            # "term" is a compound term but the symbol following it
            # is worth more than the first symbol of this compound term.
            return False
    return True

def ruleFour(romanNumList):
    # returns True if satisfies rule four
    for term in romanNumList:
        if len(term) > 1 and (term[0] != "C" and term[0] != "X" and term[0] != "I"):
            print term
            # "term" is a compound term but symbol other than C, X, or I
            # was used as the subtractive symbol in the term
            return False
    return True

def makeDecimal(romanNumList):
    numbers = []
    for term in romanNumList:
        if len(term) == 1:
            # simple term
            numbers.append(symbolDict[term])
        else:
            # compound term
            numbers.append(symbolDict[term[1]] - symbolDict[term[0]])
    return numbers
    
for number in Input:
    # turn a romanNumber into the separate terms and store it in a list
    terms = breakIntoTerms(number)
    print terms
    
    if isValid(terms) == True:
        # every term in this list is valid
        decimal = sum(makeDecimal(terms))
        print >> O, "%-6d %s" % (decimal, number)
    else:
        reason = isValid(terms)
        print >> O, "%-6s %s" % (reason, number)

O.close()
