from sys import stdin

# 에라토스테네스의 체
def get_prime_arr(num):
    arr = [True] * num
    mm = int(num ** 0.5)

    for x in range(2, mm + 1):
        if arr[x]:
            for y in range(x + x, num, x):
                arr[y] = False

    return [i for i in range(2, num) if arr[i] == True]

# 소수 조합 판별기
def get_gold(n, arr):
    # 각 조합의 차를 넣을 변수
    sub = 9999999
    # 배열에 사용될 인덱스 값
    idx = len(arr) // 2

    # 배열 오른쪽으로 이동하며 조합찾기
    for right in range(idx, len(arr)):
        # 기준이 되는 배열의 값
        std = arr[right]

        # n에서 std 빼고
        sub_std_val = n - std

        # 빼고 남은 값이 소수 맞나요?
        if check_prime_num(sub_std_val) is False:
            # 우측으로 가
            continue

        # 찾았네
        # 큰 값에서 작은 값을 빼
        if sub_std_val > std:
            tmp_sub = sub_std_val - std
        else:
            tmp_sub = std - sub_std_val

        # sub 값 비교
        if sub > tmp_sub:
            # 더 작네?
            sub = tmp_sub

            # 리턴값을 정해준다
            r1, r2 = std, sub_std_val
        else:
            # 뱉어
            return r1, r2

def check_prime_num(num):
    n = int(num ** 0.5)
    for x in range(2, n+1):
        if num % x == 0:
            return False
    return True


# 입력 준비 됐나요~
ipt = stdin.readline
step = int(ipt().rstrip())

# 입력한 만큼 뺑이 칠거에요~
for i in range(step):
    # 숫자 입력2
    num = int(ipt().rstrip())

    # 소수 반으로 나눠서~
    is_prime_n = num // 2
    
    # 소수로 판별이 되면~
    if check_prime_num(is_prime_n):
        # 출력하세용~
        print(is_prime_n, is_prime_n)
    else:
        # 소수 리스트 가져와.
        arr = get_prime_arr(num)
        # 없으면 조합 찾으러 가자
        r1, r2 = get_gold(num, arr)
        
        # 작은거 먼저 출력해주자
        if r1 <= r2:
            print(r1, r2)
        else:
            print(r2, r1)