from math import trunc
from sys import stdin

a, b = map(int, stdin.readline().split())
z = b * 100 // a

ans = int(1e11)
start, end = 0, max(a, b)

while start <= end:
    mid = (start + end) // 2
    res = (b + mid)  * 100 // (a + mid)

    if res != z:
        ans = min(ans, mid)
        end = mid - 1
    else:
        start = mid + 1

print(ans if ans != int(1e11) else -1)