def fib(n):
    global dp
    if dp[n] != -1:
        return dp[n]
    if n == 0 or n == 1:
        return n
    value = fib(n - 1) + fib(n - 2)
    dp[n] = value
    return value

n = int(input())
dp = [-1 for i in range(n + 1)]
print(fib(n))
