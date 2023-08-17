from sys import stdin
import heapq

n = int(stdin.readline())
q = []
cnt = 0
for _ in range(n):
    data = list(map(int, stdin.readline().split()))
    for j in data:
        if cnt != n:
            heapq.heappush(q, j)
            cnt += 1
        else:
            if q[0] < j:
                heapq.heappop(q)
                heapq.heappush(q, j)

q.sort()
print(q[0])