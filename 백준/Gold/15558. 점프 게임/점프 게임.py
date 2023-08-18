from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().split())
board = []
for p in range(2):
    board.append(list(map(int, list(stdin.readline().rstrip()))) + [1])


def bfs(pos, num):
    q = deque()
    sec = 0
    q.append((pos, num))
    visited = [[1] * (n + 1) for _ in range(2)]

    while q:
        visited[0][sec] = 0
        board[0][sec] = 0
        visited[1][sec] = 0
        board[1][sec] = 0

        for _ in range(len(q)):
            pos, now = q.popleft()

            for tf, mv in [(0, 1), (0, -1), (1, k)]:

                if tf == 1:
                    pos = (pos + 1) % 2

                if now + mv > n:
                    return 1

                if now + mv > -1 and board[pos][now + mv] == 1:
                    if visited[pos][now + mv] == 1:
                        q.append((pos, now + mv))
                        visited[pos][now + mv] = 0

        sec += 1

    return 0


print(bfs(0, 0))
