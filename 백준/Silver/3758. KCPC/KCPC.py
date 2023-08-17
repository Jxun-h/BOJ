from sys import stdin

for _ in range(int(stdin.readline())):
    n, k, t, m = map(int, stdin.readline().split())

    teams = {x: {y: [0, 0, 0] for y in range(1, k + 1)} for x in range(1, n + 1)}
    answer = []

    for p in range(1, m + 1):
        i, j, s = map(int, stdin.readline().split())
        teams[i][j][0] = max(teams[i][j][0], s)
        teams[i][j][1] += 1
        teams[i][j][2] = p

    for team_num, t_data in teams.items():
        p_total, p_sub, last_sub = 0, 0, 0
        for p_num, p_data in t_data.items():
            p_total += p_data[0]
            p_sub += p_data[1]
            last_sub = max(last_sub, p_data[2])

        answer.append((p_total, p_sub, last_sub, team_num))

    answer.sort(key=lambda x: (-x[0], x[1], x[2]))

    for i in range(n):
        if answer[i][3] == t:
            print(i + 1)
            break
