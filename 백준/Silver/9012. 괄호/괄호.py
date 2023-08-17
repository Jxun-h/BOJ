from sys import stdin


def check(str):
    cnt = 0
    for i in str:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False

    if cnt == 0:
        return True
    else:
        return False


for _ in range(int(stdin.readline())):
    if check(list(stdin.readline().rstrip())):
        print('YES')
    else:
        print('NO')