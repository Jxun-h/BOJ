from sys import stdin
from math import factorial

n, m = int(stdin.readline()), int(stdin.readline())
vip = []
for _ in range(m):
    vip.append(int(stdin.readline()))
arr = [1, 1, 2]
for i in range(3, 41):
    arr.append(arr[i-2] + arr[i-1])

ans = 1
if m > 0:
    pre = 0
    for i in range(m):
        ans *= arr[vip[i] - 1 - pre]
        pre = vip[i]
    ans *= arr[n - pre]
else:
    ans = arr[n]
print(ans)