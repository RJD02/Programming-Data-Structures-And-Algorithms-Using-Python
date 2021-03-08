fib_table = {}

def fib(n):
    try:
        if fib_table[n]:
            return fib_table[n]
    except:
        if n == 0 or n == 1:
            value = n
        else:
            value = fib(n - 1) + fib(n - 2)
    fib_table[n] = value
    return value

n = int(input())
print(fib(n))
