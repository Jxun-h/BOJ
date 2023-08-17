def solution(n):
    s = [True] * n  # n 개의 True 배열을 생성
    s[0] = False
    s[1] = False
    m = int(n ** 0.5)

    for x in range(2, m + 1):
        if s[x] == True:
            for k in range(x + x, n, x):
                s[k] = False
                # print(k)

    if n < 6!= 0:
        return len([x for x in range(2, n) if s[x] == True]) + 1
    else:
        return len([x for x in range(2, n) if s[x] == True])