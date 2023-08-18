from sys import stdin
from collections import deque


def solution(s):
    answer = ''
    q = deque(list(s + ' '))
    f = 0
    temp = ''

    while q:
        k = q.popleft()

        if k == '>':
            f = 0
            answer += k
            continue

        if k == '<':
            f = 1
            if temp != '':
                answer += temp[::-1]
                temp = ''

        if f == 1:
            answer += k
            continue

        if k == ' ':
            answer += temp[::-1] + ' '
            temp = ''
            continue

        temp += k
    return answer


print(solution(stdin.readline().rstrip()))