# Uses python3
import sys

def optimal_weight(W, w):
    """Knapsack w/o repetitions problem: given n gold bars, find the maximum weight of gold that fits into a bag of capacity W.
    w is a list with n elements defining the weights of the bars of gold.
    examples:
    >>> optimal_weight(10, [1, 4, 8])
    9
    """
    value_matrix = [[0 for w in range(W + 1)] for i in range (n + 1)]
    w = [0] + w # to conveniently refer to the ith bar's weight
    for i in range(1, n + 1):
        for c in range(1, W + 1):
            value_matrix[i][c] = value_matrix[i - 1][c]
            w_i = w[i]
            if w_i <= c:
                val = value_matrix[i - 1][c - w_i] + w_i
                if value_matrix[i][c] < val:
                    value_matrix[i][c] = val
    return value_matrix[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
