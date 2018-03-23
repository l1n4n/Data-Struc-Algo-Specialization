#!/usr/bin/python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


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
        self.INT_MAX = 4294967296
        self.INT_MIN = -4294967296
        
    def isBSTnode(self, node, low, high):
        if node == - 1: # base case
            return True
        if self.key[node] < low or self.key[node] > high: # check if the node violates BST property
            return False
        # recursively check the left child and the right child
        # the left child's upperbound is its parent's key - 1 & the right child's lower bound is its parent's key
        return self.isBSTnode(self.left[node], low, self.key[node] - 1) and self.isBSTnode(self.right[node], self.key[node], high)
    
            
    def IsBinarySearchTree(self):
        if self.n == 0: # An empty tree is trivially a BST.
            return True
        return self.isBSTnode(0, self.INT_MIN, self.INT_MAX)


def main():
    tree = TreeBST()
    tree.read()

    if tree.IsBinarySearchTree():
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
