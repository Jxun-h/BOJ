from sys import stdin

a, b, c = [False for _ in range(15)], [False for _ in range(30)], [False for _ in range(30)]
n = int(stdin.readline())
res = 0


def dfs(x):
    global res
    if x == n:
        res += 1
        return

    for y in range(n):
        if a[y] or b[x + y] or c[x + (n - y)]:
            continue

        a[y] = True
        b[x + y] = True
        c[x + (n - y)] = True

        dfs(x + 1)

        a[y] = False
        b[x + y] = False
        c[x + (n - y)] = False


dfs(0)
print(res)
