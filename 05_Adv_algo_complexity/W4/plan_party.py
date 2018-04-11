#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []
        self.maxfun = 0


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent):
    # processing a tree using depth-first search
    for child in tree[vertex].children:
        if child != parent:
            dfs(tree, child, vertex)

    mx1 = tree[vertex].weight
    mx2 = 0
    for kid in tree[vertex].children:
        if kid != parent:
            mx2 += tree[kid].maxfun
            for grandkid in tree[kid].children:
                if grandkid != kid and grandkid != parent:
                    mx1 += tree[grandkid].maxfun

    tree[vertex].maxfun = max(mx1, mx2)


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    dfs(tree, 0, -1)    
    return tree[0].maxfun


def main():
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
