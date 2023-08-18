from sys import stdin
from bisect import bisect_left

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    b.sort()
    ans = 0

    for i in range(n):
        std = a[i]
        idx = bisect_left(b, std)
        temp = 0

        if 0 < idx < m:
            t1, t2 = abs(b[idx - 1] - std),  abs(b[idx] - std)
            if t1 <= t2:
                temp = b[idx - 1]
            elif t1 > t2:
                temp = b[idx]
        else:
            if idx == m:
                temp = b[idx-1]
            else:
                temp = b[idx]

        ans += temp

    print(ans)