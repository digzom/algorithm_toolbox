n = int(input())

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n_number = fibonacci(n)

print(n_number)
