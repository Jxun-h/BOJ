from sys import stdin
from itertools import combinations

while 1:
    data = list(map(int, stdin.readline().split()))
    if len(data) == 1 and data[0] == 0:
        break
    else:
        a, arr = data[0], data[1:]
        res = []
        for x in list(set(combinations(arr, 6))):
            if len(set(x)) == 6:
                temp = sorted(list(x))
                if temp not in res:
                    res.append(temp)

    for x in sorted(list(res)):
        print(*x)
    print()
