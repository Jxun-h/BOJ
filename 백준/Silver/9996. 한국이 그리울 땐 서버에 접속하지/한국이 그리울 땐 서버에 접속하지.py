from sys import stdin

n = int(stdin.readline())
pattern = stdin.readline().rstrip()


def match_tf(p, s):
    p = p.split('*')
    start_m, end_m = p[0], p[1]
    if s[:len(start_m)] == start_m and s[-len(end_m):] == end_m and len(''.join(p)) <= len(s):
        return True
    return False


for _ in range(n):
    string = stdin.readline().rstrip()
    if match_tf(pattern, string):
        print('DA')
    else:
        print('NE')
