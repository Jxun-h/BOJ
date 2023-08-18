from sys import stdin

n = int(stdin.readline())
arr = []

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    arr.append((x, y))


def solve(color, idx):
    min_cost = int(1e9)
    for t_idx, t_color in arr:
        if t_idx != idx and t_color == color:
            if abs(idx - t_idx) < min_cost:
                min_cost = abs(idx - t_idx)
                return min_cost


res = 0
for idx, color in arr:
    if color != 0:
        res += solve(color, idx)
print(res)
