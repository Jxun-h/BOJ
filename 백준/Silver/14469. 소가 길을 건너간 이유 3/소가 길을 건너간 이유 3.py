from sys import stdin

n = int(stdin.readline())
arr = []

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[0], x[1]))

ans = 0

for i in range(n):
    s, c = arr[i][0], arr[i][1]
    if ans <= s:
        ans = s
        ans += c

    else:
        ans += c

print(ans)