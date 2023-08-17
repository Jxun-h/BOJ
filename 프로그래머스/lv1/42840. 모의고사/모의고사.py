from itertools import cycle

def solution(ans):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]

    answer = []

    ac = 0
    bc = 0
    cc = 0

    for ansa, ansb, ansc, ansr in zip(cycle(a), cycle(b), cycle(c), ans):
        if ansa == ansr : ac+=1
        if ansb == ansr : bc+=1
        if ansc == ansr : cc+=1

    if ac >= bc:
        if ac >= cc:
            answer.append(1)
    if bc >= ac:
        if bc >= cc:
            answer.append(2)
    if cc >= ac:
        if cc >= bc:
            answer.append(3)

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))