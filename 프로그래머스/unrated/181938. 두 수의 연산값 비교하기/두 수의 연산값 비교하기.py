def solution(a, b):
    n = int(str(a) + str(b))
    m = 2 * a * b
    answer = n if n >= m else m
    return answer