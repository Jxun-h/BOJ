from sys import stdin

for _ in range(int(stdin.readline())):

    a = list(map(int, stdin.readline().split()))[1:]
    b = list(map(int, stdin.readline().split()))[1:]

    _4a, _4b = a.count(4), b.count(4)
    if _4a == _4b:
        _3a, _3b = a.count(3), b.count(3)
        if _3a == _3b:
            _2a, _2b = a.count(2), b.count(2)
            if _2a == _2b:
                _1a, _1b = a.count(1), b.count(1)
                if _1a == _1b:
                    print('D')
                else:
                    print('A') if _1a > _1b else print('B')
            else:
                print('A') if _2a > _2b else print('B')
        else:
            print('A') if _3a > _3b else print('B')
    else:
        print('A') if _4a > _4b else print('B')