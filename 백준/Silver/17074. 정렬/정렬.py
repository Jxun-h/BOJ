from sys import stdin

n = int(stdin.readline())
arr = [-int(1e9)] + list(map(int, stdin.readline().split())) + [int(1e9)]

cnt = 0
pos = 0
ans = 0

for i in range(2, n + 1):
    if arr[i - 1] > arr[i]:
        cnt += 1
        pos = i

if cnt == 0:
    ans = n

elif cnt == 1:
    if arr[pos - 2] <= arr[pos]:
        ans += 1

    if arr[pos - 1] <= arr[pos + 1]:
        ans += 1

print(ans)
