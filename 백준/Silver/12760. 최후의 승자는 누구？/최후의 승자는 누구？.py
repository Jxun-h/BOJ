from sys import stdin

n, m = map(int, stdin.readline().split())
d = {x: 0 for x in range(1, n + 1)}
players = []
for i in range(n):
    cards = list(map(int, stdin.readline().split()))
    cards.sort()
    players.append(list(reversed(cards)))

mx = [0 for _ in range(m)]

for i in range(n):
    for j in range(m):
        mx[j] = max(mx[j], players[i][j])

for i in range(n):
    for j in range(m):
        if mx[j] == players[i][j]:
            d[i + 1] += 1

mx_cnt = max(d.values())
res = []
for key, item in d.items():
    if item == mx_cnt:
        res.append(key)
res.sort()
print(*res)