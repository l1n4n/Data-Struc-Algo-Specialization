#Uses python3

import sys

def largest_number(a):
    """ a: list of str, eg, ['89', '83', '8']
    """
    res = ""
    while a:
        current_max = a[0]
        for i in a[1:]:
            if i * len(current_max) > current_max * len(i):
                current_max = i
        a.remove(current_max)
        res += current_max
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
