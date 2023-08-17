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


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))