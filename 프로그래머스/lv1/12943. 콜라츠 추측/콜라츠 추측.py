def solution(num):
    cnt = 0
    for x in range(0,500):
        if num == 1:
            return cnt

        if num % 2 == 0:
            num /= 2
            cnt += 1
        else:
            num = num * 3 + 1
            cnt += 1

    return -1