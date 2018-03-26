#Uses python3

import sys



def Explore(v, visited, counter):
    visited[v] = counter   
    for w in adj[v]:
        if not visited[w]:
            Explore(w, visited, counter)      
    
def number_of_components(adj):
    visited = [0] * n
    counter = 1
    for x in range(n):
        if not visited[x]:
            Explore(x, visited, counter)
            counter += 1
    #print(visited, counter)
    return counter - 1

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
    print(number_of_components(adj))
