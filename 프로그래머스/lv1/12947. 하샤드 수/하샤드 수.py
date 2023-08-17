def solution(x):

    a = list(str(x))
    r = 0
    for y in a:
        r += int(y)

    if int(x) % r == 0:
        answer = True
    else:
        answer = False

    return answer