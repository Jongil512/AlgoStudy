# 진기의 최고급 붕어빵

import sys
sys.stdin = open('1860_input.txt')

def fishbread():
    cnt = 0

    # 더 일찍 올 때
    if min(arr) < M:
        return 'Impossible'

    cycle = (arr[-1] // M) + 1

    for j in range(2, cycle + 1):
        for i in range(N):
            if M*(cycle - 1) <= arr[i] < M*cycle:
                cnt += 1
        check[j] = cnt

        # # 인원이 붕어빵보다 더 많을때
        # if cnt > K:
        #     return 'Impossible'
        cnt = 0

    return 'Possible'

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    check = [0] * (arr[-1] // M + 2)
    print(f'#{tc} {fishbread()}')