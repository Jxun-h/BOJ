from collections import deque
from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().split()
    s.reverse()

    q = deque()
    while s:
        if not q:
            q.append(s.pop())
            continue

        data = s.pop()
        if len(q) == 1:
            if q[-1] >= data:
                q.appendleft(data)
            else:
                q.append(data)

        else:
            if q[0] >= data:
                q.appendleft(data)

            else:
                q.append(data)

    print(''.join(q))