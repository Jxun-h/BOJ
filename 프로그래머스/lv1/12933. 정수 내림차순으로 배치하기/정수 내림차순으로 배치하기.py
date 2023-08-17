def solution(n):
    b = list()
    a = list(str(n))
    for x in range(len(a)):
        b.append(int(a[x]))

    b.sort()
    b.reverse()

    answer =""

    for x in range(len(b)):
        answer += str(b[x])

    return int(answer)