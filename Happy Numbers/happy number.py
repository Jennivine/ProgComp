def happy(n):
    cycle = set()
    
    while n != 1:
        if n in cycle:
            return False
        nextN = 0
        for digit in str(n):
            nextN += int(digit)**2
        cycle.add(n)
        n = nextN

    return True

count = 0
for n in range(1, 1000):
    if happy(n):
        count += 1
