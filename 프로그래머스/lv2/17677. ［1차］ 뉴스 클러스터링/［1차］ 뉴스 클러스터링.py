def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    n = len(str1)
    m = len(str2)

    s1_list, s2_list = [], []

    for i in range(n - 1):
        if str1[i:i + 2].isalpha():
            s1_list.append(str1[i:i + 2])

    for j in range(m - 1):
        if str2[j:j + 2].isalpha():
            s2_list.append(str2[j:j + 2])

    total = len(s1_list) + len(s2_list)
    intersect = 0
    if total == 0:
        return 65536

    for i in s2_list:
        if i in s1_list:
            intersect += 1
            s1_list.remove(i)

    return int((intersect / (total - intersect)) * 65536)