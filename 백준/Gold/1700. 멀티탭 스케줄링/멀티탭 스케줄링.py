from sys import stdin

n, m = map(int, stdin.readline().split())
electronics = list(map(int, stdin.readline().split()))
plug, ans = [], 0

for i in range(m):
    if electronics[i] in plug:
        continue

    if len(plug) < n:
        plug.append(electronics[i])
        continue

    indexs = []
    for j in range(n):
        try:
            idx = electronics[i:].index(plug[j])
        except:
            idx = 101

        indexs.append(idx)

    pull_out = indexs.index(max(indexs))
    del plug[pull_out]
    plug.append(electronics[i])
    ans += 1

print(ans)