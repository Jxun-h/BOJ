from sys import stdin

tetro = {
    # ㅁ
    0: [[(0, 0), (0, 1), (1, 0), (1, 1)]],
    # ㄱ,ㄴ
    1: [[(0, 0), (0, 1), (0, 2), (-1, 0)], [(0, 0), (0, 1), (0, 2), (1, 0)], [(0, 0), (0, 1), (0, 2), (1, 2)],
        [(0, 0), (0, 1), (0, 2), (-1, 2)],
        [(0, 0), (-1, 0), (-2, 0), (0, 1)], [(0, 0), (-1, 0), (-2, 0), (0, -1)], [(0, 0), (1, 0), (2, 0), (0, -1)],
        [(0, 0), (1, 0), (2, 0), (0, 1)]],
    # ㅡ, ㅣ
    2: [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)]],
    # ㅗ, ㅓ
    3: [[(0, 0), (1, -1), (1, 0), (1, 1)], [(0, 0), (-1, -1), (-1, 0), (-1, 1)],
        [(0, 0), (0, 1), (-1, 1), (1, 1)], [(0, 0), (0, -1), (-1, -1), (1, -1)]],
    # ㄹ - =
    4: [[(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (-1, 1), (-1, 2)],
        [(0, 0), (1, 0), (1, -1), (2, -1)], [(0, 0), (0, 1), (1, 1), (1, 2)]]
}


n, m = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))


def get_value(x, y, blocks):
    global res
    for block in blocks:
        value = 0
        for i, j in block:
            nx, ny = i + x, j + y
            if -1 < nx < n and -1 < ny < m:
                value += board[nx][ny]
            else:
                break

        res = max(res, value)


res = -int(1e9)
for x in range(5):
    blocks = tetro[x]
    for i in range(n):
        for j in range(m):
            get_value(i, j, blocks)

print(res)