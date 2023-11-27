initial_input = input().split()

best = 0

n = int(initial_input[0])
mod_a = int(initial_input[1])

def fib(n):
    a, b = 0, 1
   
    for _ in range(n):
        a, b = b, (a + b) % mod_a
    return a

print(fib(n))
