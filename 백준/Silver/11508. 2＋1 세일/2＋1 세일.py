from sys import stdin

arr = []
n = int(stdin.readline())
for i in range(n):
    arr.append(int(stdin.readline()))

arr.sort(reverse=True)
ans = 0

for i in range(n):
    if i % 3 != 2:
        ans += arr[i]
print(ans)