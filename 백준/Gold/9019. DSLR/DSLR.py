from collections import deque
from sys import stdin


def solve(a, b):
    q = deque()
    q.append((a, ''))
    visited[a] = 0

    while q:

        a, command = q.popleft()

        if a == b:
            return command

        temp = (a * 2) % 10000
        if visited[temp]:
            q.append((temp, command + 'D'))
            visited[temp] = 0

        temp = a - 1
        if temp < 0:
            temp = 9999
        if visited[temp]:
            q.append((temp, command + 'S'))
            visited[temp] = 0

        s_a = str(a)
        while len(s_a) < 4:
            s_a = '0' + s_a
        temp = s_a[1:] + s_a[0]
        if temp == '0000':
            temp = 0
        else:
            temp = int(temp)
        if visited[temp]:
            q.append((temp, command + 'L'))
            visited[temp] = 0

        s_a = str(a)
        while len(s_a) < 4:
            s_a = '0' + s_a
        temp = s_a[-1] + s_a[:-1]
        if temp == '0000':
            temp = 0
        else:
            temp = int(temp)
        if visited[temp]:
            q.append((temp, command + 'R'))
            visited[temp] = 0


for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    visited = [1 for __ in range(10000)]

    print(solve(a, b))
