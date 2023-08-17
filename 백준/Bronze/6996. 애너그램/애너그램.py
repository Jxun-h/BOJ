from sys import stdin

for _ in range(int(stdin.readline())):
    d = {}
    data = stdin.readline().rstrip().split()

    for i in data[1]:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    tf = True
    for i in data[0]:
        if i not in d:
            tf = False
            break

        elif i in d:
            if d[i] > 0:
                d[i] -= 1
            else:
                tf = False
                break

    if tf and sum(d.values()) == 0:
        print('{} & {} are anagrams.'.format(data[0], data[1]))
    else:
        print('{} & {} are NOT anagrams.'.format(data[0], data[1]))

