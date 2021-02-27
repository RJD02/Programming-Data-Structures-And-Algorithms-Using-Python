def f():
    global x
    y = x
    print(y)
    x = 22

x = 7
f()
print(x)
