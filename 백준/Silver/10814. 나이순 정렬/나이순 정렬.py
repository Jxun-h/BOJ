from sys import stdin

arr = []
for i in range(int(stdin.readline())):
    a, b = stdin.readline().rstrip().split()
    a = int(a)

    arr.append((a, b, i))

arr.sort(key=lambda x: (x[0], x[2]))
for i in arr:
    print(i[0], i[1])