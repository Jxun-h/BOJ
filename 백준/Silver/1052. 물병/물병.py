from sys import stdin

n, k = map(int, stdin.readline().split())

arr = [0 for _ in range(26)]
arr[1] = n
buy_bottle = 0


while 1:
    for i in range(1, 26):
        if arr[i] // 2 > 0:
            arr[i + 1] += arr[i] // 2
            arr[i] %= 2
        else:
            break

    if sum(arr) <= k:
        print(buy_bottle)
        break

    else:
        buy_bottle += 1
        arr[1] += 1