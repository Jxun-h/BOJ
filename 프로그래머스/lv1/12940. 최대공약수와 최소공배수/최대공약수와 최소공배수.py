def solution(n, m):
    gy = 1
    gb = 1
    for step in range(max(n,m), 1000000):
        if (step % n == 0) and (step % m == 0):
            gb = step
            break

    for step in range(max(n,m), 1, -1):
        if (n % step == 0) and (m % step == 0):
            gy = step
            break

    answer = [gy, gb]

    return answer