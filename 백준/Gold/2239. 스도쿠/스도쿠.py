from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

arr = []
for _ in range(9):
    arr.append(list(map(int, list(stdin.readline().rstrip()))))
c1 = [[False] * 10 for _ in range(9)]
c2 = [[False] * 10 for _ in range(9)]
c3 = [[False] * 10 for _ in range(9)]


def calc(x, y):
    return (x // 3) * 3 + (y // 3)


def solve(n):
    if n == 81:
        for i in arr:
            print(''.join(map(str, i)))
        return True

    x = n // 9
    y = n % 9

    if arr[x][y]:
        return solve(n + 1)

    else:
        for i in range(1, 10):
            if not c1[x][i] and not c2[y][i] and not c3[calc(x, y)][i]:
                c1[x][i] = c2[y][i] = c3[calc(x, y)][i] = True
                arr[x][y] = i
                if solve(n + 1):
                    return True
                c1[x][i] = c2[y][i] = c3[calc(x, y)][i] = False
                arr[x][y] = 0

    return False


for i in range(9):
    for j in range(9):
        if arr[i][j]:
            c1[i][arr[i][j]] = True
            c2[j][arr[i][j]] = True
            c3[calc(i, j)][arr[i][j]] = True

solve(0)