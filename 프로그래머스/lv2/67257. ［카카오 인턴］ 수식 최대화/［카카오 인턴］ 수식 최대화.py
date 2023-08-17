from itertools import permutations as pt


def solution(expression):
    answer = -1e9
    op, nums = [], []
    a, b = -1, -1
    new_ex = []

    for i in range(len(expression)):
        if expression[i].isnumeric():
            if a < 0:
                a = i
            else:
                b = i
        else:
            if b < 0:
                b = a

            op.append(expression[i])
            nums.append((a, b))
            new_ex.append(int(expression[a:b+1]))
            new_ex.append(expression[i])
            a, b = -1, -1
    if b > -1:
        new_ex.append(int(expression[a:b+1]))
    else:
        new_ex.append(int(expression[a]))

    k = list(set(op))
    for case in list(set(pt(k, len(k)))):
        temp_new_ex = new_ex[:]
        for j in case:
            while j in temp_new_ex:
                idx = temp_new_ex.index(j)
                if j == '*':
                    temp = temp_new_ex[idx - 1] * temp_new_ex[idx + 1]
                elif j == '-':
                    temp = temp_new_ex[idx - 1] - temp_new_ex[idx + 1]
                else:
                    temp = temp_new_ex[idx - 1] + temp_new_ex[idx + 1]

                temp_new_ex = temp_new_ex[:idx - 1] + [temp] + temp_new_ex[idx + 2:]
        answer = max(answer, abs(temp_new_ex[0]))

    return answer


# print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))