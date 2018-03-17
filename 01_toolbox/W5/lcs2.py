#Uses python3

import sys

def lcs2(a, b):
    """Compute the length of a longest common subsequence of two sequences
    Samples:
    >>> lcs2("275", "25")
    2
    >>> lcs2("7", "1234")
    0
    >>> lcs2("2783", "5287")
    2
    >>> lcs2("123", "321")
    1"""
    n = len(a) + 1
    m = len(b) + 1
    match_score = [[0] * m for i in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if a[i - 1] == b[j - 1]:
                match_score[i][j] = match_score[i - 1][j - 1] + 1
            else:
                match_score[i][j] = max(match_score[i][j - 1], match_score[i - 1][j])

    return match_score[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
