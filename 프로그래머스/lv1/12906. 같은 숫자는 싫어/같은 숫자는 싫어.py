def solution(arr):
    answer = list()
    pre = -1

    for step in arr:
        if step != pre:
            answer.append(step)
            pre = step

    return answer