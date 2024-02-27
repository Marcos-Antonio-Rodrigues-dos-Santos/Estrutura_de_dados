import math
from functools import lru_cache


def fat(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fat(n-1)*3


def pot(x,n):
    if n == 0:
        return 1
    else:
        return x * pot(x, n-1)
    

def inv(s):
    l = ""
    if len(s) < 2:
        return(s)
    return s[-1] + inv(s[:-1])
    

def sd(n):
    if n <= 9:
        return n
    return n % 10 + sd(n // 10)


@lru_cache(maxsize=None)
def fib(n):
    if n <= 2:
        return n
    return fib(n-1) + fib(n-2)


def mdc(a, b):
    c = 2
    if a and b == 1:
        return c
    return (a / 2) and (b / 2)

print(mdc(10, 5))

def dec2bin(n):
    ss
