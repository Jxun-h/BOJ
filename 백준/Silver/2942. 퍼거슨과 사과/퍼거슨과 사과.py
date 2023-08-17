from sys import stdin
from math import gcd, sqrt

r, g = map(int, stdin.readline().split())

l = []
temp = gcd(r, g)
sqrt_temp = sqrt(temp)

for i in range(1, int(sqrt_temp) + 1):
    if temp % i == 0:
        l.append(i)
        if temp // i == i:
            continue
        l.append(temp // i)

for i in l:
    print(i, r // i, g // i)
