import sys

sys.setrecursionlimit(4000)
def f(k):
    if k == 1:
        return 1
    if k > 1:
        return k * f(k-1)
print(f(2023) / f(2020))