from sys import stdin

ipt = stdin.readline
math_arr = ipt().rstrip().split('-')

if len(math_arr) == 1:
    math_arr = list(map(int, math_arr[0].split('+')))
    result = sum(math_arr)
else:
    if math_arr[0].isalnum():
        result = int(math_arr[0])
    else:
        result = sum(list(map(int, math_arr[0].split('+'))))
    for step in range(1, len(math_arr)):
        if math_arr[step].isalnum():
            result -= int(math_arr[step])
        else:
            try:
                result -= int(eval(math_arr[step]))
            except:
                result -= sum(list(map(int, math_arr[step].split('+'))))

print(result)