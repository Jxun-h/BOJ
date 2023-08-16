from sys import stdin
from itertools import combinations

words = []
res = set()
tc = int(stdin.readline())

if tc == 1:
    print(res)
else:
    for _ in range(tc):
        words.append(stdin.readline().rstrip())

    for pair in list(set(combinations(words, 2))):
        change = dict()
        use = set()
        tf = True
        x, y = pair
        a, b = pair
        a, b = list(a), list(b)
        n, m = len(a), len(b)

        if n != m:
            continue
        else:
            for i in range(n):
                if a[i] != b[i] and b[i] not in use and a[i] not in change:
                    change[a[i]] = b[i]
                    use.add(b[i])
                    a[i] = b[i]
                else:
                    if a[i] in change:
                        a[i] = change[a[i]]
                    else:
                        if a[i] in use:
                            tf = False
                            break
                        else:
                            change[a[i]] = b[i]
                            use.add(b[i])

            if a == b and tf:
                res.add((x, y))

    print(len(res))