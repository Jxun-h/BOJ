from sys import stdin

res, n = 0, int(stdin.readline())
arr = []
for i in range(n):
    arr.append(int(stdin.readline()))

arr.sort(reverse=True)

for i in range(1, n + 1):
    tips = arr[i-1] - (i - 1)
    if tips > 0:
        res += tips

print(res)