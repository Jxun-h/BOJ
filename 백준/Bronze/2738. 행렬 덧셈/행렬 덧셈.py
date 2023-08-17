from sys import stdin
n, m = map(int, stdin.readline().split())
answer = []

for i in range(n):
    answer.append(list(map(int, stdin.readline().split())))

for i in range(n):
    temp = list(map(int, stdin.readline().split()))
    for j in range(m):
        answer[i][j] += temp[j]
for i in answer:
    print(*i)