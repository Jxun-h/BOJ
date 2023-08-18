from sys import stdin

n, q = map(int, stdin.readline().split())

arr = [1 for _ in range(n + 1)]

for i in range(q):
    k = int(stdin.readline())
    meet_land = 0
    temp = k

    while temp != 1:
        if not arr[temp]:
            meet_land = temp

        temp //= 2

    if meet_land == 0:
        arr[k] = 0

    print(meet_land)