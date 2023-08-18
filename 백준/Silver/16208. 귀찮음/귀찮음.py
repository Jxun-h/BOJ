from sys import stdin
from collections import deque

n = int(stdin.readline())
need_stick = deque()
need_stick.extend(sorted(list(map(int, stdin.readline().split()))))
stack = []
ans = 0


while need_stick:
    if not stack:
        stack.append(need_stick.popleft())
    elif stack and need_stick:
        a, b = stack.pop(), need_stick.popleft()
        data = a * b
        need_stick.append(a + b)
        ans += data
    else:
        break

print(ans)