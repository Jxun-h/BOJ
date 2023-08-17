from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]


def bfs(board, now, goal, dist):
    q = deque()
    visited = []
    x, y = now
    q.append((0, x, y, []))
    visited.append(now)
    check = False

    while q:
        cost, x, y, visit = q.popleft()

        if cost > dist:
            continue

        if (x, y) == goal:
            for i, j in visit:
                if board[i][j] == 'X':
                    check = True
                elif board[i][j] == 'O':
                    return False

        for i in range(4):
            nx, ny = dx[i] + x, y + dy[i]
            if -1 < nx < 5 and -1 < ny < 5:
                if (nx, ny) not in visited:
                    # 목표 지점을 visited 에 넣지 않는다.
                    # 가능한 많은 경로를 염두에 두어 계산한다
                    if (nx, ny) != goal:
                        visited.append((nx, ny))
                    temp = visit[:]
                    temp.append((nx, ny))
                    q.append((cost + 1, nx, ny, temp))
    return check


def solution(places):
    answer = []

    for i in range(len(places)):
        board = []
        data = places[i]

        ps = []

        # 대기실 리스트 만들기
        for j in range(5):
            for k in range(5):
                if data[j][k] == 'P':
                    ps.append((j, k))
            board.append(list(data[j]))

        ps.sort()
        check = True
        for j in range(len(ps)):
            x1, y1 = ps[j]
            for k in range(j + 1, len(ps)):
                x2, y2 = ps[k]
                dist = abs(x1 - x2) + abs(y1 - y2)
                if dist < 3:
                    if not bfs(board, ps[j], ps[k], dist):
                        check = False
                        break
            if not check:
                break

        answer.append(1) if check else answer.append(0)

    return answer


print(solution([["OOPXO",
                 "OPXOO", "OOOOO", "OOOOO", "OOOOO"]]))

print(solution([["OOPOO",
                 "OPOOO", "OOOOO", "OOOOO", "OOOOO"]]))

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))