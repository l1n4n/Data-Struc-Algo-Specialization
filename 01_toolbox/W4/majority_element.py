# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = (right - left) // 2 + left
    
    maj_left = get_majority_element(a, left, mid)
    maj_right = get_majority_element(a, mid, right)
    
    if maj_left == -1 and maj_right == -1:
        return -1 
    
    elif maj_left != -1 and maj_right == -1:
        no_left = a[left: right].count(maj_left)
        total = len(a[left: right])
        if no_left > total / 2:
            return maj_left
        else:
            return -1
        
    elif maj_right != -1 and maj_left == -1:
        no_right = a[left: right].count(maj_right)
        total = len(a[left: right])
        if no_right > total / 2:
            return maj_right
        else:
            return -1
        
    elif maj_right != -1 and maj_left != -1:
        no_left = a[left: right].count(maj_left)
        no_right = a[left: right].count(maj_right)
        total = len(a[left: right])
        if no_right > total / 2:
            return maj_right
        elif no_left > total / 2:
            return maj_left
        else:
            return -1       
        
        
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
