def f():
    def g(a):
        return a + 1
    def h(a):
        return 2 * a
    global x
    y = g(x) + h(x)
    print(y)
    x = 22

x = 7
f()

