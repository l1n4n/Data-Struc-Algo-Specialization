#Uses python3

import sys

def negative_cycle(adj, cost):
    """Bellman-Ford algorithm to detect any negative cycle
    """
    dist = [0] * n # initialize all distance to 0 to handle disconnected graphs   
    for i in range(n): # v times iteration to relax ALL the egdes
        for v in range(n):
            m = len(adj[v])
            for j in range(m):
                u = adj[v][j]
                weight_vu = cost[v][j]
                if dist[u] > dist[v] + weight_vu:
                    dist[u] = dist[v] + weight_vu 
                    if i == n - 1: #if updating happens during the nth iteration
                        return 1
    return 0

    

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
    print(negative_cycle(adj, cost))

