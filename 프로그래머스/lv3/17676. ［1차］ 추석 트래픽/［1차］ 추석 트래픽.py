def get_value(start, times):
    res = 0
    end = start + 1000 - 1
    for time in times:
        if start <= time[1] and end >= time[0]:
            res += 1
    return res


def solution(lines):
    times = []

    answer = 0

    for t in lines:
        arr = t.split()
        tmp = list(map(float, arr[1].split(':')))
        complete_time = tmp[0] * 3600 * 1000 + tmp[1] * 60 * 1000 + tmp[2] * 1000
        start_time = complete_time - (float(arr[2][:-1]) * 1000) + 1
        times.append((start_time, complete_time))

    for time in times:
        start, end = time
        answer = max(get_value(start, times), answer)
        answer = max(get_value(end, times), answer)

    return answer