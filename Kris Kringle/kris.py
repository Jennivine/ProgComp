from collections import deque

with open("KrisKringleIn.txt") as f:
    N, L = tuple(map(int,f.readline().strip().split()))
    
    groups = [] # helper list
    people = [] # helper list
    adjDict = dict()

    for i in range(L):
        g = f.readline().strip().split()
        groups.append(g)
        people += g
        for person in g:
            adjDict[person] = []


    for person in people:
        for group in groups:
            if not person in group:
                adjDict[person] += group

# I must say
# printing a list with 360 elements in it was not a good idea
# yeh
# let's just leave it at there...

def isLegal(string):
    # checks that the last person is not giving gift to someone in their group
    path = string.split()
    if path[0] in adjDict[path[-1]]:
        return True
    else:
        return False


possiblePaths = []
pathsCount = 0

q = deque([])
q.append(people[0])

while len(q) != 0:
    curr = q.popleft()
    last = curr.split()[-1]
    for friend in adjDict[last]:
        if friend in curr:
            continue
        else:
            newPath = curr+" "+friend
            if len(newPath.split()) == N:
                if isLegal(newPath):
                    possiblePaths.append(newPath+" "+newPath.split()[0])
                    pathsCount += 1
            else:
                q.append(newPath)

print(possiblePaths[0])
print("Solutions: %d" % (pathsCount) )
