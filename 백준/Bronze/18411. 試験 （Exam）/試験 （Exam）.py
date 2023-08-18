from sys import stdin

arr = list(map(int, stdin.readline().split()))
arr.sort()
print(arr[1] + arr[2])