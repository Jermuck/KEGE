import sys
from  functools import lru_cache
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(x):
    if x <= 4:
        return 1;
    if x > 4:
        return f(x - 1) + f(x - 3) + g(x - 2);
@lru_cache(None)
def g(x):
    if x <= 1500:
        return g(x + 1) + g(x + 2) + 1;
    if x > 1500:
        return 5;
print((f(1200) + g(100)) % 10000)