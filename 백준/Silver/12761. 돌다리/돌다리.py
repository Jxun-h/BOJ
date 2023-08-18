from sys import stdin
from collections import deque

a, b, n, m = map(int, stdin.readline().split())
dp = [-1 for _ in range(100001)]


def solve():
    q = deque()
    q.append(n)
    dp[n] = 0
    while q:
        x = q.popleft()
        for i in (x * a, x * b, x + a, x - a, x + b, x - b, x + 1, x - 1):
            if 0 < i < 100001:
                if dp[i] == -1:
                    dp[i] = dp[x] + 1
                    q.append(i)
                    
solve()
print(dp[m])
