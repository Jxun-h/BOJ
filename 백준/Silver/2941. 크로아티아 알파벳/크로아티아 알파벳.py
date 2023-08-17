from sys import stdin
ipt = stdin.readline

croatia_str_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
croatia_string = ipt().rstrip()

for step in croatia_str_list:
    croatia_string = croatia_string.replace(step, 'M')

print(len(croatia_string))
