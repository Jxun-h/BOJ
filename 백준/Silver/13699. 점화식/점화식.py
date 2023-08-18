from sys import stdin


def solutions(n):
    t = [0 for _ in range(36)]
    t[0], t[1], t[2], t[3] = 1, 1, 2, 5

    for i in range(4, 36):
        temp = 0
        if i % 2 == 0:
            for j in range(i // 2):
                temp += (t[j] * t[i-(j+1)]) * 2

        else:
            for j in range(i // 2):
                temp += (t[j] * t[i - (j+1)]) * 2
            temp += t[i // 2] ** 2

        t[i] = temp

    return t[n]


print(solutions(int(stdin.readline())))