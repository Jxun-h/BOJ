from sys import stdin

n = int(stdin.readline())
max_pillar = -1e9
idx = 0
arr = [[] for _ in range(1001)]
res = 0
last_idx = 0

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    if max_pillar < b:
        max_pillar = b
        idx = a

    arr[a].append(b)
    last_idx = max(last_idx, a)

part1 = arr[:idx+1]
part2 = arr[idx+1:last_idx+1]

now = 0
for i in part1:
    if not i:
        res += now
    else:
        if now > i[0]:
            res += now
        else:
            now = i[0]
            res += now

part2.reverse()
now = 0
for i in part2:
    if not i:
        res += now
    else:
        if now > i[0]:
            res += now
        else:
            now = i[0]
            res += now

print(res)