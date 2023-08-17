from sys import stdin
from math import pi
ipt = stdin.readline

r = int(ipt().rstrip())
print('%.6f' % (pi * (r**2)))
print('%.6f' % (2 * (r**2)))