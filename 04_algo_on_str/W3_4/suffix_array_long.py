# python3
import sys


def build_suffix_array(s):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    BuildSuffixArray(S)
    order ← SortCharacters(S)
    class ← ComputeCharClasses(S, order)
    L ← 1
    while L < |S|:
        order ← SortDoubled(S, L, order, class)
        class ← UpdateClasses(order, class, L)
        L ← 2L
    return order    
    """
    n = len(s)
    order = sort_char(s)
    cl = compute_char_classes(s, order)
    l = 1
    while l < n:
        order = sort_doubles(s, l, order, cl)
        cl = update_classes(order, cl, l)
        l *= 2
    return order

def update_classes(new_order, cl, l):
    """given the renewed order of the doubled suffix, compute the new buckets
    UpdateClasses(newOrder, class, L)
    n ← |newOrder|
    newClass ← array of size n
    newClass[newOrder[0]] ← 0
    for i from 1 to n − 1:
        cur ← newOrder[i], prev ← newOrder[i − 1]
        mid ← (cur + L)(mod n), midPrev ← (prev + L)(mod n)
        if class[cur] ̸= class[prev] or class[mid] ̸= class[midPrev]:
            newClass[cur] ← newClass[prev] + 1
        else:
            newClass[cur] ← newClass[prev]
    return newClass

    """
    n = len(new_order)
    new_cl = [None] * n
    new_cl[new_order[0]] = 0
    for i in range(1, n):
        cur, prev = new_order[i], new_order[i - 1]
        mid, mid_prev = (cur + l) % n, (prev + l) % n # in case idx out of range n
        if cl[cur] != cl[prev] or cl[mid] != cl[mid_prev]:
            new_cl[cur] = new_cl[prev] + 1
        else:
            new_cl[cur] = new_cl[prev]
    return new_cl


def sort_doubles(s, l, order, cl):
    """given the order of the l-length suffix of s, compute the order of the doubled-l-length suffix

    SortDoubled(S, L, order, class)
    position ← zero array of size |S|
    newOrder ← array of size |S|
    for i from 0 to |S| − 1:
    position[class[i]] ← position[class[i]] + 1
    for j from 1 to |S| − 1:
         position[j] ← position[j] + position[j − 1]
    for i from |S| − 1 down to 0:
        start ← (order[i] − L + |S|) mod |S|
        cl ← class[start]
        position[cl] ← position[cl] − 1
        newOrder[position[cl]] ← start
    return newOrder
    """
    n = len(s)
    position = [0] * n
    new_order = [None] * n
    for i in range(n):
        position[cl[i]] = position[cl[i]] + 1 # initialize the number of every cl as 1
    for j in range(1, n):
        position[j] = position[j] + position[j - 1] # count the occurances
    for i in range(n-1, -1, -1):
        start = (order[i] - l + n) % n # shift the suffix by length L counter_clockwise, so that we can sort the doubled suffix by its second half
        c_start = cl[start] # count sort the first half
        position[c_start] = position[c_start] - 1 
        new_order[position[c_start]] = start
    return new_order



def compute_char_classes(s, order):
    """ compute equivalant classes(buckets) of the characters in string s
    ComputeCharClasses(S, order)
    class ← array of size |S|
    class[order[0]] ← 0
    for i from 1 to |S| − 1:
        if S[order[i]] ̸= S[order[i − 1]]:
            class[order[i]] = class[order[i − 1]] + 1
        else:
            class[order[i]] = class[order[i − 1]]
    return class
    """
    n = len(s)
    cl = [None] * n
    cl[order[0]] = 0
    for i in range(1, n):
        if ord(s[order[i]]) != ord(s[order[i - 1]]):
            cl[order[i]] = cl[order[i - 1]] + 1
        else:
            cl[order[i]] = cl[order[i - 1]]
    return cl

def sort_char(s):
    """count sort by character's integer code
    Output: list of index sorted by s[index]'s integer code
    >>> sort_char('bca')
    [2, 0, 1]

    SortCharacters(S)
    order ← array of size |S|
    position ← zero array of size |Σ|
    for i from 0 to |S| − 1:
        position[S[i]] ← position[S[i]] + 1
    for j from 1 to |Σ| − 1:
        position[j] ← position[j] + position[j − 1]
    for i from |S| − 1 down to 0:
        c ← S[i]
        position[c] ← position[c] − 1
        order[position[c]] ← i
    return order"""
    n = len(s)
    order = [None] * n
    position = [0] * 256
    for i in range(n):
        position[ord(s[i])] = position[ord(s[i])] + 1
    for j in range(256):
        position[j] = position[j] + position[j - 1]
    for i in range(n-1, -1, -1):
        c = ord(s[i])
        position[c] = position[c] - 1
        order[position[c]] = i
    return order





if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
