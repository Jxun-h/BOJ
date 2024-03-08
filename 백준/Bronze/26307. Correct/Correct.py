import sys


arr = list(map(int, sys.stdin.readline().split()))
print((arr[0] - 9) * 60 + arr[1])