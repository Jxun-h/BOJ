from sys import stdin

g = stdin.readline().rstrip()
cnt = 0


def solve(s):
    global cnt
    temp = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ')':
            temp += 1
        else:
            if temp - 1 < 0:
                cnt += 1
            else:
                temp -= 1

    if temp != 0:
        cnt += temp


solve(g)
print(cnt)
