import sys

sys.set_int_max_str_digits(100)

n = int(input())

def fib(n):
   a, b = 0, 1
   for _ in range(n):
       a, b = b, a + b
   return a

print(fib(n))
