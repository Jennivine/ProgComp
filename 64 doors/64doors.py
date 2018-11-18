doors = dict(zip([i for i in xrange(1,65)],[False]*64))


for i in xrange(1,65):
    for j in xrange(1,65):
        if i % j == 0:
            if doors[i] == False:
                doors[i] = True
            else:
                doors[i] = False

for i,v in doors.iteritems():
    if v:
        print i,
