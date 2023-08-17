from sys import stdin

ipt = stdin.readline

# 테스트 케이스의 개수 T임
T = int(ipt().rstrip())

for step1 in range(T):
    arr = []
    # 지원자의 숫자 N임
    N = int(ipt().rstrip())

    for step2 in range(N):
        # 지원자  서류, 면접 등수 입력받는다~
        arr.append(list(map(int, ipt().rstrip().split())))

    # 서류 등수가 낮은 순으로 정렬한번 때려주고
    arr.sort(key=lambda x: x[0])
    cnt = 1

    # 면접 등수만 비교할거에용~
    std = arr[0][1]
    for idx in range(1, N):
        if arr[idx][1] < std:
            std = arr[idx][1]
            cnt += 1

    # 통과 개수
    print(cnt)

    