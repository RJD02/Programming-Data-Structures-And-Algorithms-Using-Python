def fib(n):
    if fib_table[n]:
        return fib_table[n]
    if n == 0 or n == 1:
        value = n
    else:
        value = fib(n - 1) + fib(n - 2)
    fib_table[n] = value
    return value

n = int(input())
fib_table = [0 for i in range(n + 1)]
print(fib(n))
