from sys import stdin

ipt = stdin.readline

num_str = check_str = ipt().rstrip()

result_str = ''
count = 0

if len(num_str) == 1:
    num_str = check_str = '0' + num_str

while check_str != result_str:
    first_num = num_str[1]
    second_num = str(int(num_str[0]) + int(num_str[1]))

    if len(second_num) > 1:
        second_num = second_num[1]

    result_str = first_num + second_num
    num_str = result_str
    count += 1

print(count)