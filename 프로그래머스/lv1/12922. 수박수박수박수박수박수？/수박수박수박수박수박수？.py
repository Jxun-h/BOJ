def solution(n):
    answer = ''
    for step in range(n):
        if step % 2==0:
            answer += '수'
        else:
            answer += '박'

    return answer