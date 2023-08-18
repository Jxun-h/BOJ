from sys import stdin

a, b, c, m = map(int, stdin.readline().split())
stamina = 0
ans = 0

for i in range(24):
    if stamina + a > m:
        stamina = 0 if stamina - c < 0 else stamina - c
        continue
    else:
        stamina += a
        ans += b

print(ans)