# python3
import sys

def InverseBWT(bwt):
    """Reconstruct a string from its Burrows–Wheeler transform.
    Input Format. A string Transform with a single “$” sign, 
    except for the last symbol, Text contains symbols A, C, G, T only.
    >>> InverseBWT('AC$A')
    'ACA$'
    >>> InverseBWT('AGGGAA$')
    'GAGAGA$'    
    """
    # count the last column + index of each letter
    counter = [0] * 5 # $, A, C, G, T
    last_column = []
    for letter in bwt:
        if letter == '$':
            last_column.append(('$', counter[0]))
            counter[0] += 1
        elif letter == 'A':
            last_column.append(('A', counter[1]))
            counter[1] += 1
        elif letter == 'C':
            last_column.append(('C', counter[2]))
            counter[2] += 1
        elif letter == 'G':
            last_column.append(('G', counter[3]))
            counter[3] += 1
        elif letter == 'T':
            last_column.append(('T', counter[4]))
            counter[4] += 1
        else:
            raise ValueError
    first_column = sorted(last_column)
    n = len(bwt)
    hash_first_last = {first_column[i]: last_column[i] for i in range(n)}
    reversed_result = ['$']
    next_key = ('$', 0)
    for i in range(1, n):
        letter, key = hash_first_last[next_key][0], hash_first_last[next_key]
        reversed_result.append(letter)
        next_key =  key
    result = reversed_result[::-1]
    return ''.join(letter for letter in result)


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))