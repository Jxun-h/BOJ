from sys import stdin

arr = [[0 for _ in range(31)] for _ in range(31)]

for i in range(1, 31):
    arr[1][i] = i

for i in range(2, 31):
    for j in range(i, 31):
        if i == j:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i - 1][j - 1] + arr[i][j - 1]


for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    print(arr[a][b])