# Uses python3
def edit_distance(s, t):
    """    Edit distance between two strings s and t.
    The edit distance between two strings is the minimum number of insertions,
    deletions, and mismatches in an alignment of two strings.
    Samples:
    >>> edit_distance("ab", "ab")
    0
    >>> edit_distance("short", "ports")
    3
    >>> # Explanation: s h o r t −
    >>> #              − p o r t s
    >>> edit_distance("editing", "distance")
    5
    >>> # Explanation: e d i − t i n g −
    >>> #              − d i s t a n c e
    """
    n = len(s) + 1
    m = len(t) + 1
    dis_matrix = [[x] + [0] * (m - 1) for x in range(n)]
    dis_matrix[0] = [x for x in range(m)]
    for i in range(1, n):
        for j in range(1, m):
            insert = dis_matrix[i - 1][j] + 1
            delete = dis_matrix[i][j - 1] + 1
            replace = dis_matrix[i - 1][j - 1] + 1
            match = dis_matrix[i - 1][j - 1]
            if s[i - 1] == t[j - 1]:
                dis_matrix[i][j] = min(insert, delete, match)
            else:
                dis_matrix[i][j] = min(insert, delete, replace)

    return dis_matrix[- 1][- 1]



if __name__ == "__main__":
    print(edit_distance(input(), input()))
