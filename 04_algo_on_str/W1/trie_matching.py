# python3
import sys

# NA = -1

class Node:
    def __init__ (self):
        self.next = {}
        self.is_leaf = False

def solve(text, n, patterns):
    result = []
    root = Node()
    # add patterns to a trie structure
    for pattern in patterns:
        currentNode = root
        for i, c in enumerate(pattern):
            if c not in currentNode.next:
                currentNode.next[c] = Node()
            if i == len(pattern) - 1:
                currentNode.next[c].is_leaf = True
            else:
                currentNode = currentNode.next[c]
    
    # search multiple patterns using the built trie
    for i in range(len(text)): # iterate len(text) times
        index = i # search begins at position i of the text
        currentNode = root # searching from the root
        while index < len(text): 
            c = text[index] 
            if c not in currentNode.next: # if the first letter does not match any label outgoing from the node, then no match
                break
            currentNode = currentNode.next[c] # if first match, then move on to the matching branch
            if currentNode.is_leaf: # if the edge's end is a leaf, i.e., all former letters match, then the whole pattern is matched
                result.append(i)
                break
            index += 1 # search begins from the next position of the text

    return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
