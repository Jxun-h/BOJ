from sys import stdin

for i in range(1, int(stdin.readline()) + 1):
    res = 'Not a pangram'
    string = stdin.readline().rstrip()

    alphabet = [[False] * 26 for _ in range(3)]

    for j in string:
        idx = 0
        if not j.isalpha():
            continue
        else:
            while 1:
                if not alphabet[idx][ord(j.lower()) - 97]:
                    alphabet[idx][ord(j.lower()) - 97] = True
                    break
                else:
                    idx += 1

                if idx > 2:
                    idx = 0
                    break

    cnt = 0
    for data in alphabet:
        if False in data:
            break
        else:
            cnt += 1

    if cnt == 1:
        res = 'Pangram!'
    elif cnt == 2:
        res = 'Double pangram!!'
    elif cnt == 3:
        res = 'Triple pangram!!!'

    print('Case {}: {}'.format(i, res))