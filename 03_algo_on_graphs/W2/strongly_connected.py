#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs_order(adj, v, visited, stack):
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            dfs_order(adj, w, visited, stack)
    stack.append(v)

def reverse(adj):
    rev_adj = [[] for _ in range(n)]
    for v in range(n):
        for w in adj[v]:
            rev_adj[w].append(v)
    return rev_adj

def dfs_scc(adj, v, visited):
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            dfs_scc(adj, w, visited)    


def number_of_strongly_connected_components(adj):
    # first run dfs on the original and get postorder
    visited = [False] * n
    stack = []
    for v in range(n):
        if not visited[v]:
            dfs_order(adj, v, visited, stack)

    # get reversed graph
    re = reverse(adj)

    # run dfs on the reversed graph
    visited = [False] * n
    result = 0
    while stack:
        v = stack.pop()
        if not visited[v]:
            dfs_scc(re, v, visited)
            result += 1
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
