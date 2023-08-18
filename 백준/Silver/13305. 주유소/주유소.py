import sys
from sys import stdin

k = int(stdin.readline())
dist = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))

# 17점
if sum(cost) == k:
    print(sum(dist))

else:
    start = 0
    res = cost[start] * sum(dist)

    idx = 1
    while idx < k:
        temp = 0
        for i in range(start, idx):
            temp += (cost[i] * dist[i])
        temp += (sum(dist[idx:]) * cost[idx])
        if res > temp:
            res = temp
        idx += 1

    print(res)