from sys import stdin

ans = 0

for _ in range(int(stdin.readline())):
    a, d, g = map(int, stdin.readline().split())

    if a == d + g:
        ans = max(a * (d + g) * 2, ans)
    else:
        ans = max(ans, a * (d + g))

print(ans)