from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    d = {x: x for x in list(map(int, stdin.readline().split()))}
    m = int(stdin.readline())
    for i in list(map(int, stdin.readline().split())):
        print(1 if i in d else 0)