with open("triffids.txt") as f:
    N = int(f.readline().strip())
    passphrase = f.readline().strip()
    queries = []
    
    for i in range(N):
        queries.append(f.readline().strip())
        
cipherToLetter = dict()
letterToCipher = dict()

def generate(passphrase):
    global cipherToLetter
    global letterToCipher
    
    uniqueElements = list(dict.fromkeys(list(passphrase)))
    uniqueSet = set(uniqueElements)

    cipher = [111,112,113,121,122,123,131,132,133,\
              211,212,213,221,222,223,231,232,233,\
              311,312,313,321,322,323,331,332,333]

    if not " " in uniqueSet:
        uniqueElements.append(" ")

    for i in range(65,91):
        if not chr(i) in uniqueSet:
            uniqueElements.append(chr(i))    
    
    letterToCipher = dict(zip(uniqueElements, cipher))
    cipherToLetter = dict(zip(cipher, uniqueElements))


def expand(cipher):
    ls = []
    for letter in cipher:
        ls += list(str(letterToCipher[letter]))

    return ls

def collect(ls):
    L = len(ls)
    magicN = int(L/3)
    ciphers = []
    for i in range(magicN):
        ciphers.append("".join([ls[i], ls[i+magicN], ls[i+magicN*2]]))
    return ciphers

def decipher(ls):
    string = ""
    for cipher in ls:
        string += cipherToLetter[int(cipher)]
    return string

# solve 
generate(passphrase)
for cipher in queries:
    string = decipher(collect(expand(cipher)))
    print(string)
        
