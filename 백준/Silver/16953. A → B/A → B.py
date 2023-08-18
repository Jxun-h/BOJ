from sys import stdin
from collections import deque

a, b = map(int, stdin.readline().split())
q = deque()
q.append((a, 1))


def bfs():
    while q:
        k, cost = q.popleft()
        if k == b:
            return cost
        if k * 2 <= b:
            q.append((k * 2, cost + 1))

        if int(str(k) + '1') <= b:
            q.append((int(str(k) + '1'), cost + 1))

    return -1


print(bfs())