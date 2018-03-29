#Uses python3
import sys
import math
from heapq import *

def dist(x, y, i, j):
    return math.sqrt(((x[i] - x[j]) ** 2) + ((y[i] - y[j]) **2))

def minimum_distance(x, y):
    
    """
    Given n points on a plane, connect them with segments of minimum total length such that there is a path between any two points.
    n is the number of points
    x is the list of x-coordinate
    y is the list of y-coordinate
    Output the minimum total length of segments.    
    """
    # Prime's algorithm with priority queue
    n = len(x)
    result = 0.
    cost = [float('inf')] * n
    adj = [[] for _ in range(n)]
    weight = [[] for _ in range(n)]
    
    for i in range(n):
        adj[i] = [x for x in range(n) if x != i]
        weight[i] = [dist(x, y, i, j) for j in range(n) if j != i]
        
        
    connected = [False] * n
    priorityQ = [] # outside nodes (+ some repeated tree-nodes accessible to the outside nodes)

    cost[0] = 0
    heappush(priorityQ, (cost[0], 0))

    while priorityQ and sum(connected) <= n - 1:
        cost_u, u = heappop(priorityQ)
        if not connected[u]: # ignore tree-nodes (Note the difference from Dijstra's shortest path!!!)
            result += cost_u
            connected[u] = True            
            for i in range(n - 1):
                v = adj[u][i]                
                if not connected[v]:
                    weight_v = weight[u][i]                
                    if cost[v] > weight_v:
                        cost[v] = weight_v
                        heappush(priorityQ, (cost[v], v))
    
    return result




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
