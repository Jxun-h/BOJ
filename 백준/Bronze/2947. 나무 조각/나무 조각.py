from sys import stdin

arr = list(map(int, stdin.readline().split()))
ans = [1, 2, 3, 4, 5]
l = len(arr)

while 1:
    for i in range(l - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(*arr)

    if ans == arr:
        break