from sys import stdin

n, m, k = map(int, stdin.readline().split())
ind = [0 for _ in range(n + 1)]
build = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    ind[b] += 1

for _ in range(k):
    command, structure = map(int, stdin.readline().split())
    if command == 1:
        if ind[structure] > 0:
            print('Lier!')
            exit()
        build[structure] += 1
        if build[structure] == 1:
            for i in graph[structure]:
                ind[i] -= 1

    elif command == 2:
        if build[structure] <= 0:
            print('Lier!')
            exit()
        else:
            build[structure] -= 1
            if build[structure] == 0:
                for i in graph[structure]:
                    ind[i] += 1

print('King-God-Emperor')