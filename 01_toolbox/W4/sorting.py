# Uses python3
import sys
import random

def partition3(a, l, r):
    """3-way quick sort: partition the arr into three parts, left is less than the pivot, middle is equal to the pivot,
    right is greater than the pivot
    
    """
    pivot = a[l]
    lt = l
    gt = r
    i = l + 1
    while i <= gt:
        if a[i] < pivot:
            a[i], a[lt] = a[lt], a[i]
            i += 1
            lt += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
    #print(lt, gt)
    return lt, gt
    
    

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    #m = partition2(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    s, e = partition3(a, l, r)
    #m = partition2(a, l, r)
    randomized_quick_sort(a, l, s - 1);
    randomized_quick_sort(a, e + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
