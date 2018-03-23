# python3

from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
    if v == None:
        return
    v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v

# rotates v one step up --> v is above its old parent
def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else: 
            grandparent.right = v

# rotates v two steps up --> v is above its old grandparent
def bigRotation(v):    
    if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)    
    else: 
    # Zig-zag
        smallRotation(v)
        smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): 
    v = root
    last = root # last one that has been visited
    next = None # the next bigger one than the target key; if the key is larger than every node, then next wont get updated
    while v != None: # not reaching the bottom of the tree
        if v.key >= key and (next == None or v.key < next.key): # case1: v.key is larger or equal to and v.key is the next bigger one
            next = v    
        last = v # get updated no matter what
        if v.key == key: # case2: find the key
            break    
        if v.key < key: # case3: v.key is smaller, so search its right
            v = v.right
        else: # case4: v.key > key(equal case catched by case2) and next!= None and v.key >= next.key : the current node is larger but not the next bigger one
            v = v.left      
    root = splay(last)
    return (next, root) # next.key might be key or the next bigger one, root is the deepest visited node

def split(root, key):  
    (result, root) = find(root, key)  
    if result == None: # the key is the largest   
        return (root, None)  
    right = splay(result) # new root (of 'right') is the key or its next bigger one
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)

  
def merge(left, right):
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left # find the smallest one in the right tree
    right = splay(right)
    right.left = left
    update(right) # the sum of left does not change, so no need of update
    return right

  
# Code that uses splay tree to solve the problem
                                    
root = None

def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right == None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)  
    root = merge(merge(left, new_vertex), right)
  
def erase(x): 
    global root    
    (less_than_x, g_or_equal_x) = split(root, x)
    (x_to_x1, g_or_equal_x1) = split(g_or_equal_x, x + 1)
    root = merge(less_than_x, g_or_equal_x1)

def search(x): 
    global root
    result, root = find(root, x) # find reset the root
    if not result:
        return False
    return result.key == x
  
def sum(fr, to): 
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = 0
    # if fr is bigger than every node, then middle == None
    if middle:
        ans = middle.sum
    root = merge(left, (merge(middle, right))) # merge no matter what!
    return ans

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
