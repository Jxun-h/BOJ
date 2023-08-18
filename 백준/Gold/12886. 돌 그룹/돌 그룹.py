from collections import deque
from sys import stdin

a, b, c = map(int, stdin.readline().split())
visited = [[0] * 1501 for _ in range(1501)]


def solve(a, b, c):
    sum_val = a + b + c

    if sum_val % 3 != 0:
        return 0

    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        a, b = q.popleft()
        temp_res = [a, b, sum_val - a - b]

        for i in range(3):
            for j in range(3):
                if temp_res[i] < temp_res[j]:
                    num1 = temp_res[i] * 2
                    num2 = temp_res[j] - temp_res[i]

                    if not visited[num1][num2]:
                        visited[num1][num2] = 1
                        q.append((num1, num2))

    return visited[sum_val//3][sum_val//3]


print(solve(a, b, c))