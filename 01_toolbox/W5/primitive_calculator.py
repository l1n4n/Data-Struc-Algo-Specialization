# Uses python3
import sys

from collections import defaultdict
def optimal_sequence(n):
    """n is an integer ranging from 1 to 10**6
    operations with the current number x:
    * multiply x by 2
    * multiply x by 3
    * add 1 to x
    Output: the minimum number k of operations needed to get n from 1 & a sequence of intermediate numbers

    >>> list(optimal_sequence(1))
    [1]
    >>> list(optimal_sequence(145))
    [1, 3, 9, 18, 36, 72, 144, 145]
    >>> list(optimal_sequence(14512))
    [1, 3, 9, 10, 11, 33, 66, 67, 201, 402, 403, 1209, 3627, 3628, 7256, 14512]
    """
    num_dict = {}
    num_dict[0] = 0
    num_dict[1] = 0
    #precedents_dict = defaultdict(list)
    precedents_dict = {}
    precedents_dict[1] = [1]
    
    for i in range(2, n + 1):
        #print(precedents_dict)
        
        precedent1 = i - 1
        try1 = num_dict[precedent1] + 1        
        
        precedent3, remainder3 = i // 3, i % 3
        try3 = num_dict[precedent3] + remainder3 + 1
        
        precedent2, remainder2 = i // 2, i % 2
        try2 = num_dict[precedent2] + remainder2 + 1
        
        best = try1
        precedent = precedent1
        remainder = 0
        
        if try2 < best:
            #print(i, precedent)
            best = try2
            precedent = precedent2
            remainder = remainder2

            
        elif try3 < best:
            best = try3
            precedent = precedent3
            remainder = remainder3
 
          
        num_dict[i] = best
        precedents_dict[i] = precedents_dict[precedent][:]
        for x in range(remainder, -1, -1):
            precedents_dict[i].append(i - x)
            
    return precedents_dict[n]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
