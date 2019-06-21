zigzag = [[1],[0,1]]

def generate_even(i):
    l = [0]
    for j in range(1,i+1):
        n = l[j-1]+zigzag[i-1][-j]
        l.append(n)
    return l[::-1]

def generate_odd(i):
    l = [0]
    for j in range(1,i+1):
        n = l[j-1]+zigzag[i-1][j-1]
        l.append(n)
    return l

for i in range(2,16):
    if i % 2 == 0:
        row = generate_even(i)
    else:
        row = generate_odd(i)
    zigzag.append(row)

for i in range(0,16,2):
    print zigzag[i][0],

print

for i in range(1,16,2):
    print zigzag[i][-1],

print

print " >> ".join(map(str,zigzag[15]))
