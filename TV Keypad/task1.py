



def checkWord(word):
    word = word.lower()
    for i in range(len(word)-1):
        c1 = ord(word[i])-97
        c2 = ord(word[i+1])-97
        if c1%7 == c2%7:
            continue
        if 0 <= c1 <= 6 and 0 <= c2 <= 6:
            continue
        if 7 <= c1 <= 13 and 7 <= c2 <= 13:
            continue
        if 14 <= c1 <= 20 and 14 <= c2 <= 20:
            continue
        if 21 <= c1 <= 25 and 21 <= c2 <= 25:
            continue
        return False
    return True

with open("task1topics.dat") as f:
    for i in range(200):
        word = f.readline().strip()
        if checkWord(word):
            print(word)
        
        
