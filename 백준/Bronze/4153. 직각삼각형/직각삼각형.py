from sys import stdin

while 1:
    arr = list(map(int, stdin.readline().split()))
    if sum(arr) == 0:
        break
    arr.sort()
    if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2:
        print('right')
    else:
        print('wrong')