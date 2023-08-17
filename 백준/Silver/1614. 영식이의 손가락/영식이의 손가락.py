from sys import stdin

hurt_finger = int(stdin.readline())
heart = int(stdin.readline())
answer = 0
flag = 1

if hurt_finger == 1:
    answer = 8 * heart
    print(answer)
    flag = 0

elif hurt_finger == 2:
    a, b = 6, 2

elif hurt_finger == 3:
    answer += 2 + heart * 4
    print(answer)
    flag = 0

elif hurt_finger == 4:
    a, b = 2, 6

elif hurt_finger == 5:
    answer += 4
    answer += heart * 8
    print(answer)
    flag = 0


if flag:
    if heart % 2 != 0:
        temp = heart // 2 + 1
        answer += (hurt_finger - 1) + temp * a + (heart - temp) * b

    else:
        temp = heart // 2
        answer += (hurt_finger - 1) + temp * a + temp * b

    print(answer)