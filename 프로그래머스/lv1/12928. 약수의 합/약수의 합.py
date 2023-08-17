def solution(n):
    answer = 0
    a = [x for x in range(1, n+1) if n % x == 0]
    for x in a: answer += int(x)
    return answer


print(solution(12))