from sys import stdin
ipt = stdin.readline

step_num = int(ipt().rstrip())
# 개수 체크
cnt = 0

for x in range(step_num):
    check = True
    input_str = ipt().rstrip()

    if len(input_str) > len(set(input_str)):
        for step in set(input_str):
            cnt_num_in_str = input_str.count(step)

            if cnt_num_in_str > 1:
                str_group = ''

                for step2 in range(cnt_num_in_str):
                    str_group += step

                if str_group not in input_str:
                    check = False
                    break
            else:
                continue
        if check:
            cnt += 1
    else:
        cnt+=1

print(cnt)