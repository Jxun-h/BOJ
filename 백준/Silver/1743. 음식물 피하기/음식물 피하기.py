from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

n, m, k = map(int, stdin.readline().split())
arr = [[0] * (m + 1) for _ in range(n + 1)]
food_t = []

for _ in range(k):
    x, y = map(int, stdin.readline().split())
    arr[x][y] = 1
    food_t.append((x, y))

answer = -1e9
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]


def dfs(x, y):
    global res
    if x < 0 or y < 0 or x > n or y > m:
        return

    if arr[x][y] == 1:
        arr[x][y] = 0
        res += 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])

        return


for x, y in food_t:
    res = 0
    dfs(x, y)
    answer = max(res, answer)

print(answer)
