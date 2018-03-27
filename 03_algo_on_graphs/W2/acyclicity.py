#Uses python3

import sys
def explore(v, adj, visited, path):     
    visited[v] = 1 # mark v as visited
    path[v] = 1 # add v to the current exploring path
    for w in adj[v]:        
        if path[w]: # if w is in the path, then a cycle is found
            return 1
        if visited[w]: # if w has been visited, since the program has not return 1 before, w must leads to no cycle 
            pass
        if not visited[w] and explore(w, adj, visited, path): # explore w if not visited, and return the result
            return 1
        # a less wordy way to write is
        # if path[w] or explore(w, adj, visited, path):
        #    return 1
        # but this takes a little bit longer and a little bit more memory 
    path[v] = 0 # mark v as 0 for the future new exploration starting from another vertex
    return 0


def acyclic(adj):
    """Check if a directed graph contains a cycle. 
    Input: adjacency list representation, vertices are integers starting from 0. 
    e.g. [[1], [2], [0], [0]] means 0-->1, 1-->2, 2-->0, 3-->0
    output: 1 if has cycle, 0 if not
    """    
    n = len(adj)
    visited = [0] * n 
    path = [0] * n # mark the seen node during ONE exploration starting from v
    for v in range(n):
        if not visited[v]:
            if explore(v, adj, visited, path):
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
