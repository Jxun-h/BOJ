def solution(a, b):
    month = 0

    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for mon_step in range(a-1):
        month += mon[mon_step]

    month += b

    step = month % 7 -1

    return day[step]

print(solution(5, 24))
