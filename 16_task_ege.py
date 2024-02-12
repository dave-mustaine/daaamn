import sys
from functools import lru_cache

sys.setrecursionlimit(1_000_000_000)


# number = 0
# func = 0
# number_of_zeros = 0


@lru_cache
def f(n):
    if n > 0 and (not n % 2):
        return n
    elif n > 0 and (n % 2):
        return f(n - 1)


# while func != 34:
#     func = f(number)
#     number += 1

print(f(11))
# for i in range(number, 6000):
#     n = i
#     while True:
#         n = (n / 6 - 2) / 6
#         print(i)
