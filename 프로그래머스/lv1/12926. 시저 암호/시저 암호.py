def solution(s, n):
    a = [ord(x) for x in s]
    answer = ''


    n = n%26
    for x in a:
        if 97 <= x <= 122:
            if x + n > 122:
                answer += chr(x - 26 + n)
            else:
                answer += chr(x + n)
        elif 65 <= x <= 90:
            if x + n > 90:
                answer += chr(x - 26 + n)
            else:
                answer += chr(x + n)
        else :
            answer += chr(x)
    return answer