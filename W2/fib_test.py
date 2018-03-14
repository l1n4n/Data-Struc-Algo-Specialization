def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib(n):
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


def StressTest(N):
    while True:
        n = random.randint(2, N)
        print(n)
        result1 = calc_fib(n)
        result2 = calc_fib_fast(n)
        if result1 == result2:
            print('OK')
        else:
            print('wrong: ', result1, result2)
            break