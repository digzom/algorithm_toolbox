n = int(input())

def fib(n):
    return do_fib(0, 1, n)


def do_fib(a, b, n):
    if n > 0:
        return do_fib(b, a + b, n - 1)
    else:
        return a

print(fib(n))

