# python3
import sys
from itertools import chain, islice


def build_suffix_array(A):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    http://web.stanford.edu/class/cs97si/suffix-array.pdf
    n ← length(A)
    for i ← 0, n – 1
        P(0, i) ← position of Ai in the ordered array of A‘s characters
    cnt ← 1
    for k ← 1, [log2n] (ceil)
        for i ← 0, n – 1
            L(i) ← (P(k – 1, i) , P(k – 1, i + cnt) , i)
        sort L
        compute P(k, i) , i = 0, n - 1
        cnt ← 2 * cnt
    """
    L = sorted((a, i) for i, a in enumerate(A))
    n = len(A)
    count = 1
    
    while count < n:
        P = [0] * n
        for (r, i), (s, j) in zip(L, islice(L, 1, None)):
            P[j] = P[i] + (r != s)

        L = sorted(chain((((P[i],  P[i+count]), i) for i in range(n - count)),
                         (((P[i], -1), i) for i in range(n - count, n))))
        count *= 2
    return [i for _, i in L]
    

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
