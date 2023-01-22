import sys
sys.setrecursionlimit(10000)


def fib(n):
    if n == 1:
        return 1
    else:
        return n * fib(n-1) - 1


print(fib(1000)//fib(997))
