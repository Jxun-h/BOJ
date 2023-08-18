from sys import stdin, setrecursionlimit

setrecursionlimit(2000)


def visit_tf(pos, cur_direction, next_direction):
    x, y = pos
    return cur_direction != next_direction and 0 <= y < m


def solve(pos, cur_pos):
    x, y = pos
    if x == n:
        return 0

    if dp[x][y][cur_pos] != int(1e9):
        return dp[x][y][cur_pos]

    for next_pos, dy in enumerate(direction):
        npx, npy = x + 1, y + dy
        if visit_tf((npx, npy), cur_pos, next_pos):
            data = solve((npx, npy), next_pos) + arr[x][y]
            dp[x][y][cur_pos] = min(data, dp[x][y][cur_pos])

    return dp[x][y][cur_pos]


if __name__ == '__main__':
    n, m = map(int, stdin.readline().split())
    arr = []
    answer = int(1e9)
    dp = [[[answer] * 3 for i in range(m)] for _ in range(n)]

    direction = [-1, 0, 1]

    for _ in range(n):
        arr.append(list(map(int, stdin.readline().split())))

    for i in range(m):
        for j in range(3):
            answer = min(answer, solve((0, i), j))

    print(answer)
