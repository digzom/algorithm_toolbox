def euclidian_gcd(a, b):
    if b == 0:
        return a

    a_reminder = a % b 

    return euclidian_gcd(b, a_reminder)

gcd = euclidian_gcd(3918848080, 1653264)

print(gcd)
