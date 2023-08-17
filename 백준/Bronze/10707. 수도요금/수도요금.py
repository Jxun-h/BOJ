from sys import stdin

a, b, c, d, p = [int(stdin.readline()) for _ in range(5)]
ans = min(a * p, (p - c) * d + b) if p > c else min(a * p, b)
print(ans)
