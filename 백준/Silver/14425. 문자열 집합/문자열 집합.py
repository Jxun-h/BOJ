from sys import stdin

n, m = map(int, stdin.readline().split())
ans = 0

arr = dict()
for _ in range(n):
    key = stdin.readline().rstrip()
    arr[key] = 0

for _ in range(m):
    s = stdin.readline().rstrip()
    if s in arr:
        ans += 1

print(ans)