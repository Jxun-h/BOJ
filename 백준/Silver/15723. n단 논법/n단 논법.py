from collections import deque
from sys import stdin

n = int(stdin.readline())
d = {chr(97 + x): x for x in range(26)}
graph = [[0] * 26 for _ in range(26)]

for _ in range(n):
    a, b = map(str, stdin.readline().rstrip().split(' is '))
    a, b = d[a], d[b]
    graph[a][b] = 1


for k in range(26):
    for i in range(26):
        for j in range(26):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1


m = int(stdin.readline())
for _ in range(m):
    a, b = map(str, stdin.readline().rstrip().split(' is '))
    a, b = d[a], d[b]
    if graph[a][b]:
        print('T')
    else:
        print('F')