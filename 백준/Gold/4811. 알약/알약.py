from sys import stdin

arr = [[0] * 31 for _ in range(31)]
arr[0][1] = 1
for i in range(31):
    for j in range(i, 31):
        if i == 0:
            arr[i][j] = 1
        else:
            if i == j:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = arr[i-1][j] + arr[i][j-1]

while 1:
    n = int(stdin.readline())
    if n == 0:
        break

    print(arr[n][n])

