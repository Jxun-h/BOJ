from sys import stdin
inp = stdin.readline
node = 1
graph = [[] for _ in range(101)]
arr = [[]]


for _ in range(int(inp())):
    s, a, b = map(int, inp().split())

    if s == 1:
        j = len(arr)
        arr.append((a, b))

        for i in range(1, len(arr)):
            if (arr[i][0] < a < arr[i][1]) or (arr[i][0] < b < arr[i][1]):
                graph[j].append(i)

            if (a < arr[i][0] < b) or (a < arr[i][1] < b):
                graph[i].append(j)

    else:
        visited = [1 for _ in range(101)]
        visited[a] = 0
        stack = [a]
        tf = False

        while stack:
            now = stack.pop()

            if now == b:
                tf = True
                break

            for node in graph[now]:
                if visited[node]:
                    stack.append(node)
                    visited[node] = 0

        print(1 if tf else 0)