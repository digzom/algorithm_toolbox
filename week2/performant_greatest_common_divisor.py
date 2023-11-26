n = input().split()

a = int(n[0])
b = int(n[1])

def euclidian_gcd(a, b):
    if b == 0:
        return a

    a_reminder = a % b 

    return euclidian_gcd(b, a_reminder)

gcd = euclidian_gcd(a, b)

print(gcd)

