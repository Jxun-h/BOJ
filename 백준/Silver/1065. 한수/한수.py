from sys import stdin

def solve():
    ipt = stdin.readline
    num = int(ipt().rstrip())
    cnt = 0
    for step in range(1, num+1):
        if len(str(step)) == 1:
            cnt+=1

        elif len(str(step)) == 2:
            cnt+=1

        else:
            num_str = list(str(step))
            x = int(num_str[0])-int(num_str[1])
            y = int(num_str[1])-int(num_str[2])

            if x == y:
                cnt+=1

    return cnt


print(solve())