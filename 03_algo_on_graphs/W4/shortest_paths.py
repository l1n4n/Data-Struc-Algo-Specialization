#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #during |V|'th iteration of Bellman-Ford algorithm 
    #not all nodes, that reachable from negative cycle will be relaxed, but just some of them. 
    #After that you need to find the cycle and explore all reachable nodes from it.
    #every vertex reachable from a negative cycle needs to be marked "-" as there is a path to the node of -Inf length
    # making use of the negative cycle. In the lecture, the lecturer suggested 
    # running a BFS starting with all the vertexes listed in D to ensure all vertexes of path length -Inf were found.
    """Do V iterations of Bellman-Ford, save all nodes relaxed on Vth iteration to a queue `Q`
    Do BFS with `Q` and find all nodes reachable from `Q`
    All those nodes and only those can have infinite distance from `s`"""
    """Well, I believe that you are quite right. :) 
    If the vertex is reachable from NC you can make it's distance to be -infinity. 
    Let's denote those as F. Run DFS from S to figure the vertices reachable from S. 
    Those reachable from S and not in F is what you need."""




    # bf algorithm to detect neg cycles
    distance[s] = 0
    reachable[s] = 1
    shortest[s] = 1
    q = []  
    for i in range(n): # v times iteration to relax ALL the egdes
        for v in range(n):
            m = len(adj[v])
            for j in range(m):
                u = adj[v][j]
                weight_vu = cost[v][j]
                if reachable[v] == 1:
                    #print(u)
                    reachable[u] = 1 
                    if distance[u] == 10**19 or distance[u] > distance[v] + weight_vu:
                        distance[u] = distance[v] + weight_vu                    
                        if i == n - 1: #if updating happens during the nth iteration
                            q.append(u)
    
    """visited(Q.first) = true
    while Q not empty:
        u <- Q.deQueue()
        shortest[u] = 0 // there is no shortest path from `s` to `u`
        for all (u, v) in E:
            if not visited(v):
                visited(v) = true
                Q.push(v)"""
    # bfs to find all vertices reachable from a negetive cycle
    
    distance[s] = 0 # in case s is part of negative cycle

    
    seen = [False] * n
    while q:
        #print(q)
        u = q.pop(0)
        seen[u] = True                    
        shortest[u] = 0
        for w in adj[u]:
            if not seen[w]:
                q.append(w)
    #print(distance)



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

