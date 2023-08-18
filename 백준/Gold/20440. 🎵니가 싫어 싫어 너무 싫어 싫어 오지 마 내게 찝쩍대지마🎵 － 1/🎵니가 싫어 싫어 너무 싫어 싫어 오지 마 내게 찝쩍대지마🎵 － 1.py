from sys import stdin

n = int(stdin.readline())
time = []
time_set = set()
time_set.add(-1)

for i in range(n):
    s, e = map(int, stdin.readline().split())
    time.append((s, e))
    time_set.update([s, e])

d = {}
cnt = 0
time_set = list(time_set)
time_set.sort()
for i in time_set:
    d[i] = cnt
    cnt += 1

prefix = [0 for _ in range(len(time_set) + 1)]

for s, e in time:
    prefix[d[s]] += 1
    prefix[d[e]] -= 1

max_val = 0

for i in range(1, len(time_set)):
    prefix[i] = prefix[i] + prefix[i - 1]
    if prefix[i] > max_val:
        max_val = prefix[i]

print(max_val)
ans = [0, 0]
tf = False
for i in range(len(time_set) + 1):
    if prefix[i] == max_val and not tf:
        ans[0] = time_set[i]
        tf = True

    if prefix[i] != max_val and tf:
        ans[1] = time_set[i]
        break

print(*ans)