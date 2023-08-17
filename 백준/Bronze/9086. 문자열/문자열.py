from sys import stdin

for _ in range(int(stdin.readline())):
    data = stdin.readline().rstrip()
    if len(data) == 1:
        print(data * 2)
    else:
        print(data[0] + data[-1])