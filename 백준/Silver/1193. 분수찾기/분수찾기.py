from sys import stdin

ipt = stdin.readline

num = int(ipt().rstrip())
room_number = 0
result = 0
del_cnt = 0

while True:
    if result >= num:
        break
    else:
        room_number += 1
        result += room_number

for x in range(1, room_number):
    del_cnt += x

arr_num = num - del_cnt - 1

if room_number % 2 == 0:
    # 짝수
    print(str(1 + arr_num) + '/' + str(room_number - arr_num))
else:
    # 홀수
    print(str(room_number - arr_num) + '/' + str(1 + arr_num))

