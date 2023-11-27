def fib_last_digit(n):
   a, b = 0, 1
   for _ in range(n):
       a, b = b, (a + b) % 10
   return a

n = int(input())
print(fib_last_digit(n))
