# Uses python3
import sys

def get_fibonacci_huge_fast(n, m):
    # initialize a dictionary for the Pisano period for m
    p = {0: 0, 1: 1}
    # find the period
    i = 2
    while True:
        p[i] = (p[i - 1] + p[i - 2]) % m        
        # check if the 01 pattern appears
        if p[i] == 1 and p[i - 1] == 0:
            break
        i += 1
    length = len(p) - 2
    small_fib_index = n % length
    return p[small_fib_index]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))