from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
visited = [0 for _ in range(100001)]

l, ans = 0, 0
for r in range(n):
    visited[arr[r]] += 1
    while l < r and visited[arr[r]] != 1:
        visited[arr[l]] -= 1
        l += 1

    ans += (r - l + 1)
print(ans)
