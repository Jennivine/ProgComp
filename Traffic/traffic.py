with open("trafficIn.txt") as f:
    N, C = tuple(map(int, f.readline().strip().split()))
    red  = list(f.readline().strip())
    blue = list(f.readline().strip())

    R = len([x for x in red if x == "R"])
    B = len([x for x in blue if x == "B"])
    
    
# better to simulate it in a matrix?
L = 2*N + 1
matrix = [["" for i in range(L)] for i in range(L)]

matrix[L//2] = red
for i in range(L):
    matrix[i][L//2] = blue[i]

def move(OG,c):
    # given an array, returns the a modified array
    new = ["" for i in range(len(OG))]
    n = 0
    
    for i in range(len(OG)-1):
        if new[i] != "":
            continue
        
        if OG[i] != c:
            new[i] = OG[i]
        else:
            if OG[i+1] == ".":
                new[i] = "."
                new[i+1] = c
                n += 1
            else:
                new[i] = c
    
    if OG[0] == "." and OG[-1] == c:
        new[0] = c
        new[-1] = "."
        n += 1
    else:
        if new[-1] == "":
            new[-1] = OG[-1]

    return new,n
    

def cycle():
    # update matrix when called
        # returns the number of red and blue cars moved
    moved = 0
    # red half-cycle
    OG = matrix[L//2]
    new, n = move(OG, "R")

    matrix[L//2] = new
    moved += n

    # blue half cycle
    OG = [matrix[i][L//2] for i in range(L)]
    new, n = move(OG, "B")

    for i in range(L):
        matrix[i][L//2] = new[i]
    
    moved += n
    return moved

# solve
aveVel = 0
curVel = 0

for i in range(C):
    cars = cycle()
    curVel = cars / (R+B)
    aveVel += curVel

aveVel /= C

print("Current velocity: %.3f, average velocity = %.3f" % (curVel, aveVel) )
print("".join(matrix[L//2]))
print("".join([matrix[i][L//2] for i in range(L)]))



