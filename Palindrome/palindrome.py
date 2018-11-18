import re
with open("palindromeIn.txt", "r") as I:
    N = int(I.readline().strip())
    Input = []
    words = []
    for n in xrange(N):
        word = I.readline().strip()
        words.append(word)
        Input.append(list(re.sub("[^a-zA-Z]","",word).lower()))

O = open("palindromeOut.txt", "w")

for index,word in enumerate(Input):
    if word == word[::-1]:
        O.write("Yes \"%s\"\n" %(words[index]))
    else:
        O.write(" No \"%s\"\n" %(words[index]))

O.close()
