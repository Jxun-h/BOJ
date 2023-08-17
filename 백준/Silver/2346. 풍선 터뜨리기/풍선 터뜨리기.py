from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
now = 1
move = data[now - 1]
data[now - 1] = int(1e5)
print(now, end=' ')


while 1:
    if data.count(int(1e5)) == n:
        break

    if move < 0:
        temp = move * -1
        for _ in range(temp, 0, -1):
            now -= 1
            if now == 0:
                now = n

            while data[now - 1] == int(1e5):
                now -= 1
                if now == 0:
                    now = n

        print(now, end=' ')
        move = data[now - 1]
        data[now - 1] = int(1e5)

    elif move > 0:
        temp = move
        for _ in range(temp, 0, -1):
            now += 1
            if now > n:
                now = 1

            while data[now - 1] == int(1e5):
                now += 1
                if now > n:
                    now = 1

        print(now, end=' ')
        move = data[now - 1]
        data[now - 1] = int(1e5)