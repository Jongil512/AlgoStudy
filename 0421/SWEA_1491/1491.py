import sys
sys.stdin = open('1491_input.txt')

def wall_deco():
    # 최솟값 초기화
    min_v = 84950634
    for r in range(1, N+1):
        # 1부터 돌리면 중복값이 발생해 시간이 오래걸리므로 r부터 시작
        for c in range(r, N+1):
            # r*c가 N 이하이면 최솟값과 비교
            if (r*c) <= N:
                if A * abs(r-c) + B * (N - (r*c)) < min_v:
                    min_v = A * abs(r - c) + B * (N - (r * c))
            # 그렇지 않으면 break
            else:
                break
    return min_v

T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    print(f'#{tc} {wall_deco()}')