def solution(msg):
    answer = []

    base_dict = {chr(e + 64): e for e in range(1, 27)}
    num = 27

    while msg:
        t = 1
        while msg[:t] in base_dict.keys() and t <= len(msg):
            t += 1
        t -= 1

        answer.append(base_dict[msg[:t]])
        base_dict[msg[:t + 1]] = num
        num += 1
        msg = msg[t:]

    return answer