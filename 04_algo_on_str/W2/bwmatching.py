# python3
import sys

def fill_counts_matrix(bwt):
    N = len(bwt)
    Matrix = [[None] * (N + 1) for i in range(5)] # except for the one $ symbol, BWT(Text) contains symbols A, C, G, T only
    symbols = ['$', 'A', 'C', 'G', 'T']
    for i in range(5):
        Matrix[i][0] = 0

    for i in range(1, N + 1):
        symbol = bwt[i - 1]        
        for j in range(5):
            Matrix[j][i] = Matrix[j][i - 1] if symbol != symbols[j] else Matrix[j][i - 1] + 1
       
    return Matrix



def PreprocessBWT(bwt):
    """
    Preprocess the Burrows-Wheeler Transform bwt of some text
    and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
    """    
    occ_counts_before = fill_counts_matrix(bwt)
    totals = [occ_counts_before[i][-1] for i in range(5)]
    starts = {}
    starts['$'] = 0
    starts['A'] = 1 if occ_counts_before[1][-1] != 0 else None
    starts['C'] = sum(totals[:2]) if occ_counts_before[2][-1] != 0 else None
    starts['G'] = sum(totals[:3]) if occ_counts_before[3][-1] != 0 else None
    starts['T'] = sum(totals[:4]) if occ_counts_before[4][-1] != 0 else None
    
    return starts, occ_counts_before 


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
    """
    Compute the number of occurrences of string pattern in the text
    given only Burrows-Wheeler Transform bwt of the text and additional
    information we get from the preprocessing stage - starts and occ_counts_before.

    """
    N = len(bwt)
    Pattern = list(pattern)
    symbols = ['$', 'A', 'C', 'G', 'T']

    top = 0
    bottom = N - 1
    while top <= bottom:
        if Pattern:
            symbol = Pattern.pop()
            sym_idx = symbols.index(symbol)
            if symbol in bwt[top: bottom + 1]:
                top = starts[symbol] + occ_counts_before[sym_idx][top]
                bottom = starts[symbol] + occ_counts_before[sym_idx][bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    # Preprocess the BWT once to get starts and occ_count_before.
    # For each pattern, we will then use these precomputed values and
    # spend only O(|pattern|) to find all occurrences of the pattern
    # in the text instead of O(|pattern| + |text|).  
    starts, occ_counts_before = PreprocessBWT(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
