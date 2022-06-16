import sys
sys.stdin = open('3307_input.txt')

# 최장 증가 부분 수열

def LIPP():
    for i in range(1, N+1):     # arr에서 하나씩 꺼낸 다음
        for j in range(i):      # 그 전 수까지만 비교
            if arr[i] > arr[j] and D[j] >= D[i]:    # 만약 arr[i]보다 수는 작지만 D[i]보다 큰 경우
                D[i] = D[j] + 1                     # D[i]의 순서가 정해짐

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    D = [0] * (N+1)             # 순서 배열 생성
    LIPP()
    print(f'#{tc} {max(D)}')

    # 0 5 3 7 1 2 4 8 9

    #D = 0 1 1 2 1 2 3 4 5