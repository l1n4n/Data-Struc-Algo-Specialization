# python3
import sys

def BWT(text):
    """Construct the Burrows–Wheeler transform of a string.
    Input: A string Text ending with a “$” symbol
    >>> BWT('AA$')
    'AA$'
    >>> BWT('ACACACAC$')
    'CCCC$AAAA'
    """
    n = len(text)
    Matrix = [text[i:] + text[:i] for i in range(n)]
    Matrix.sort()    
    return ''.join([row[-1] for row in Matrix])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))