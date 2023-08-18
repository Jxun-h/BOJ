import sys

input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    alphabet_cnt = {chr(97 + x): 0 for x in range(26)}

    alphabet_idx = {chr(97 + x): [] for x in range(26)}

    str_arr = input()
    k = int(input())

    min_length = 1e12
    max_length = -1
    cnt = 0

    for i in str_arr[:-1]:
        alphabet_idx[i].append(cnt)
        alphabet_cnt[i] += 1
        cnt += 1

    alphabet_candidate = [chr(97 + x) for x in range(26)]

    for key, val in alphabet_cnt.items():

        if val < k:
            alphabet_candidate.remove(key)

    if len(alphabet_candidate) == 0:
        print(-1)
    else:
        for i in alphabet_candidate:
            temp = 0
            for j in range(0, len(alphabet_idx[i]) - k + 1):
                temp = alphabet_idx[i][j + k - 1] - alphabet_idx[i][j] + 1
                if temp > max_length and str_arr[alphabet_idx[i][j + k - 1]] == str_arr[alphabet_idx[i][j]]:
                    max_length = temp

                if temp < min_length:
                    min_length = temp

        print(min_length, max_length)
