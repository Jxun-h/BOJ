from sys import stdin
from itertools import permutations as p

arr = []
n, k = int(stdin.readline()), int(stdin.readline())
for i in range(n):
    arr.append(int(stdin.readline()))

res = set()
for i in list(set(p(arr, k))):
    res.add(''.join(list(map(str, i))))

print(len(res))