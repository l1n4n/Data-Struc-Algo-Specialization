# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.depth = [0] * self.n
        

        def node_depth(self, node):
            # calculate the depth of each node        
            par_node = self.parent[node]
            if par_node == -1:
                return 1
            if self.depth[node] != 0: # if this node has been calculated, then do not re-calculate
                return self.depth[node]
            depth = self.node_depth(par_node) + 1 #if it has not been calculated, then do the calculation
            return depth      
              
                
        def compute_height(self):
            for i in range(self.n):
                self.depth[i] = self.node_depth(i)                
            return max(self.depth)

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
