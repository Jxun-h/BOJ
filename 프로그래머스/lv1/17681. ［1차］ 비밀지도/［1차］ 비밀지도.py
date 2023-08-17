def solution(n, arr1, arr2):
    answer = []
    _1map = []
    _2map = []

    for i, j in zip(arr1, arr2):
        c = bin(i)[2:]
        s = bin(j)[2:]

        if len(c) < n:
            _1map.append(list(('0' * (n - len(c)) + c).replace('1', '#')))
        else:
            _1map.append(list(c.replace('1', '#')))

        if len(s) < n:
            _2map.append(list(('0' * (n - len(s)) + s).replace('1', '#')))
        else:
            _2map.append(list(s.replace('1', '#')))

    for i in range(n):
        st = ''
        for j in range(n):
            if _1map[i][j] != '0' or _2map[i][j] != '0':
                st += '#'
            else:
                st += ' '

        answer.append(st)

    return answer