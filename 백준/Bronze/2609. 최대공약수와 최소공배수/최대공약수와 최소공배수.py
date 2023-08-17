from sys import stdin
from math import gcd, lcm

a, b = map(int, stdin.readline().split())
print(gcd(a, b), lcm(a, b), sep='\n')