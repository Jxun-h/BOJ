from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().split())
grade = [len(stdin.readline().rstrip()) for x in range(n)]
grade_q = [deque() for _ in range(21)]
ans = 0

for i, v in enumerate(grade):
    while grade_q[v] and i - grade_q[v][0] > k:
        grade_q[v].popleft()
    
    if grade_q[v]:
        ans += len(grade_q[v])
    
    grade_q[v].append(i)

print(ans)