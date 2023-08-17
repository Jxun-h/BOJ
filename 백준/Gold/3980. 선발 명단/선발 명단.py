from sys import stdin


def solve(cnt):
    if cnt == 11:
        global ans
        if 0 not in position:
            ans = max(ans, sum(position))
        return

    for i in range(11):
        if board[cnt][i] != 0 and position[i] == 0:
            position[i] = board[cnt][i]
            board[cnt][i] = 0
            solve(cnt + 1)
            board[cnt][i] = position[i]
            position[i] = 0


for tc in range(int(stdin.readline())):
    board = []
    for _ in range(11):
        board.append(list(map(int, stdin.readline().split())))

    ans = 0
    position = [0 for __ in range(11)]

    solve(0)
    print(ans)