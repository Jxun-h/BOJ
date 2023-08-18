from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6
                  )
n, m = map(int, stdin.readline().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)


def solve(start, cnt):
    visited[start] = True

    if cnt > 3:
        print(1)
        exit()

    for i in arr[start]:
        if not visited[i]:
            solve(i, cnt + 1)
            visited[i] = False

    return False


tf = False
for i in range(n):
    visited = [False] * n
    res = solve(i, 0)
    visited[i] = False

print(0)