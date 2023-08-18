from sys import stdin

n, k = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(stdin.readline()))

l, r = 1, max(arr)
answer = 0

while l <= r:
    mid = (l + r) // 2

    t = sum(i // mid for i in arr)
    if t >= k:
        answer = mid
        l = mid + 1

    else:
        r = mid - 1

print(answer)
        