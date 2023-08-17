from sys import stdin


n = int(stdin.readline())
start, end = 1, n
res = 1e99

if n != 0:
    while start <= end:
        mid = (start + end) // 2

        if mid ** 2 >= n:
            res = min(mid, res)

        if mid ** 2 < n:
            start = mid + 1
        else:
            end = mid - 1

    print(res)

else:
    print(0)