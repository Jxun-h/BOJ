from sys import stdin
from itertools import combinations

mo_um = []

l, c = map(int, stdin.readline().split())
alpha = list(stdin.readline().rstrip().split())

for i in alpha:
    if i in ("a", "e", "i", "o", "u"):
        mo_um.append(i)

res = set()
for i in list(set(combinations(alpha, l))):
    length = l
    for k in mo_um:
        if k in i:
            length -= 1
    if length < 2 or length == l:
        continue
    else:
        res.add(tuple(sorted(list(i))))

for i in list(sorted(res)):
    print(''.join(i))
