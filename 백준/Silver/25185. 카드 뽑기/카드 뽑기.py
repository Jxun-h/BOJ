from sys import stdin
from itertools import combinations


def check(data):
    for temp in combinations(data, 3):
        if (temp[0][1] == temp[1][1] == temp[2][1]) and (temp[0][0] == temp[1][0] - 1 == temp[2][0] - 2):
            return ':)'

    for d in set(data):
        if data.count(d) == 3:
            return ':)'

    data_set = {0, 1, 2, 3}
    for temp in combinations(data_set, 2):
        t1_a, t1_b = temp
        t2_a, t2_b = (data_set - set(temp))
        if data[t1_a] == data[t1_b] and data[t2_a] == data[t2_b]:
            return ':)'

    return ':('


t = int(stdin.readline())
for _ in range(t):
    temp = stdin.readline().split()
    data = []
    for t1, t2 in temp:
         data.append((int(t1), t2))

    data.sort()

    print(check(data))