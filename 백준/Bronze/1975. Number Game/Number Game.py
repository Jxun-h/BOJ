from sys import stdin


def solution(n, x, arr):
    if n < x:
        arr.append(n)
        return arr

    if n % x == 0:
        arr.append(0)
        return solution(n // x, x, arr)

    else:
        arr.append(1)
        return solution(n // x, x, arr)


def chk_zero(arr, idx, cnt):
    if arr[idx] == 0:
        return chk_zero(arr, idx+1, cnt+1)
    else:
        return cnt


t = int(stdin.readline().rstrip())


for step in range(t):
    n = int(stdin.readline().rstrip())
    idx = 0
    cnt = 0
    for x in range(2, n+1):
        arr = []
        if n % x == 0:
            tmp_arr = (solution(n, x, arr))
            cnt = chk_zero(tmp_arr, idx, cnt)

    print(cnt)