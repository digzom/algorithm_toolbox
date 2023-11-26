n = int(input())

def fib_last_digit(n):
   a, b = 0, 1
   for _ in range(n):
       a, b = b, (a + b) % 1
   return a

str_n = str(fib_last_digit(n))
print(str_n[-1])
