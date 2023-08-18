from sys import stdin
from collections import deque

n, m, k = map(int, stdin.readline().split())
arr = [[5] * (n + 1) for _ in range(n + 1)]
water = [[-1] * (n + 1)]

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(n):
    water.append([-1] + list(map(int, stdin.readline().split())))

tree_data = [[deque() for _ in range(n + 1)] for _ in range(n + 1)]
dead_trees = [[list() for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    x, y, olds = map(int, stdin.readline().rstrip().split())
    tree_data[x][y].append(olds)


def sp_sm():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            length = len(tree_data[i][j])
            for k in range(length):
                if tree_data[i][j][k] > arr[i][j]:
                    for p in range(k, length):
                        dead_trees[i][j].append(tree_data[i][j].pop())
                    break
                else:
                    arr[i][j] -= tree_data[i][j][k]
                    tree_data[i][j][k] += 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            while dead_trees[i][j]:
                arr[i][j] += (dead_trees[i][j].pop() // 2)


def fa_wi():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            length = len(tree_data[i][j])
            for k in range(length):
                if tree_data[i][j][k] % 5 == 0:
                    for p in range(8):
                        nx, ny = dx[p] + i, dy[p] + j
                        if 1 <= nx <= n and 1 <= ny <= n:
                            tree_data[nx][ny].appendleft(1)
            arr[i][j] += water[i][j]


for year in range(1, k + 1):
    # spring, summer
    sp_sm()

    # fall, winter
    fa_wi()


ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        ans += len(tree_data[i][j])

print(ans)