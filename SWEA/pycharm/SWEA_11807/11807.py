import sys

sys.stdin = open('11807_input.txt')

T = int(input())

for tc in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    charge = list(map(int, input().split()))

    cnt = 0
    start = 0
    while start <= N:
        if start + K >= N:
            print(f'#{tc} {cnt}')
            break
        elif start + K in charge:
            cnt += 1
            start += K
        elif start + K not in charge:
            for i in range(1, K+1):
                if i == K:
                    print(f'#{tc} 0')
                    start += N
                    break
                elif (start + K - i) in charge:
                    cnt += 1
                    start = start + K - i
                    break
                else:
                    pass