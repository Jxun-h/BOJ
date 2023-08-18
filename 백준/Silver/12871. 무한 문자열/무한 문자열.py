from sys import stdin
from math import lcm

a = stdin.readline().rstrip()
b = stdin.readline().rstrip()
al, bl = len(a), len(b)
length = lcm(al, bl)
print(1 if a * (length // al) == b * (length // bl) else 0)
