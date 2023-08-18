from sys import stdin

n, l, k = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))

arr.sort(key=lambda x: (x[1], x[0]))

ans = 0

for i in range(n):
    if k == 0:
        break

    if arr[i][1] <= l and arr[i][0] <= l:
        ans += 140
        k -= 1

    elif arr[i][1] > l and arr[i][0] <= l:
        ans += 100
        k -= 1

print(ans)