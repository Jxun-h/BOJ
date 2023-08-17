from sys import stdin

n = int(stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(stdin.readline().rstrip()))
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def solve():
    ans = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1

            ans = cnt if cnt > ans else ans

        cnt  = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
            else:
                cnt = 1

            ans = cnt if cnt > ans else ans

    return ans


res = -int(1e9)
for i in range(n):
    for j in range(n):
        for k in range(4):
            nx, ny = dx[k] + i, dy[k] + j
            if -1 < nx < n and -1 < ny < n:
                if arr[nx][ny] != arr[i][j]:
                    arr[i][j], arr[nx][ny] = arr[nx][ny], arr[i][j]
                    res = max(res, solve())
                    arr[i][j], arr[nx][ny] = arr[nx][ny], arr[i][j]

print(res)
