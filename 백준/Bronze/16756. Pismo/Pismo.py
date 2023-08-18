n = int(input())
arr = list(map(int, input().split()))
ans = int(1e9)
for i in range(1, n):
    ans = min(abs(arr[i] - arr[i- 1]), ans)
print(ans)