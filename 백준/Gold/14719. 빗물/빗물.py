from sys import stdin
h, w = map(int, stdin.readline().split())


def solution(h, w):
    answer = 0
    data = list(map(int, stdin.readline().split()))
    for i in range(w):
        left = max(data[:i + 1])
        right = max(data[i:])

        low = min(left, right)

        answer += abs(data[i] - low)
    return answer


print(solution(h, w))

