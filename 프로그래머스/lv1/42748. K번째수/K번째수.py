def solution(array, commands):

    answer = []

    for step in commands:
        start = step[0] - 1
        end = step[1]
        idx = step[2] - 1

        tmp_arr = sorted(array[start:end])

        answer.append(tmp_arr[idx])

    return answer