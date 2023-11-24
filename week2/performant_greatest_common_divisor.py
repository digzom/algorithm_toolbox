import time

def euclidian_gcd(a, b):
    if b == 0:
        return a

    a_reminder = a % b 

    return euclidian_gcd(b, a_reminder)

start_time = time.time()
gcd = euclidian_gcd(3918848080, 1653264)
end_time = time.time()

time_diff = end_time - start_time

print(gcd)
print(time_diff)

