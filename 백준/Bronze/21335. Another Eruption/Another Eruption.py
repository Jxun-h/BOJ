# from sys import stdin
#
#
# def prime_list(n):
#     sieve = [False, False] + [True] * n
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i]:
#             for j in range(i + i, n, i):
#                 sieve[j] = False
#
#     return sieve
#
#
# prime_nums = prime_list(10 ** 6)
#
# for _ in range(int(stdin.readline())):
#     cnt = 0
#     num = int(stdin.readline())
#     for i in range((num // 2) + 1):
#         if prime_nums[i] and prime_nums[num - i]:
#             cnt += 1
#
#     print(cnt)
#
#
#

from sys import stdin
from math import sqrt

pi = PI = 3.14159265359
a = int(stdin.readline())
print('%.7lf' % (sqrt(a / pi) * 2 * pi))
