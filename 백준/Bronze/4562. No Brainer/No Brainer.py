from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    if a >= b:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")