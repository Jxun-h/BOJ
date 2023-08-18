from sys import stdin
from itertools import combinations

n = int(stdin.readline())

arr = []
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))

member = [x for x in range(n)]


team = [x for x in list(combinations(member, n // 2))]

res = 1e9

for t in range(len(team)):
    skill_team = team[t]
    link_team = tuple(set(member) - set(team[t]))

    skill_p = 0
    for i in range(n // 2):
        r = skill_team[i]
        for j in skill_team:
            skill_p += arr[r][j]

    link_p = 0
    for i in range(n // 2):
        r = link_team[i]
        for j in link_team:
            link_p += arr[r][j]

    res = min(res, abs(skill_p - link_p))

print(res)