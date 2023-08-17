from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
data.sort()

ans, res = [0] * 3, float('inf')

for i in range(n - 2):
    m = data[i]
    if i > 0 and data[i] == data[i - 1]:
        continue

    start, end = i + 1, n - 1
    while start < end:
        value = m + data[start] + data[end]
        if abs(value) < abs(res):
            ans[0], ans[1], ans[2] = m, data[start], data[end]
            res = value

        if value < 0:
            start += 1

        elif value > 0:
            end -= 1

        else:
            print(ans[0], ans[1], ans[2])
            exit()

print(ans[0], ans[1], ans[2])