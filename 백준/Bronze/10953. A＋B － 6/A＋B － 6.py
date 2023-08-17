from sys import stdin

for _ in range(int(stdin.readline())):
    data = list(map(int, stdin.readline().split(',')))
    print(sum(data))