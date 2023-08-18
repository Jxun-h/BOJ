from sys import stdin
x, l, r = map(int, stdin.readline().split())
ans = int(1e9)
for i in range(l, r + 1):
    if abs(x - i) < abs(x - ans):
        ans = i
print(ans)