import sys
sys.stdin = open('5215_input.txt')

# 햄버거 다이어트

def hamburger(n, total_score, total_cal):
    global max_taste
    if total_cal > Cal:                     # 총 칼로리가 제시된 칼로리를 넘을 경우 리턴
        return

    if n == N:                              # 마지막까지 돌았을 때 맛 점수의 총 합이 최대 점수보다 높다면 변경 후 리턴
        if max_taste < total_score:
            max_taste = total_score
        return

    hamburger(n+1, total_score + arr[n][0], total_cal + arr[n][1])      # 이번 햄버거를 포함할 경우
    hamburger(n+1, total_score, total_cal)                              # 이번 햄버거를 포함하지 않을 경우

T = int(input())
for tc in range(1, T+1):
    N, Cal = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 변수값들 초기화
    total_cal = 0
    total_score = 0
    max_taste = 0
    hamburger(0, 0, 0)
    print(f'#{tc} {max_taste}')