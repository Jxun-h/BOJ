from itertools import combinations
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()

for tmp in combinations(arr, m):
    print(*tmp)