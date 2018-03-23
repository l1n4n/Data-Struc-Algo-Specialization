#!/usr/bin/python3

import sys, threading
import math

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class TreeBST:
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


  def inOrderTravCountMax(self, i):
    """inordertravesal + remember the max value along the way. 
    If the next one is larger than current, update max; 
    if the next one is less than max, then incorrect"""
      
    if self.left[i] != - 1:
      self.inOrderTravCountMax(self.left[i])
    key = self.key[i]
    if key <= self.current_max:
      self.ans = False
      return
    else:
      self.current_max = key
    if self.right[i] != -1:
      self.inOrderTravCountMax(self.right[i])

  def IsBinarySearchTree(self):    
    if self.n == 0: # if depth is 0, tivially true
      return True
    self.ans = True
    self.current_max = -math.inf
    self.inOrderTravCountMax(0)
    return self.ans


def main():
  tree = TreeBST()
  tree.read()
  
  if tree.IsBinarySearchTree():
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
