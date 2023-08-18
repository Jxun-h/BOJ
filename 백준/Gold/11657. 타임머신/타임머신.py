from sys import stdin

n, m = map(int, stdin.readline().split())
inf = int(1e9)
edges = []
distance = [inf] * (n + 1)

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    edges.append((a, b, c))


def be_f(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if distance[node] != inf and distance[next_node] > distance[node] + cost:
                distance[next_node] = distance[node] + cost
                if i == n - 1:
                    return True
    return False


cycle = be_f(1)
if cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if distance[i] == inf:
            print(-1)
        else:
            print(distance[i])