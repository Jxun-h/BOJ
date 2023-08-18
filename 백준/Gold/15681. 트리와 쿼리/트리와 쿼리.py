from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 9)

n, r, queue = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]
count = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def solve(x):
    count[x] = 1
    for i in graph[x]:
        if not count[i]:
            solve(i)
            count[x] += count[i]


solve(r)

for _ in range(queue):
    print(count[int(stdin.readline())])