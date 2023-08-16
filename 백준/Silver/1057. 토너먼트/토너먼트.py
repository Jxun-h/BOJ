from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

data = list(map(int, stdin.readline().split()))
team = [0 for _ in range(1, data[0] + 1)]
for i in data[1:]:
    team[i - 1] = 1


def solve(round, length):
    global team
    temp = []
    for i in range(0, length // 2 * 2, 2):
        t1, t2 = i, i + 1
        if team[t1] and team[t2]:
            return round
        elif team[t1] or team[t2]:
            temp.append(1)
        else:
            temp.append(0)

    if length % 2 != 0:
        temp.append(team[-1])

    team = temp[:]

    if length % 2 != 0:
        return solve(round + 1, length // 2 + 1)
    else:
        return solve(round + 1, length // 2)


print(solve(1, data[0]))
