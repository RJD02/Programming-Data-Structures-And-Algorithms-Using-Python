import time
start = time.time()

def gcd(m, n):
    if m < n:
        m, n = n, m
    if m % n == 0:
        return n
    else:
        diff = m - n
    return gcd(max(diff, n), min(diff, n))

m, n = input().split(" ")
m = int(m)
n = int(n)
print("gcd = ", gcd(m, n))

end = time.time()
print("Time = ", end - start)
