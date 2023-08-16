from sys import stdin

temp, ans, n = '666', 0, int(stdin.readline())
while 1:
    if '666' in temp:
        ans += 1

    if ans == n:
        print(temp)
        break

    temp = str(int(temp) + 1)