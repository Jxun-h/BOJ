from sys import stdin

for tc in range(int(stdin.readline())):
    stick_length, ant = map(int, stdin.readline().split())
    ans = [[], []]

    for _ in range(ant):
        pos = int(stdin.readline())

        data = stick_length - pos
        if data > stick_length // 2:
            ans[1].append(data)
            ans[0].append(stick_length - data)

        elif data < stick_length // 2:
            ans[0].append(data)
            ans[1].append(stick_length - data)
        
        else:
            ans[0].append(data)
            ans[1].append(data)

    print(max(ans[0]), max(ans[1]))
