def get_calc(s):
    s = s.replace("S", "")
    s = s.replace("D", "**2")
    s = s.replace("T", "**3")

    if len(s) > 1:
        return eval(s)
    else:
        return int(s)


def solution(dartResult):
    answer = []
    stack = ''
    idx = 0

    for i in dartResult:
        if stack != '' and i.isdigit() and not stack[-1].isnumeric():
            answer.append(get_calc(stack))
            stack = '' + i


        elif i.isdigit():
            stack += i

        elif chr(96) < i.lower() < chr(123):
            stack += i

        elif i == '*':
            answer.append(get_calc(stack))
            for i in range(2):
                if idx - i < 0:
                    break
                answer[idx - i] *= 2

            stack = ''
            idx += 1

        elif i == '#':
            answer.append(get_calc(stack) * -1)
            stack = ''

        else:
            stack += i
            answer.append(get_calc(stack))
            idx += 1
            stack = ''

        idx = len(answer)
        
    if stack != '':
        answer.append(get_calc(stack))

    return sum(answer)