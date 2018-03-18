# Uses python3
import sys
import itertools

def partition3(A):
    """A is a list of integers.
    Output 1, if it possible to partition the numbers in A into three subsets with equal sums, and 0 otherwise.
    >>> partition3([3, 3, 3, 3])
    0
    >>> partition3([40])
    0
    >>> partition3([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59])
    1
    >>> partition3([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25])
    1
    """
    total = sum(A)
    if total % 3 != 0:
        return 0
    capacity = total // 3
    A.sort()
    N = len(A) + 1
    M = [[[0 for z in range(N)] for y in range(capacity + 1)] for x in range(capacity + 1)]
    
    for z in range(N):
        M[0][0][z] = 1
    
    for x in range(0, capacity + 1):
    
        for y in range(0, capacity + 1):
        
            for z in range(1, N):
                
                val = A[z - 1]
                
                if M[x][y][z - 1] == 1:
                    M[x][y][z] = 1
                    if x + val <= capacity:
                        M[x + val][y][z] = 1
                    if y + val <= capacity:
                        M[x][y + val][z] = 1

    return M[-1][-1][-1]


    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

