from sys import stdin

n = int(stdin.readline())
arr = [stdin.readline().rstrip() for _ in range(n)]
ans = 'NEITHER'



if arr == list(sorted(arr)):
    ans = 'INCREASING'

if arr == list(sorted(arr, reverse=True)):
    ans = 'DECREASING'

print(ans)