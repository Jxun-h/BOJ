from collections import deque
def solution(n, s, a, b, fares):
    answer = int(1e9)
    INF = int(1e9)
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    for q, w, e in fares:
        distance[q][w] = e
        distance[w][q] = e
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    distance[i][j] = 0
                else:
                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
                    
    for i in range(1, n + 1):
        if answer > distance[s][i] + distance[i][b] + distance[i][a]:
            answer = distance[s][i] + distance[i][b] + distance[i][a]
    return answer