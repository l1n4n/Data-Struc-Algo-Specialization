# python3

import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))


def poly_hash(s, prime, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % prime 
    return ans

def precompute_hashes(text, p_len, p, x):
    H = [0] * (len(text) - p_len + 1)
    s = text[-p_len:] # the last possible match
    H[len(text)-p_len] = poly_hash(s, p, x)
    y = 1
    for i in range(1, p_len + 1):
        y = (y * x) % p # avoid using  y = x ** p_len to speed up the calculation
    for i in reversed(range(len(text) - p_len)):        
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + p_len])) % p # H[len(text) - p_len] has been calclulated, so we use it to calculate the former
    return H

def get_occurrences(pattern, text):
    """Rabin–Karp’s algorithm for searching the given pattern in the given text
    with precomputed hash values of the candidate substrings to improve running time
    """
    p = 1000000007 # a big prime
    x = random.randint(1, p)
    t_len = len(text)
    p_len = len(pattern)
    phash = poly_hash(pattern, p, x)
    H = precompute_hashes(text, p_len, p, x)
    return [
        i 
        for i in range(t_len - p_len + 1) 
        if phash == H[i] and text[i:i + p_len] == pattern
    ]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


