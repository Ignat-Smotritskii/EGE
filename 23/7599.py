def f(n, k):
    if n == k:
        return 1
    if n > k or n == 13:
        return 0
    return f(n+1, k) + f(n+2, k) + f(n*3, k)


print(f(3, 8) * f(8, 18))
