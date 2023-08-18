from sys import stdin

n = int(stdin.readline())
file_name = {}
for i in range(n):
    data = stdin.readline().rstrip().split('.')
    if data[1] in file_name:
        file_name[data[1]] += 1
    else:
        file_name[data[1]] = 1

res = []
for key, item in file_name.items():
    res.append((key, item))

res.sort()
for i in res:
    print(*i)