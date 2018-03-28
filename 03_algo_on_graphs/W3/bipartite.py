#Uses python3

import sys
#from collections import deque 
# use list is faster than deque

def bipartite(adj):
    """Given an undirected CONNECTED graph with n vertices and m edges, use bfs to check whether it is bipartite"""
    # if consider unconnected case, then have to add a visited arr. run bfs on vertex 0, mark every seen node as visited, if not found any 'triangle',
    # run bfs on the next UNvisited node, till every node is visited or a triangle is found.
    # However, as for the grader of this assignment, stackoverflow is likely to occur...    
    color = [None] * n
    color[0] = 1
    #q = deque([0])
    q = []
    q.append(0)
    while q:
        #u = q.popleft()
        u = q.pop(0)
        for w in adj[u]:            
            if color[w] == None:
                q.append(w)
                color[w] = -color[u]           
            elif color[w] == color[u]:
                return 0                
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
