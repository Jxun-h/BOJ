def solution(n):
    answer = list()
    a = list(str(n))
    for x in range(len(a)-1, -1, -1):
        answer.append(int(a[x]))

    return answer