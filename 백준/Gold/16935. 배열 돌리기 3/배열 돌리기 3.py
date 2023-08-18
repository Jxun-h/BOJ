from sys import stdin

n, m, r = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))

command = list(map(int, list(stdin.readline().split())))
for i in range(r):
    if command[i] == 1:
        length = len(board)
        for j in range(length // 2):
            board[j], board[length - 1 - j] = board[length - 1 - j], board[j]

    elif command[i] == 2:
        for i in range(len(board)):
            board[i] = list(reversed(board[i]))

    elif command[i] == 3:
        if len(board) == n:
            new_board = [[0] * n for _ in range(m)]
            for j in range(m):
                for k in range(n):
                    new_board[j][n - 1 - k] = board[k][j]
        else:
            new_board = [[0] * m for _ in range(n)]
            for j in range(n):
                for k in range(m):
                    new_board[j][m - 1 - k] = board[k][j]

        board = new_board

    elif command[i] == 4:
        if len(board) == n:
            new_board = [[0] * n for _ in range(m)]
            for j in range(m - 1, -1, -1):
                for k in range(n - 1, -1, -1):
                    new_board[(m - 1) - j][k] = board[k][j]
        else:
            new_board = [[0] * m for _ in range(n)]
            for j in range(n - 1, -1, -1):
                for k in range(m - 1, -1, -1):
                    new_board[(n - 1) - j][k] = board[k][j]

        board = new_board

    elif command[i] == 5:
        r, c = len(board), len(board[0])
        new_board = [[0] * c for _ in range(r)]

        arr1 = [item[:c // 2] for item in board[:r // 2]]
        arr2 = [item[c // 2:] for item in board[:r // 2]]
        arr3 = [item[c // 2:] for item in board[r // 2:]]
        arr4 = [item[:c // 2] for item in board[r // 2:]]

        for j in range(r // 2):
            new_board[j] = arr4[j] + arr1[j]

        for j in range(r // 2, r):
            new_board[j] = arr3[j - r // 2] + arr2[j - r // 2]
        board = new_board

    elif command[i] == 6:
        r, c = len(board), len(board[0])
        new_board = [[0] * c for _ in range(r)]

        arr1 = [item[:c // 2] for item in board[:r // 2]]
        arr2 = [item[c // 2:] for item in board[:r // 2]]
        arr3 = [item[c // 2:] for item in board[r // 2:]]
        arr4 = [item[:c // 2] for item in board[r // 2:]]
        for j in range(r // 2):
            new_board[j] = arr2[j] + arr3[j]

        for j in range(r // 2, r):
            new_board[j] = arr1[j - r // 2] + arr4[j - r // 2]
        board = new_board

for arr in board:
    print(*arr)