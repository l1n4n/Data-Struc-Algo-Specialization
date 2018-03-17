#Uses python3

import sys

def lcs3(a, b, c):
    """Compute the length of a longest common subsequence of three sequences.
    note: a simple extension of lcs2
    examples:
    >>> lcs3('123', '213', '135')
    2
    >>> lcs3('83217', '821387', '683147')
    3
    """
    x = len(a) + 1
    y = len(b) + 1
    z = len(c) + 1
    match_score = [[[0 for i in range(z)] for j in range(y)] for k in range(x)]
    for i in range(1, x):
        for j in range(1, y):
            for k in range(1, z):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    match_score[i][j][k] = match_score[i - 1][j - 1][k - 1] + 1
                else:
                    match_score[i][j][k] = max(match_score[i - 1][j][k], match_score[i][j - 1][k], match_score[i][j][k - 1])

    return match_score[-1][-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
