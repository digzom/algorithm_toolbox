n = input().split()

best = 0

a = int(n[0])
b = int(n[1])

for d in range(1, a + b):
    if a % d == 0 and b % d == 0:
        best = d


print(best)
