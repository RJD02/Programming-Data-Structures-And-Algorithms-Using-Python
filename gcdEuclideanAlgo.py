import time
start = time.time()

def gcd(m, n):
    if m < n:
        m, n = n, m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

m, n = input().split(" ")
m = int(m)
# m = int(m)
n = int(n)
print("Gcd = ", gcd(m, n))
end = time.time()
print("Time = ", (end - start) * 1000)
