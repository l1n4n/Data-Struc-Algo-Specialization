# Uses python3
import sys

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     #write your code here
#     return number_of_inversions

def get_number_of_inversions(a):
    sort_a, count = merge_count(a)
    return count

def merge_count(arr):

    if len(arr) <= 1:        
        return arr, 0
    else:
        cut = len(arr)//2
        left = arr[:cut]
        right = arr[cut:]
        left_sorted, l = merge_count(left)
        right_sorted, r = merge_count(right)
        # inductive step
        current = 0
        i = 0
        j = 0
        result = []
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] <= right_sorted[j]:                
                result.append(left_sorted[i])
                i += 1
            else:                
                result.append(right_sorted[j])
                j += 1
                current += len(left_sorted) - i
        while i < len(left_sorted):
            result.append(left_sorted[i])
            i += 1
        while j < len(right_sorted):
            result.append(right_sorted[j])
            j += 1
        
        return result, current + l + r

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a))
