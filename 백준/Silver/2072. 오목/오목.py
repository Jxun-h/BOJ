from sys import stdin

board = [[0] * 20 for _ in range(20)]
dx, dy = [1, 0, 0, -1,
          1, -1, -1, 1], \
         [0, 1, -1, 0,
          1, -1, 1, -1]
players = [[], []]


def check_win(p):
    visited = [[-1] * 20 for _ in range(20)]
    for x, y in sorted(players[p - 1]):
        for i in range(8):
            cnt = 0
            nx, ny = x, y
            while 0 < nx < 20 and 0 < ny < 20 and board[nx][ny] == p and visited[nx][ny] != i:
                visited[nx][ny] = i
                cnt += 1
                nx += dx[i]
                ny += dy[i]

            if cnt == 5:
                return True

    return False


for i in range(1, int(stdin.readline()) + 1):
    a, b = map(int, stdin.readline().split())
    board[a][b] = 1 if i % 2 != 0 else 2
    players[(i + 1) % 2].append((a, b))

    if i > 8:
        for player in range(1, 3):
            if check_win(player):
                print(i)
                exit()

print(-1)