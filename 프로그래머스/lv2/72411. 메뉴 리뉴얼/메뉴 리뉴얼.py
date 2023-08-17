from itertools import combinations


def solution(orders, course):
    answer = []
    score = {}
    n = len(orders)
    for i in range(n):
        data = sorted(list(orders[i]))
        for j in course:
            for k in list(set(combinations(data, j))):
                t = ''.join(k)
                if t in score:
                    score[t] += 1
                else:
                    score[t] = 1

    new_score = []
    for menu, num in score.items():
        if num > 1:
            new_score.append((menu, num))

    new_score.sort(key=lambda x: -x[1])

    for i in course:
        max_order = 0
        for c, num in new_score:
            if len(c) == i:
                if max_order <= num:
                    max_order = num
                    answer.append(c)
                else:
                    break
    answer.sort()
    return answer


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))