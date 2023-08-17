def solution(s):

    a = list(s)
    a.sort(reverse=True)
    answer = ""
    for x in a:
        answer += x
    return answer


print(solution("Zbcdefg"))