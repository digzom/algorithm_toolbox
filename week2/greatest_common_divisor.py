# for integers, a and b, their greatest common divisor or gcd(a, b) is the largest 
# integer d so that d divides a and b.

best = 0
a = 3918848
b = 1653264

for d in range(1, a + b):
    if a % d == 0 and b % d == 0:
        best = d


print(best)
