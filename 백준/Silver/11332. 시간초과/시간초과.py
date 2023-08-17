from sys import stdin

for _ in range(int(stdin.readline())):
    data = stdin.readline().rstrip().split()
    time_complexity = data[0]
    n, t, l = map(int, data[1:])
    flag = True

    if time_complexity == 'O(N)':
        big0 = n * t

    elif time_complexity == 'O(N^2)':
        big0 = (n ** 2) * t

    elif time_complexity == 'O(N^3)':
        big0 = (n ** 3) * t

    elif time_complexity == 'O(2^N)':
        big0 = (2 ** n) * t

    else:
        big0 = 1
        for i in range(n, 1, -1):
            big0 *= i
            if big0 > (10 ** 8) * l:
                flag = False
                break
        if flag:
            big0 *= t
        else:
            print('TLE!')
            continue

    if big0 > (10 ** 8) * l:
        print('TLE!')
    else:
        print('May Pass.')
