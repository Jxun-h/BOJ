from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
q = deque()
for i in range(1, n + 1):
    q.append(i)
res = 0

for i in arr:
    while 1:
        if q[0] != i:
            if len(q) // 2 >= q.index(i):
                temp = q.popleft()
                q.append(temp)
                res += 1
            else:
                q.appendleft(q.pop())
                res += 1
        else:
            q.popleft()
            break

print(res)