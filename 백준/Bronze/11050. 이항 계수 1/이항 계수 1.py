from math import factorial
from sys import stdin

n, k = map(int, stdin.readline().split())

if 0 <= k <= n:
    print(factorial(n) // (factorial(k) * factorial((n - k))))
elif k < 0 or k > n:
    print(0)