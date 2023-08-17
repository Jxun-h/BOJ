import sys

# input() 함수보다 좀 더 빠름
ipt = sys.stdin.readline
result = 0

count = int(ipt())
arr = [int(x) for x in ipt().split()]

arr.sort()

for x in range(1, count+1):
    result += sum(arr[0:x])

print(result)