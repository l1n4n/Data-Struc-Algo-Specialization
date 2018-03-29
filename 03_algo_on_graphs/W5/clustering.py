#Uses python3
import sys
import math

def dist(i, j):
    """to calculate the distance/weight between two nodes.
    x[i], y[i] are given as i's x-coordinate and y-coordinate
    x[j], y[j] are given as j's x-coordinate and y-coordinate
    """
    return math.sqrt(((x[i] - x[j]) ** 2) + ((y[i] - y[j]) **2))

class Node:
    """to record the x-coordinate, the y-coordinate, the parent, the rank"""
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.rank = 0

class Edge:
    """to record the starting, ending nodes, the weight"""
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = dist(u, v)        

def makeSetS(n):
    """make every point on the plane a node with itself as its parent, aka, a singleton disjoint set
    return a list of nodes
    """
    nodes = []
    for i in range(n):
        nd_i = Node(x[i], y[i], i)
        nodes.append(nd_i)
    return nodes

def makeEdgeS(n):
    """make every path between any two points an edge (to apply Kruskal’s algorithm)
    return a list of edges
    """
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append(Edge(i, j, dist(i, j)))
    return edges

def find(i, nodes):
    # path compression
    if i != nodes[i].parent:
        nodes[i].parent = find(nodes[i].parent, nodes)
    return nodes[i].parent

def union(u, v, nodes):
    # rank heuristic
    u_id = find(u, nodes)
    v_id = find(v, nodes)
    if u_id == v_id:
        return
    if nodes[u_id].rank > nodes[v_id].rank:
        nodes[v_id].parent = u_id
    else:
        nodes[u_id].parent = v_id 
    if nodes[u_id].rank == nodes[v_id].rank:
        nodes[v_id].rank += 1


def clustering(x, y, k):
    """
    Given n points on a plane and an integer k, 
    compute the largest possible value of d such that the given points can be partitioned into k non-empty subsets 
    in such a way that the distance between any two points from different subsets is at least d.
    Input: x is the list of x-coordinate of the points; y is the list of y-coordinate of the points, k is the no of maximal cluster
    Output the largest value of d.
    
    Use Kruskal’s algorithm for MST
    """
    #n = len(x)
    nodes = makeSetS(n)
    E = makeEdgeS(n)
    E = sorted(E, key=lambda edge: edge.weight)

    clusters = n # starting with n clusters (each point is a cluster), each time we do a union the no of clusters decreases by 1
    
    for edge in E:
        u = edge.u
        v = edge.v
        if find(u, nodes) != find(v, nodes):
            clusters -= 1
            union(u, v, nodes)
        if clusters < k: 
            return edge.weight
    
    return -1.


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
