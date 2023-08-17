def solution(a, b):
    n = int(str(a) + str(b))
    m = int(str(b) + str(a))
    answer = n if n >= m else m
    return answer