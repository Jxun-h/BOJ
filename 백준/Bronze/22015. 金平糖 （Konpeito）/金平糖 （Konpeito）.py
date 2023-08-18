from sys import stdin
arr = list(map(int, stdin.readline().split()))
arr.sort()
res = 0
for i in range(2):
    res += (arr[-1] - arr[i])
print(res)