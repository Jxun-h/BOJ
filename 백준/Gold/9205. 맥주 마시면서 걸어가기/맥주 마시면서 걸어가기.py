from sys import stdin

for step in range(int(stdin.readline())):
    n = int(stdin.readline())
    data = []
    for i in range(n + 2):
        data.append(tuple(map(int, stdin.readline().split())))

    arr = [[0] * (n + 2) for _ in range(n + 2)]

    for i in range(n + 2):
        for j in range(n + 2):
            if i != j:
                ix, iy = data[i]
                jx, jy = data[j]

                if abs(ix - jx) + abs(iy - jy) <= 1000:
                    arr[i][j] = 1

    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                if i != j:
                    if arr[i][k] and arr[k][j]:
                        arr[i][j] = 1

    print('happy') if arr[0][n + 1] == 1 else print('sad')