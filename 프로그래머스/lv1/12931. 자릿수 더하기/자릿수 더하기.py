def solution(n):
    a = list(str(n))
    answer = 0
    for step in a:
        answer += int(step)

    return answer