from sys import stdin

r, c, q = map(int, stdin.readline().split())
pic = [[0] * (c + 1)]
for i in range(r):
    sum_list = [0]
    data = list(map(int, stdin.readline().split()))
    sum_list.append(data[0])
    for i in range(1, c):
        sum_list.append(sum_list[-1] + data[i])
    pic.append(sum_list)

for _ in range(q):
    a, b, c, d = map(int, stdin.readline().split())
    addr = [(a, b), (c, d)]
    addr.sort(key=lambda x: x[0])
    res = 0

    knife = (abs(addr[0][0]-addr[1][0]) + 1) * (abs(addr[0][1]-addr[1][1]) + 1)
    for i in range(addr[0][0], addr[1][0] + 1):
        res += pic[i][addr[1][1]] - pic[i][addr[0][1] - 1]

    print(res // knife)