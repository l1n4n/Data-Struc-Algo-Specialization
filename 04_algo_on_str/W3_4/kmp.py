# python3
import sys

def compute_prefix_func(pattern):
    length = len(pattern)
    s = [0] * length
    s[0] = 0
    border = 0
    for i in range(1, length):
        while border > 0 and pattern[i] != pattern[border]:
            border = s[border - 1]
        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s

def find_pattern(pattern, text):
    """
    KMP (knuth_morris_pratt) algorithm to find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    result = []
    concat = pattern + '$' + text
    len_p = len(pattern)
    s = compute_prefix_func(concat)
    len_c = len(concat)
    for i in range(len_p + 1, len_c):
        if s[i] == len_p:
            result.append(i - 2 * len_p)
    return result

    


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))

