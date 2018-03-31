#!/usr/bin/python3

import sys
from heapq import *

"""
Bidirectional Dijkstra
03/30/2018 record: (Max time used: 55.02/150.00, max memory used: 719790080/2147483648.)
"""


from heapq import *
class BiDij:
    def __init__(self, n):
        self.n = n;                             # Number of nodes
        self.inf = n*10**6                      # All distances in the graph are smaller
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.popped_out = [False]*n                # popped_out[v] == True iff v was popped_out, i.e. popped out from the queue, by forward or backward search
        self.workset = set()                       # All the nodes visited, put into the queue, by forward or backward search, the point consists the shortest path is definitely in

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query.
        """
        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
            self.popped_out[v] = False;
        self.workset.clear()  


    
    def shortestPath(self):
        """After meeting-in-the-middle process
        find the real shortest path among all the visited points by either forward search or backward search
        """
        length = self.inf
        
        for u in self.workset:
            if self.d[0][u] + self.d[1][u] < length:
                length = self.d[0][u] + self.d[1][u] # iterate to find the best
        if length == self.inf:
            return - 1 # no path between s and t
        return length

    
    def query(self, adj, cost, s, t):
        """given an adjacency list repre of graph with cost
        calculate the shortest path between s and t
        output -1 if there is no path"""
        self.clear()                
 
        q = [[], []]
        # bidirectional Dijkstra
        self.visit(q, 0, s, 0) # begin forward search
        self.visit(q, 1, t, 0) # begin backward search
        
        while q[0] and q[1]:
            """extract min from forward queue and backward queue in turn"""
            for side in [0, 1]:
                u = self.extract_min(q, side)
                self.Process(u, q, side, adj[side], cost[side])
                if self.popped_out[u]:
                    return self.shortestPath()
                self.popped_out[u] = True
        """if one queue is empty before meeting, then no path between s and t"""
        return -1 
        #print('{} --> {} is {}'.format(s, t, self.shortestPath(s, t, distance, distance_r)))
    
    def extract_min(self, q, side):            
        _, u = heappop(q[side]) # python's built-in priority queue
        return u    

    
    def Process(self, u, q, side, adj, cost):
        """relax u's every neighbor""" 
        for v, w in zip(adj[u], cost[u]): 
            self.visit(q, side, v, self.d[side][u] + w)
        
        
            
    def visit(self, q, side, v, dist):
        """to relax the distance to node v from direction side by value dist.
        add v to the workset for after-meeting searching
        """
        if self.d[side][v] > dist:
            self.d[side][v] = dist
            heappush(q[side], (self.d[side][v], v))            
            self.workset.add(v)

def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s-1, t-1))
