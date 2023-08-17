from sys import stdin

n = int(stdin.readline())
graph = []
result = 0
cursor = 0
a = 0

for _ in range(n):
    graph.append(int(stdin.readline()))
    
graph.append(0)
stack = [(0, graph[0])]

for i in range(1, n + 1):
    cursor = i
    while stack and stack[-1][1] > graph[i]:
        cursor, height = stack.pop()

        # (i - cursor) = 가로 길이
        # height = 높이
        result = max(result, height * (i - cursor))
    stack.append((cursor, graph[i]))

print(result)