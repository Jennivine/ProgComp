with open("humanTimeIn.txt") as f:
    n = int(f.readline().strip())
    query = []
    
    for i in range(n):
        query.append(f.readline().strip())


for time in query:
    m = int(time[2:])
    h = int(time[:2])

    minutes = ""
    connector = ""
    hour = ""

    # deal with minutes first
    if m > 30:
        connector = "to"
        m = 60 - m
        h = (h+1) % 24
        minutes = str(m)+" minutes"
    else:
        connector = "past"
        minutes = str(m)+" minutes"

    # special cases for minutes
    if m == 1:
        minutes = str(m)+" minute"
    elif m == 15:
        minutes = "a quarter"
    elif m == 30:
            minutes = "half"

    # now deal with the hour
    if h <= 12:
        # AM
        if h == 0:
            hour = "12 midnight"
        elif h == 12:
            hour = "12 noon"
        else:
            hour = str(h)+"am"    
    else:
        # PM
        h = h % 12
        hour = str(h)+"pm"    
    
    # output string
    if m != 0:
        string = time+" is "+minutes+" "+connector+" "+hour
    else:
        string = time+" is "+hour

    print(string)
    
    

