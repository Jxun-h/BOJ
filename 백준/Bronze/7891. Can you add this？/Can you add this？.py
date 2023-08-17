from sys import stdin

for _ in range(int(stdin.readline())):
    print(sum(list(map(int, stdin.readline().split()))))
