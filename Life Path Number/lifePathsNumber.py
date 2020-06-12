with open("lifeIn.txt", "r") as I:
    N = int(I.readline().strip())
    Input = []
    for n in xrange(N):
        Input.append(tuple(map(int,I.readline().strip().split("/"))))

def reduceNum (num):
    while num >= 10:
        if num % 11 == 0 and num < 40:
            break
        else:
            num = sum(map(int,list(str(num))))
    return num

O = open("lifeOut.txt", "w")


for month,day,year in Input:
    result = reduceNum(month) + reduceNum(day) + reduceNum(year)
    result = reduceNum(result)
    O.write("%d %02d/%02d/%4d\n" % (result,month,day,year))

O.close()

        
