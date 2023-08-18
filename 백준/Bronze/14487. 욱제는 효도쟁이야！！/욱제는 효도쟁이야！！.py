from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
print(sum(arr) - max(arr))