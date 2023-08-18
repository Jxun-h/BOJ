from sys import stdin


def get_pi(arr, p):
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = arr[j - 1]
        if p[i] == p[j]:
            j += 1
            arr[i] = j
    return arr


def solution(s, p):
    n, m = len(s), len(p)
    pi = get_pi([0 for _ in range(m)], p)
    j = 0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == m -1:
                return 1
            else:
                j += 1
    return 0


s, p = stdin.readline().rstrip(), stdin.readline().rstrip()
print(solution(s, p))