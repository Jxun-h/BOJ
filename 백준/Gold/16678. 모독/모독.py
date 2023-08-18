from sys import stdin

arr = []
n = int(stdin.readline())
for _ in range(n):
    arr.append(int(stdin.readline()))

ans, i = 0, 1
for x in sorted(arr):
    if x >= i:
        ans += (x - i)
        i += 1

print(ans)