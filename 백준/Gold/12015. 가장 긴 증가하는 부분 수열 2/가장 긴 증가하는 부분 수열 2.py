from sys import stdin
from bisect import bisect_left

n = int(stdin.readline().strip())
dp = []
data = list(map(int, stdin.readline().split()))
dp.append(data[0])
for i in data[1:]:
    if dp[-1] < i:
        dp.append(i)
    else:
        dp[bisect_left(dp, i)] = i

print(len(dp))