from sys import stdin

s = stdin.readline().rstrip().replace(' ', '')
ans = ''


def to_java(string):
    if string[0] == '_' or string[-1] == '_' or '__' in string:
        return 'Error!'

    ret = ''
    under = False

    for i in string:
        if i.isupper():
            return 'Error!'

        if i == '_':
            under = True
            continue

        if under:
            under = False
            ret += i.upper()
            continue

        ret += i

    return ret


def to_cpp(string):
    if string[0].isupper():
        return 'Error!'

    ret = ''
    for i in string:
        if i.isupper():
            ret += '_' + i.lower()

        else:
            ret += i

    return ret


if '_' in s:
    print(to_java(s))
else:
    print(to_cpp(s))