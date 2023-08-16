def solution(my_string, overwrite_string, s):
    my_string = list(my_string)
    for i in range(s, len(overwrite_string) + s):
        my_string[i] = overwrite_string[i - s]
    answer = ''.join(my_string)
    return answer