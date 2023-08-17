from sys import stdin
from itertools import permutations

arr = []
for _ in range(9):
    arr.append(int(stdin.readline()))

for j in list(permutations(arr, 7)):
    if sum(j) == 100:
        for k in sorted(list(j)):
            print(k)

        break