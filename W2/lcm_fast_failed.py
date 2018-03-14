# Uses python3

# This is not fast! exceed the time limit!
import sys

def lcm_fast(a, b):
    big = max(a, b)
    small = min(a, b)
    
    while True:
    	if big % small == 0:
    		break
    	else:
    		big += max(a, b)
    return big




if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))
