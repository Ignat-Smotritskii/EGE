def f(n, k):
    if n > k:
        return 0
    if n == k:
        return 1
    return f(n+3, k) + f(n*2, k)


print(f(3, 27) * f(27, 63))
