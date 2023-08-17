from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    route = []
    x, y = 0, 0

    while x < n:
        if x % 2 == 0:
            for j in range(y, m):
                route.append((x, j))
            y = m - 1
            x += 1
        else:
            limit = -1 if x == n - 1 else 0

            for j in range(y, limit, -1):
                route.append((x, j))
            x += 1
            y = 1

    start = n - 2 if n % 2 == 0 else n - 1
    for i in range(start, 0, -1):
        route.append((i, 0))

    print(1)
    print(*route, sep='\n')