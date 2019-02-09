def RAP(num):
    return num + int(str(num)[::-1])

rapMap = set()
rapDict = dict()
noPalindrome = 0

for i in xrange(1, 1001):
    n = RAP(i)
    while n != int(str(n)[::-1]) and n < 2**48:
        n = RAP(n)
 
    if n >= 2**48:
        print i, "does not lead to a palindrome"
        noPalindrome += 1
    else:
        rapMap.add(n)
        if n in rapDict:
            rapDict[n].append(i)
        else:
            rapDict[n] = [i]

rapMap = sorted(list(rapMap))
mostCommon = 0
commonCount = 0
for key in rapDict:
    if len(rapDict[key]) > commonCount:
        commonCount = len(rapDict[key])
        mostCommon = key
