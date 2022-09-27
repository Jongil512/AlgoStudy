import sys

sys.stdin = open('11633_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    result = [] # 리스트 생성
    while len(arr) >= M:
        sum_num = 0
        for i in range(M):
            sum_num += arr[i]
        result.append(sum_num)
        arr = arr[1:]

    min_v = result[0]
    max_v = result[0]

    for number in result:
        if min_v > number:
            min_v = number
        if max_v < number:
            max_v = number

    ans = max_v - min_v
    print(f'#{tc} {ans}')
