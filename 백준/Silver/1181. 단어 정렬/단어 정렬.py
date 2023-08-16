from sys import stdin

arr = set()
for i in range(int(stdin.readline())):
    s = stdin.readline().rstrip()
    l = len(s)
    arr.add((l, s))

arr = list(arr)
arr.sort(key=lambda x: (x[0], x[1]))
for l, s in arr:
    print(s)