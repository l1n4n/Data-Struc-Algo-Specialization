#Uses python3
import sys


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


from collections import defaultdict

def build_trie(patterns):
    """
    Construct a trie from a collection of patterns.
    Input Format. a list of strings Patterns    
    """
    tree = defaultdict(dict)    
    node_num = 1

    for string in patterns:
        currentNode = 0
        for i in range(len(string)):            
            currentSymbol = string[i]
            
            if currentSymbol in tree[currentNode]:
                currentNode = tree[currentNode][currentSymbol]
            else:
                tree[currentNode][currentSymbol] = node_num 
                currentNode = node_num
                node_num += 1    
    return tree



if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

