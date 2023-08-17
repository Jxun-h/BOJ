from sys import stdin
from math import gcd

a, b = map(int, stdin.readline().split())
temp = b // a
aa, bb = int(1e9), int(1e9)

for i in range(1, b):
    if i * i > temp:
        break

    if temp % i == 0:
        if gcd(i, temp // i) == 1:
            aa, bb = i, temp // i

print(aa * a, bb * a)