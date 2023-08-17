from sys import stdin
from math import factorial as fa

while 1:
    n = int(stdin.readline())
    if n == 0:
        break

    l = len(str(n))
    ans = 0

    for i in str(n):
        ans += fa(l) * int(i)
        l -= 1

    print(ans)