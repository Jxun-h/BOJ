from sys import stdin

inp = stdin.readline
arr = []

n = int(inp())
for _ in range(n):
    arr.append(list(map(int, inp().split())))

arr.sort(key=lambda x: (-x[1]))
ans = arr[0][1] - arr[0][0]

for i in range(1, n):
    if ans > arr[i][1]:
        ans = arr[i][1] - arr[i][0]
    else:
        ans -= arr[i][0]

print(ans if ans >= 0 else -1)