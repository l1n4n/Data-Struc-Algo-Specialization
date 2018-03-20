# python3

import sys

class tableMerger:

    def __init__(self, n, lines):
        self.n = n
        self.lines = lines
        self.rank = [1] * n
        self.parent = list(range(0, n))
        self.maxline = max(self.lines)
        

    def getParent(self, table):
        # find parent and compress path
        if table != self.parent[table]:
            self.parent[table] = self.getParent(self.parent[table])

        return self.parent[table]

    def merge(self, destination, source):
        realDestination, realSource = self.getParent(destination), self.getParent(source)

        if realDestination == realSource:
            return False

        # merge two components
        # use union by rank heuristic 
        # update ans with the new maximum table size
        if self.rank[realDestination] < self.rank[realSource]:
            self.parent[realDestination] = realSource
            self.lines[realSource] +=  self.lines[realDestination]
            self.maxline = max(self.maxline, self.lines[realSource])
        else:
            self.parent[realSource] = realDestination
            self.lines[realDestination] += self.lines[realSource]
            self.maxline = max(self.maxline, self.lines[realDestination])
            if self.rank[realDestination] == self.rank[realSource]:
                self.rank[realDestination] += 1

        return True

    
n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))

tm = tableMerger(n, lines)
for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    tm.merge(destination - 1, source - 1)
    print(tm.maxline)
        
