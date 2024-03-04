import functools as ft
import sys
 
sys.setrecursionlimit(100000)
@ft.lru_cache(maxsize=None)

def f(n):
    if n == 0 : return 1
    return 2 * f(n-1)
