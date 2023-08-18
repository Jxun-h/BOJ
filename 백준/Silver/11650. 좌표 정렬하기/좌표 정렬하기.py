from sys import stdin
arr = []
for _ in range(int(stdin.readline())):
    arr.append(list(map(int, stdin.readline().split())))

arr.sort(key=lambda x: (x[0], x[1]))
for i in arr:
    print(*i)