# Uses python3
import sys

def get_change(m):
        
    A = 0
    x, r1 = m // 10, m % 10
    A += x
    m = r1
    y, r2 = m // 5, m % 5
    A += y
    m = r2
    A += m
    return A

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
