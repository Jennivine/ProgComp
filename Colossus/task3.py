path = {}

def R1(A,B):
    return (A+1, B*2)

def R2(A,B):
    return (A*2, B+1)

def printRoute(n1, n2):
    if path[(n1,n2)] == (n1,n2):
        print "%d,%d " % (n1, n2),
        return

    new1, new2 = path[(n1,n2)]
    printRoute(new1, new2)
    print "%d,%d " % (n1, n2),
    
def BFS(A,B):
    queue = []
    visited =  set()
    
    path[(A,B)] = (A,B)
    queue.append((A,B))    
    visited.add((A,B))

    while len(queue) != 0:
        top = queue.pop(0)
        n1, n2 = top
        
        if n1 == n2:
            break

        newT1 = R1(n1, n2)
        n11, n12 = newT1
        if not (n11, n12) in visited:
            queue.append((n11, n12))
            path[(n11,n12)] = (n1,n2)
            visited.add((n11,n12))

        newT2 = R2(n1,n2)
        n21, n22 = newT2
        if not (n21, n22) in visited:
            queue.append((n21, n22))
            path[(n21,n22)] = (n1,n2)
            visited.add((n21,n22))

    printRoute(n1, n2)

with open("task3.txt") as f:
    n = int(f.readline().strip())

    for i in range(n):
        A,B = tuple(map(int, f.readline().strip().split()))
        BFS(A,B)
        print
    
