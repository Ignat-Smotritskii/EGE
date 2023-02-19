def f(n, k, q):
    if n == k:
        return 1
    elif n > k:
        return 0
    elif q == 0:
        return f(n+1, k, 0) + f(n+2, k, 0) + f(n*2, k, 1)
    else:
        return f(n + 1, k, 0) + f(n + 2, k, 0)


print(f(1, 9, 0))
