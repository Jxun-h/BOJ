from sys import stdin

n, q = map(int, stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().split()))
shift = 0

for _ in range(q):
    query = list(map(int, stdin.readline().split()))

    if query[0] == 1:
        i, x = query[1] - 1, query[2]
        arr[(i + shift) % n] += x

    elif query[0] == 3:
        shift = (shift + query[1]) % n

    elif query[0] == 2:
        shift = (shift + n - query[1]) % n


for i in range(n):
    print(arr[(shift + i) % n], end=' ')