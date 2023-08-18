from sys import stdin
from collections import deque

n = int(stdin.readline())
d = list(map(int, stdin.readline().split()))
front, ans = deque(range(1, n + 1)), deque()

while d:
    data = d.pop()
    num = front.popleft()

    if data == 1:
        ans.appendleft(num)

    elif data == 2:
        ans.insert(1, num)

    elif data == 3:
        ans.append(num)

print(*ans)