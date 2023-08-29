from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, c, d = map(int, stdin.readline().split());

    if c * d > a * b:
        print("Eurecom")
    elif c * d < a * b:
        print("TelecomParisTech")
    else:
        print("Tie")
