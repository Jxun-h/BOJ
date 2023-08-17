from sys import stdin
from math import gcd

a, b = map(int, stdin.readline().split())

print(a + b - 1 - (gcd(a, b) - 1))