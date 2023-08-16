from sys import stdin
from math import lcm

arr = list(map(int, stdin.readline().split()))
res = int(1e9)

for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            res = min(res, lcm(arr[i], arr[j], arr[k]))
print(res)