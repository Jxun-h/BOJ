def solution(s):
    a = s.split(" ")
    answer = ""
    for step in range(len(a)):
        b = list(a[step])
        for catch in range(len(b)):
            if catch % 2 == 0:
                b[catch] = b[catch].upper()
            else:
                b[catch] = b[catch].lower()
            answer += b[catch]
        if step < len(a) - 1:
            answer += " "

    return answer