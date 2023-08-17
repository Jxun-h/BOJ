from sys import stdin
for _ in range(int(stdin.readline())):
    data = stdin.readline().rstrip()
    if '=' in data:
        print('skipped')
    else:
        print(eval(data))