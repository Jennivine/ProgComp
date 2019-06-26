# This problem deals with family trees
# but I didn't raelise that at first
# so I asked
# what if the trees have cycles in it

with open("inheritance.txt") as f:
    N = int(f.readline())
    tree = {}
    dead = set()
    
    # build adjacency list
    for i in range(N):
        children = f.readline().split(":")
        node = children[0]
        
        # format node to get rid of extra info
        if node[-1] == "x":
            node = node[:-1]
            dead.add(node)
        elif node[-1] == "*":
            node = node[:-1]
            
        tree[node] = children[1].split()

def rearrange(l):
  return [x for x in l if x[0] == "M"] + \
         [x for x in ["+".join([x for x in l if x[0] == "F"])] if x != ""]

for node in tree:
  tree[node] = rearrange(tree[node])

# generator functions 
def preOrder(n):
    yield n
    for c in tree[n]:
        if c[0] == "F":
            yield c
        else:
            yield from preOrder(c)

def postOrder(n):
  for c in tree[n]:
    if c[0] == "F":
      yield c
    else:
      yield from postOrder(c)

# output results
for n in preOrder("M0"):
    if n[0] == "F" or n in dead:
      continue
    else:
      print(n, end=" ")   

for n in postOrder("M0"):
    if n[0] == "M" or n in dead:
      continue
    else:
      print(n, end=" ")   

print()   
