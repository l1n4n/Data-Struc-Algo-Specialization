# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

n = len(a)
if a[0] < a[1]:
    a[0], a[1] = a[1], a[0]
for i in range(2, n):
    if a[i] >= a[0]:
        a[0], a[1] = a[1], a[0]
        a[0], a[i] = a[i], a[0]
    elif a[1] < a[i] < a[0]:
        a[1], a[i] = a[i], a[0]
print(a[0] * a[1])

