import time
start = time.time()
def gcd(m, n):
    if m % n == 0:
        return n
    if m < n:
        m,n = n,m
    return gcd(m,n)

m = input()
n = input()
print(gcd(int(m), int(n)))
end = time.time()
print("Time = ", end - start, "ms")
