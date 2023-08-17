from sys import stdin
from math import lcm, gcd

a1, b1 = map(int, stdin.readline().split())
a2, b2 = map(int, stdin.readline().split())

l = lcm(b1, b2)

res = [a1 * (l // b1) + a2 * (l // b2), l]
g = gcd(res[0], res[1])

res[0], res[1] = res[0] // g, res[1] // g

print(*res)