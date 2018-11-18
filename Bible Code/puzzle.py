import re
with open("puzzle.txt", "r") as I:
    InputLines = I.read().lower()
    InputLines = list(re.sub("[^a-z]", "", InputLines))

def solve():
    global InputLines

    for index in xrange(len(InputLines)):
        if InputLines[index] == "i":
            if InputLines[index::12][:3] == ["i","v","a"]:
                print "".join(InputLines[index::12][:21])
                
solve()
