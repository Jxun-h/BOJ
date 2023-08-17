from sys import stdin
from bisect import bisect_left, bisect_right


def binary(arr, i):
    r = bisect_right(arr, i)
    l = bisect_left(arr, i)
    return r - l


n, arr = int(stdin.readline()), sorted(list(map(int, stdin.readline().split())))
m, krr = int(stdin.readline()), list(map(int, stdin.readline().split()))

for i in krr:
    print(binary(arr, i))