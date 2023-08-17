import math
from sys import stdin

n, l = map(int, stdin.readline().split())
arr = []

for _ in range(n):
    data = tuple(map(int, stdin.readline().split()))
    arr.append(data)

arr.sort()
answer = 0
pre_time = 0

for s, e in arr:
    if s <= pre_time:
        s = pre_time + 1

        if e <= s:
            continue

    current_cnt = math.ceil((e-s) / l)
    answer += current_cnt
    pre_time = max(pre_time, s + current_cnt * l - 1)
    
print(answer)
