from sys import stdin

arr = [0 for _ in range(30001)]
arr[0], arr[1], arr[2], arr[3], arr[4] = 1, 1, 2, 6, 4
print(arr[int(stdin.readline())])