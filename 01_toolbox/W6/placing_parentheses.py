# Uses python3
import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def minMax(i, j, ops, M, m):
    """get the min and the max value of any sub-expression from S[i] to S[j] (including S[j])
    """
    mn = math.inf
    mx = - math.inf
    for k in range(i, j):
        op = ops[k]
        a = evalt(M[i][k], M[k + 1][j], op)
        b = evalt(M[i][k], m[k + 1][j], op)
        c = evalt(m[i][k], M[k + 1][j], op)
        d = evalt(m[i][k], m[k + 1][j], op)
        mn = min(mn, a, b, c, d)
        mx = max(mx, a, b, c, d)
    return mn, mx


def get_maximum_value(dataset):
    """Find the maximum value of an arithmetic expression 
    by specifying the order of applying its arithmetic operations using additional parentheses.
    Input: A string S of length 2n + 1
    Each symbol at an even position of S is a digit (that is, an integer from 0 to 9).
    Each symbol at an odd position is one of three operations from {+,-,*}.
    Examples:
    >>> get_maximum_value('1+5')
    6
    >>> get_maximum_value('5-8+7*4-8+9')
    200
    """
    N = len(dataset)
    digits = [int(dataset[i]) for i in range(0, N, 2)]
    ops = [dataset[i + 1] for i in range(0, N - 1, 2)]
    # create two empty matrices
    n = len(digits)
    M = [[0] * n for i in range(n)]
    m = [[0] * n for i in range(n)]
    # initialize base cases (j-i==0)
    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]
    # fill in the matrices
    for s in range(1, n):
        for i in range(n - s):
            j = i + s # the difference in length between j and i is s
            mn, mx = minMax(i, j, ops, M, m)
            m[i][j] = mn
            M[i][j] = mx

    return M[0][n - 1] # the right corner of the Max matrix


if __name__ == "__main__":
    print(get_maximum_value(input()))
