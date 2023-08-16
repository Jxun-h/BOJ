from sys import stdin

n, m = map(int, stdin.readline().split())
trues = set(list(map(int, stdin.readline().split()))[1:])
party = []
cnt = []

for _ in range(m):
    data = set(map(int, stdin.readline().split()[1:]))
    if data:
        party.append(data)
        cnt.append(1)

for _ in range(m):
    for i, p in enumerate(party):
        if trues & p:
            cnt[i] = 0
            trues |= p

print(sum(cnt))