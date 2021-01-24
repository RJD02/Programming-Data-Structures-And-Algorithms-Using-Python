def divides(m, n):
    if n % 2 == 0:
        return True
    return False

def even(n):
    return divides(2, n)

def odd(n):
    return (not divides(2, n))

print(odd(33))
print(even(22))
