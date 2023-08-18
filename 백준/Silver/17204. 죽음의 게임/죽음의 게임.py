from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [[] for _ in range(n + 1)]

for i in range(n):
    arr[i].append(int(stdin.readline()))


def solve(x):
    q = deque()
    q.append((0, x))
    visited = set()

    while q:
        number, x = q.popleft()

        if number > n and m not in visited:
            return -1

        if x == m:
            return number

        if arr[x][0]:
            q.append((number + 1, arr[x][0]))

    return -1


print(solve(0))