from sys import stdin

n, m, s = map(int, stdin.readline().split())
time_table = []

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    time_table.append((a, b))

time_table.sort()


def check1():
    for i in range(n - 1):
        data = sum(time_table[i])
        if time_table[i + 1][0] - data >= m:
            return data
    return -1


def check2():
    data = sum(time_table[-1])
    if data + m <= s:
        return data
    return -1


if time_table[0][0] >= m:
    print(0)
    exit()

res = check1()
if res != -1:
    print(res)
    exit()

res = check2()
if res != -1:
    print(res)
    exit()

print(-1)