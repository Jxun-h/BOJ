from sys import stdin

arr = list(map(int, stdin.readline().split()))
od = 0
ans = 1

for i in range(3):
    if arr[i] % 2 != 0:
        ans *= arr[i]
        od = 1

if od:
    print(ans)
else:
    print(arr[0] * arr[1] * arr[2])