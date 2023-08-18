from sys import stdin

ans = 1
n = int(stdin.readline())
if n > 1:
    for x in range(2, n + 1):
        ans *= x

print(ans)