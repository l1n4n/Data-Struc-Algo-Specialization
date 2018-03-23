# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    self.inOrderTraversal(0)    
    return self.result

  def inOrderTraversal(self, i):
    """left --> root --> right"""
    if self.left[i] != - 1:
        self.inOrderTraversal(self.left[i])
    self.result.append(self.key[i])
    if self.right[i] != -1:
        self.inOrderTraversal(self.right[i])

  def preOrder(self):
    self.result = []
    self.preOrderTraversal(0)
    return self.result
  
  def preOrderTraversal(self, i):
    """root --> left --> right"""
    self.result.append(self.key[i])
    if self.left[i] != -1:
        self.preOrderTraversal(self.left[i])
    if self.right[i] != -1:
        self.preOrderTraversal(self.right[i])    

  def postOrder(self):
    self.result = []
    self.postOrderTraversal(0)                
    return self.result
    
  def postOrderTraversal(self, i):
    """left --> right --> root"""
    if self.left[i] != -1:
        self.postOrderTraversal(self.left[i])
    if self.right[i] != -1:
        self.postOrderTraversal(self.right[i])
    self.result.append(self.key[i])

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
