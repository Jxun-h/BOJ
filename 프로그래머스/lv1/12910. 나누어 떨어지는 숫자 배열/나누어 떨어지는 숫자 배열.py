def solution(arr, divisor):

    if len(list(x for x in arr if x % divisor == 0)):
        answer = list(x for x in arr if x % divisor == 0)
    else:
        answer = [-1]

    answer.sort()

    return answer