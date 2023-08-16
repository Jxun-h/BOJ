# 단어 갯수 지정
word_n = int(input())

# 단어들 리스트 만들기
word_lst = []
for _ in range(word_n) :
    word_lst.append(input())

# 문자들 마다에 곱해야할 수 딕셔너리화 시키기 {'G': 100, 'C': 1010, 'F': 1, 'A': 10000, 'D': 100, 'E': 10, 'B': 1}
alpha_digit_dic = {}

for each_lst in word_lst :
    cnt = 0
    for i in each_lst :

        if i not in alpha_digit_dic :
            alpha_digit_dic[i] = 10 ** (len(each_lst) - cnt - 1)
        elif i in alpha_digit_dic :
            alpha_digit_dic[i] += 10 ** (len(each_lst) - cnt - 1)
        cnt += 1

# 딕셔너리 Key값을 내림차순으로 솔팅하고 9부터 차례대로 곱해주기
digit_lst = sorted(list(alpha_digit_dic.values()), reverse=True)

sum = 0
for i in range(len(digit_lst)) :
    sum += digit_lst[i] * (9 - i)
ans = sum
print(ans)