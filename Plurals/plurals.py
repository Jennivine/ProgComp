with open("pluralsIn.txt", "r") as I:
    N = int(I.readline().strip())
    Input = []
    for n in xrange(N):
        Input.append(tuple(I.readline().strip().split(" ")))      

O = open("pluralsOut.txt", "w")

def plural(word):
    word = list(word)
    if word[-1] in set(["s", "x", "z"]) or "".join(word[-2:]) in set(["sh","ch"]):
        word.append("es")
    elif word[-1] == "o" and word[-2] not in set(["a","e","i","o","u","y"]):
        word.append("es")
    elif word[-1] == "y" and word[-2] not in set(["a","e","i","o","u"]):
        word[-1] = "ies"
    elif word[-2:] == ["f","e"] and word[-3] != "f":
        word[-2:] = "ves"
    elif word[-1] == "f" and word[-2] != "f":
        word[-1] = "ves"
    else:
        word.append("s")

    return "".join(word)

plural("knife")

for line in Input:
    Q, word = line #word will always be in its singular form
    if int(Q) == 0:
        O.write("no %s\n" % plural(word))
    elif int(Q) == 1:
        O.write("one %s\n" % word)
    else:
        O.write("%s %s\n" % (Q, plural(word)))

O.close()
