stack = []

def inTopost(infix):
    ans = ""
    invalid = False
    for c in infix:
        if c.isdigit() or c.isalpha():
            ans += c
        else:
            if c == "(":
                stack.append(c)
            elif c == ")":
                while stack[-1] != "(":
                    ans += stack.pop()
                    if len(stack) == 0:
                        ans = "missing left parenthesis"
                        invalid = True
                        break
                stack.pop()
            else:
                if not c in operators:
                    ans = "unknown operator " + c
                    invalid = True
                    break
                while len(stack) != 0:
                    top = stack[-1]
                    if top == "(" or (precedence[top] < precedence[c]) or (precedence[top] == precedence[c] and la[top] == False):
                        break
                    ans += stack.pop()
                stack.append(c)

    if not invalid:
        while len(stack) != 0:
            top = stack.pop()
            if top == "(":
                ans = "missing right parenthesis"
                break
            ans += top
    
    return ans

precedence = dict()
la = dict()
operators = set()

with open("input.txt") as f:
    o = f.readline().strip().split(" ")
    for OP in o[1:]:
        if OP[-1] == "L":
            la[OP[0]] = True
        else:
            la[OP[0]] = False
            
        precedence[OP[0]] = int(OP[1])
        operators.add(OP[0])

    n = int(f.readline().strip())
    for i in range(n):
        line = f.readline().strip()
        print inTopost(line)
        
        
