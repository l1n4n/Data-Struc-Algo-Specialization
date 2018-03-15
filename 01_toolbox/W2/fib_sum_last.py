# Uses python3
import sys

def fibonacci_sum_fast(n):

    # initialize a dictionary for the Pisano period for m
    p = {0: 0, 1: 1}
    # find the period
    i = 2
    while True:
        p[i] = (p[i - 1] + p[i - 2]) % 10        
        # check if the 01 pattern appears
        if p[i] == 1 and p[i - 1] == 0:
            break
        i += 1
    
    period = len(p) - 2
    period_sum = sum(list(p[i] for i in range(period))) % 10
    
    # x: how many circles, ind: the position of n in a circle
    x, ind = n // period, n % period
    return (x * period_sum + sum(list(p[i] for i in range(ind + 1)))) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))
