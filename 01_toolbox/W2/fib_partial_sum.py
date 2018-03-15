# Uses python3
import sys

def fibonacci_partial_sum_fast(from_, to):
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
    period_sum = sum(list(p[i] for i in range(period))) % 10 # the sum is 280, modulo 10 = 0, so it is safe to omit the num of circle
    
    # x: how many circles, ind: the position of n in a circle
    x, indm = from_ // period, from_ % period
    
    y, indn = to // period, to % period 
    
    if indm < indn:
        ans = ((y - x) * period_sum + sum(list(p[i] for i in range(indm, indn + 1)))) % 10
    else:
        ans = ((y - x - 1) * period_sum + sum(list(p[i % 60] for i in range(indm, indn + 60 + 1)))) % 10
    
    
    return ans

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))