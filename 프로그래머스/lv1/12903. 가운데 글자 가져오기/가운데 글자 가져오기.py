def solution(s):
    answer = list(s)

    len_check = len(answer) % 2
    step = int(len(answer) / 2)

    if len_check == 0:
        result = answer[step-1]
        result += answer[step]
    else:
        result = answer[step]
    return result


print(solution("abcde"))
print(solution("qwer"))