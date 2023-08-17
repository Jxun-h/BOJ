def solution(a,b):
    a = sorted(a)
    b = sorted(b)
    c = len(b)-1
    answer = 0
    for x in a:
        if c >= 0:
            answer += x*b[c]
            c-=1
    return answer