from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer, data, sql = [], {}, []

    n, m = len(info), len(query)

    for j in info:
        temp = j.split()
        condition = temp[:-1]
        score = int(temp[-1])

        for i in range(5):
            comb = list(combinations(range(4), i))
            for c in comb:
                test_case = condition.copy()
                for idx in c:
                    test_case[idx] = '-'
                case = ''.join(test_case)
                if case not in data:
                    data[case] = [score]
                else:
                    data[case].append(score)
    for i in data.values():
        i.sort()

    for i in range(m):
        sql = query[i].replace('and', '').split()
        test_query = ''.join(sql[:-1])
        test_score = int(sql[-1])

        if test_query in data:
            idx = bisect_left(data[test_query], test_score)
            answer.append(len(data[test_query]) - idx)
        else:
            answer.append(0)

    return answer