from sys import stdin

e, f, c = map(int, stdin.readline().split())
empty = e + f
ans = 0
while empty // c > 0:
    ans += empty // c
    temp = empty // c
    empty %= c
    empty += temp

print(ans)