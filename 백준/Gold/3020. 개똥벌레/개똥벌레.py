from sys import stdin

n, h = map(int, stdin.readline().split())
wall_s = [0] * (h + 1)
wall_j = [0] * (h + 1)
ans = [n, 0]

for i in range(n):
    if i % 2 == 0:
        wall_s[int(stdin.readline())] += 1
    else:
        wall_j[int(stdin.readline())] += 1


for i in range(h - 1, -1, -1):
    wall_s[i] += wall_s[i + 1]
    wall_j[i] += wall_j[i + 1]


for i in range(1, h + 1):
    if ans[0] > (wall_s[i] + wall_j[h - i + 1]):
        ans[0] = (wall_s[i] + wall_j[h - i + 1])
        ans[1] = 1
    elif ans[0] == (wall_s[i] + wall_j[h - i + 1]):
        ans[1] += 1

print(*ans)