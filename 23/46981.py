def f(x, y, mul):
    if x > y:
        return 0
    if x == y:
        return 1
    if mul:
        return f(x + 1, y, False) + f(x + 2, y, False)
    else:
        return f(x + 1, y, False) + f(x + 2, y, False) + f(x * 2, y, True)


print(f(1, 11, False))