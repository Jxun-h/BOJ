from sys import stdin

while 1:
    data = stdin.readline().rstrip()
    if data == 'END':
        break
    data = data.split()

    data.reverse()

    for i in range(len(data)):
        print(data[i][::-1], end=' ')
    print()