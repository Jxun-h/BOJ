from sys import stdin

key = [0] + list(stdin.readline().rstrip())
angel = [0] + list(stdin.readline().rstrip())
devil = [0] + list(stdin.readline().rstrip())
dp = [[0 for _ in range(len(angel))] for _ in range(2)]
answer = 0
dp[0][0], dp[1][0] = 1, 1


def find_path(x, y):
    temp, b = 0, ''
    if x == devil:
        b = angel
    else:
        b = devil

    if x[j] == key[i]:
        for k in range(j - 1, -1, -1):
            if b[k] == key[i - 1]:
                temp += dp[y][k]
        dp[not y][j] = temp
        if i == len(key) - 1:
            global answer
            answer += temp


for i in range(1, len(key)):
    for j in range(len(devil) - 1, -1, -1):
        find_path(angel, 1)
        find_path(devil, 0)

print(answer)