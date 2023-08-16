from sys import stdin

n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(int(stdin.readline()))

ans = -1
arr.sort(reverse=True)

if n > 3:
    for i in range(n-2):
        if arr[i] < arr[i + 1] + arr[i + 2]:
            ans = max(ans, arr[i + 1] + arr[i + 2] + arr[i])
else:
    if arr[0] < arr[1] + arr[2]:
        ans = max(ans, arr[0] + arr[1] + arr[2])

print(ans)