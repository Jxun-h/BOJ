def solution(N, stages):
    result = []
    total = len(stages)
    for stage in range(1, N + 1):
        cnt = stages.count(stage)
        if cnt == 0 and total == 0:
            fail_per = 0
        else:
            fail_per = cnt / total

        result.append((fail_per, stage))

        total -= cnt
    result.sort(key=lambda x: (-x[0], x[1]))

    answer = [i[1] for i in result]

    return answer