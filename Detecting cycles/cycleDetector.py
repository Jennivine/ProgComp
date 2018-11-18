def cycleGenerator (a,b,c,d):
    listValues = [d]
    value = (a*d*d + b) % c
    
    while not value in listValues:
        listValues.append(value)
        value = (a*value*value + b) % c

    valueIndex = listValues.index(value)
    string = len(listValues[:valueIndex])
    cycle = len(listValues[valueIndex:])
    print "repeat = %d, string = %d, cycle = %d" % (value, string, cycle)

cycleGenerator(1,7,43,2)

cycleGenerator(1,3,100,11)
cycleGenerator(5,5,8888,88)
cycleGenerator(1,9,666,10)
cycleGenerator(1,1,31,1)
