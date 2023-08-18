from sys import stdin
from bisect import bisect_left

for tc in range(1, int(stdin.readline()) + 1):
    n, k = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    ans1 = 'Case #{}'.format(tc)
    dp = [arr[0]]

    for i in range(1, n):
        if dp[-1] < arr[i]:
            dp.append(arr[i])
        else:
            j = bisect_left(dp, arr[i])
            dp[j] = arr[i]

    print(ans1)
    print(1 if len(dp) >= k else 0)