import sys

# input() 함수보다 빠르다
ipt = sys.stdin.readline

count = int(ipt())
arr = [0] * 10001

for x in range(count):
    num = int(ipt())
    arr[num] = arr[num] + 1

for x in range(10001):
    if arr[x] != 0:
        for y in range(arr[x]):
            print(x)