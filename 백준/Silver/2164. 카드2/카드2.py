from collections import deque
from sys import stdin

n = int(stdin.readline())
q = deque(range(1, n + 1))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(*q)