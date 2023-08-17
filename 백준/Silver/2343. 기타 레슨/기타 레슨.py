from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))


def get_cnt():
    count = 0
    temp = 0
    for i in range(n):
        if temp + arr[i] > mid:
            count += 1
            temp = 0
        temp += arr[i]

    if temp:
        count += 1

    return count


left, right =max(arr), sum(arr)
while left <= right:
    mid = (left + right) // 2
    cnt = get_cnt()
    if cnt > m:
        left = mid + 1
    elif cnt <= m:
        right = mid - 1

print(max(left, right, mid))