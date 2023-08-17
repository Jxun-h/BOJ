def solution(s):
    x = s.split(' ')
    answer = ''
    b = []
    for i in range(1):
        for k in x:
            b.append(int(k))
        answer = str(min(b))+" "
        answer += str(max(b))
    return answer