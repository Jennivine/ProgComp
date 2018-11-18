def rats(number):
    reversedNumber = int(str(number)[::-1])
    add = number + reversedNumber
    digits = [i for i in str(add)]
    digits.sort()
    answer = int("".join(digits))
    return answer

def findCycle(number):
    sortedResults = [number]
    while number <= 10**12:
        number = rats(number)
        if number in sortedResults:
            return sortedResults[sortedResults.index(number):]
        sortedResults.append(number)
    return None

allCycles = dict()

for n in xrange(1,10000):
    cycle = findCycle(n)
    
    if cycle != None:
        cycle = " ".join((str(n) for n in cycle))

        if cycle in allCycles:
            allCycles[cycle] += 1
        else:
            allCycles[cycle] = 1

for cycle, count in sorted(allCycles.iteritems(), key = lambda (k,v):(len(k.split(" ")),int(k.split(" ")[0]))):
    print "Period: %d, occurs %d times, cycle: %s" % (len(cycle.split(" ")),count,cycle)
