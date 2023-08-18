from sys import stdin

for _ in range(int(stdin.readline())):
    for i in range(int(stdin.readline())):
        a, b = map(int, stdin.readline().split())
        print(a + b, a * b)
