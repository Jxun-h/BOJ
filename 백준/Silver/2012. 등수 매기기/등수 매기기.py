from sys import stdin

n = int(stdin.readline())
s = []
for i in range(n):
    s.append(int(stdin.readline()))

s.sort()
ans = 0
for i in range(1, n + 1):
    ans += abs(i - s[i - 1])
print(ans)