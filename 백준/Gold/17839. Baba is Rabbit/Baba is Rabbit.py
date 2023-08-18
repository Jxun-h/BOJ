from collections import deque
from sys import stdin

graph = {}
for _ in range(int(stdin.readline())):
    a, b = stdin.readline().rstrip().split(' is ')
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)


def solve():
    q = deque()
    q.append("Baba")
    visited = {}
    while q:
        now = q.popleft()

        try:
            for i in graph[now]:
                if i not in visited:
                    visited[i] = 1
                    q.append(i)
        except:
            pass

    return visited


try:
    ans = sorted(solve())
    print(*ans, sep='\n')

except:
    pass
