def maxPairNaive(a):
    result = 0
    n = len(a)
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    return result

def maxPairFast(a):

    n = len(a)
    if a[0] < a[1]:
        a[0], a[1] = a[1], a[0]
    for i in range(2, n):
        if a[i] >= a[0]:
            a[0], a[1] = a[1], a[0]
            a[0], a[i] = a[i], a[0]
        elif a[1] < a[i] < a[0]:
            a[1], a[i] = a[i], a[0]
    return a[0] * a[1]

import random
random.seed(1234)
def StressTest(N, M):
    while True:
        n = random.randint(2, N)
        A = []
        for i in range(n):
            A.append(random.randint(0, M))
        print(A)
        result1 = maxPairNaive(A)
        result2 = maxPairFast(A)
        if result1 == result2:
            print('OK')
        else:
            print('wrong: ', result1, result2)
            break