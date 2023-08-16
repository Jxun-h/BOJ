from sys import stdin

n = int(stdin.readline())
h = list(map(int, stdin.readline().split()))
ans = [0] * n
for p in range(1, n+1):
    t = h[p-1]
    cnt = 0
    for i in range(n):
        if cnt == t and ans[i] == 0:
            ans[i] = p
            break
        elif ans[i] == 0:
            cnt += 1
print(*ans)