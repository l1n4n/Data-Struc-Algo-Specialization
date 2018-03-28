#Uses python3

import sys
from collections import deque

def distance(adj, s, t):
    """Given an undirected graph with n vertices and m edges and two vertices u and v, 
    compute the length of a shortest path between u and v, -1 if there is no path.
    Input: ajacency list representation
    """
    dist = [-1] * n
    dist[s] = 0
    process_queue = deque([s])
    while process_queue:
        v = process_queue.popleft()
        for w in adj[v]:
            if dist[w] == - 1:
                process_queue.append(w)
                dist[w] = dist[v] + 1

    return dist[t]

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
