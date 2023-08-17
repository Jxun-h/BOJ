from sys import stdin

s = stdin.readline().rstrip()
ans = 0
for i in ['a', 'e', 'i', 'o', 'u']:
    ans += s.count(i)

print(ans)