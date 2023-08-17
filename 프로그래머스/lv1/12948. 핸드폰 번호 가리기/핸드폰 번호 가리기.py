def solution(phone_number):
    a = list(phone_number)
    b = ['*'] * len(a[:-4])
    b += a[-4:]
    answer = ""
    for x in b:
        answer += x
    return answer