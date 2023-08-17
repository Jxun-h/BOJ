def sep_tuple(s):
    txt = s.replace('{{', '{').replace('}}', '}')
    res = []
    tmp = []
    num = ''

    ans = []

    for k in range(len(txt)):
        if txt[k] == '{':
            num = ''

        if txt[k].isnumeric():
            num += txt[k]

        if txt[k] == ',' and txt[k + 1] != '{':
            tmp.append(int(num))
            num = ''

        if txt[k] == '}':
            if num != '':
                tmp.append(int(num))

            res.append(tmp)
            tmp = []

    res.sort(key=lambda x: len(x))
    for r in res:
        for j in r:
            if j not in ans:
                ans.append(j)
    return ans


def solution(s):
    answer = sep_tuple(s)
    return answer