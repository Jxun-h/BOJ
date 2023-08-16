from sys import stdin
from collections import Counter as cc

ipt = stdin.readline

ipt_str = ipt().rstrip().lower()

cnt_dict = cc(ipt_str)
cnt_nums = list(cc(ipt_str).values())
cnt_max = max(cnt_nums)

if cc(cnt_nums)[cnt_max] >= 2:
    print('?')
else:
    print(cnt_dict.most_common(1)[0][0].upper())