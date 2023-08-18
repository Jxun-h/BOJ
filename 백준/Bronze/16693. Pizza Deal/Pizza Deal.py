from sys import stdin
from math import pi
a1, p1 = map(int, stdin.readline().split())
r1, p2 = map(int, stdin.readline().split())
print('Whole pizza' if p1/a1 > p2/(r1**2*pi) else 'Slice of pizza')