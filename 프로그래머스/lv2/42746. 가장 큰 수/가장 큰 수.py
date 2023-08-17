def solution(numbers):
    result = []

    for number in numbers:
        temp = str(number)

        while len(temp) < 4:
            temp += temp

        result.append([temp[:4], number])

    return str(int(''.join([str(x[1]) for x in sorted(result, reverse=True)])))