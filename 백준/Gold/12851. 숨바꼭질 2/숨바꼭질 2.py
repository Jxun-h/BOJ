from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().split())
res = []


def solve():
    q = deque()
    q.append(n)

    if n == k:
        return 0, 1

    if n > k:
        return n - k, 1

    q, visited, ways = deque([n]), [float('inf')] * 100001, [0] * 100001
    time, count, success = 0, 0, False

    ways[n] = 1
    visited[n] = 0

    while q and not success:
        size = len(q)

        for _ in range(size):
            cur = q.popleft()

            for next_mv in (cur - 1, cur + 1, cur * 2):
                if -1 < next_mv < 100001 and time + 1 <= visited[next_mv]:
                    ways[next_mv] += 1
                    visited[next_mv] = time + 1

                    if next_mv == k:
                        success = True

                    if not success:
                        q.append(next_mv)
        time += 1

    return visited[k], ways[k]


time, count = solve()
print('{}\n{}'.format(time, count))