from sys import stdin
from itertools import permutations


n = int(stdin.readline())


for x in permutations(range(10), 7):

    h, e, l, o, w, r, d = x
    if h == 0 or w == 0:
        continue

    res1 = (h * 10000 + e * 1000 + l * 100 + l * 10 + o)
    res2 = (w * 10000 + o * 1000 + r * 100 + l * 10 + d)

    if (res1 + res2) == n:
        print("  %d" % res1)
        print("+ %d" % res2)
        print("-------")
        if res1 + res2 >= 100000:
            print(" %d" % (res1 + res2))
        else:
            print("  %d" % (res1 + res2))
        exit()

print('No Answer')