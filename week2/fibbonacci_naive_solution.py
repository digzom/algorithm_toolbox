def fibonacci(n):
    if n <= 1:
        return n
    else:
        fibonacci(n - 1) + fibonacci(n - 2)


n_number = fibonacci(10)

print(n_number)

# have to do it in a more optimized way
