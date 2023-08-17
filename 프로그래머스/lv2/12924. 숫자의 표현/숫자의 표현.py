def solution(n):
    cnt = 0
    a=0
    for x in range(1, n+1):
        for y in range(x, n+1):
            a += y
            if a == n:
                cnt += 1
            if a >= n:
                a=0
                break
    return cnt