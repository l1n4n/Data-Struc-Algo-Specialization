#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):    
    """Do V iterations of Bellman-Ford, save all nodes relaxed on Vth iteration to a queue `Q`
    Do BFS with `Q` and find all nodes reachable from `Q`"""

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

