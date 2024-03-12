import sys

arr = [[y for y in range(31)] for x in range(31)]

for x in range(2, 31):
    for y in range(x, 31):
        if x == y:
            arr[x][y] = 1
        else:
            arr[x][y] = arr[x - 1][y - 1] + arr[x][y - 1]

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(arr[a][b])
