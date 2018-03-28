#Uses python3

import sys
from heapq import *

def distance(adj, cost, s, t):
    """Dijkstra's shortest path with priority queue
    """
    
    conquered = [False] * n # n: number of vertices; mark True after being processed, i.e. poped out of the priorityQ
    dist = [float('inf')] * n
    dist[s] = 0 # the shortest distance from s to every vertices (represented as integers)
    priorityQ = [] # keep the to be processed vertices
    heappush(priorityQ, (dist[s], s))
    
    while priorityQ:
        dist_u, u = heappop(priorityQ) # pop the one with the lowest priority, aka, shortest path from the conquered to unconquered
        conquered[u] = True
        m = len(adj[u])
        for i in range(m):
            w = adj[u][i]
            if not conquered[w]:
                cost_uw = cost[u][i]
                if dist[w] > dist[u] + cost_uw:
                    dist[w] = dist[u] + cost_uw
                    # put u's newly relaxed kids in the queue, i.e. u's being conquered shortened the distance from the conquered to these kids           
                    heappush(priorityQ, (dist[w], w))

    if dist[t] == float('inf'):
        return - 1
    return dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
