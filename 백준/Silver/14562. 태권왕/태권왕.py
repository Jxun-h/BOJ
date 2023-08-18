from sys import stdin
from collections import deque


def solve(s, t):
    q = deque()
    q.append((0, s, t))

    while q:
        time, s, t = q.popleft()

        if s == t:
            return time

        if (t + 3) >= s * 2:
            if use[s * 2] == -1:
                q.append((time + 1, s * 2, t + 3))

        if use[s + 1] == -1:
            q.append((time + 1, s + 1, t))


for _ in range(int(stdin.readline())):
    s, t = map(int, stdin.readline().split())
    use = [-1 for _ in range(100001)]
    print(solve(s, t))