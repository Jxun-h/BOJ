from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

n = int(stdin.readline())
arr, ans = [], ''
for i in range(n):
    arr.append(list(map(int, list(stdin.readline().rstrip()))))


def check(x, y, mode):
    for i in range(x, x + mode):
        for j in range(y, y + mode):
            if arr[x][y] != arr[i][j]:
                return False
    return True


def solve(x, y, mode):
    global ans

    if check(x, y, mode):
        if arr[x][y] == 1:
            ans += '1'
        else:
            ans += '0'

    else:
        ans += '('
        solve(x, y, mode // 2)
        solve(x, y + mode // 2, mode // 2)
        solve(x + mode // 2, y, mode // 2)
        solve(x + mode // 2, y + mode // 2, mode // 2)
        ans += ')'


solve(0, 0, n)
print(ans)