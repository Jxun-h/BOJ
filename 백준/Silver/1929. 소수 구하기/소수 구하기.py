from sys import stdin
from math import sqrt as sq
ipt = stdin.readline

m, n = ipt().split()
m, n = int(m), int(n)

arr = [x for x in range(m, n+1) if (x % 2 != 0 or x == 2) and x != 1]
result_arr = []

for x in arr:
    chk = True
    for y in range(2, int(sq(x))+1):
        if x % y == 0:
            chk = False
            break
    if chk:
        print(x)