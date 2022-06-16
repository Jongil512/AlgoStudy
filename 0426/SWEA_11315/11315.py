import sys
sys.stdin = open('11315_input.txt')

# 오목 판정

def omok(x, y):
    global ans
    global cnt
    for i in range(4):                                              # 델타 검색
        cnt = 1                                                     # 델타 시작할 때마다 cnt 초기화
        for j in range(1, 5):                                       # 최소 5개 이상이면 오목이므로 4번만 o가 있으면 오목
            nx = x + dx[i] * j                                      # DFS로 돌리면 다른 방향까지 인정되기 때문에 곱으로 계산
            ny = y + dy[i] * j
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':  # 조건 만족할 경우 cnt + 1
                cnt += 1
                if cnt >= 5:                                        # cnt가 5 이상일 때 YES
                    ans = 'YES'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    ans = 'NO'
    dx = [1, 1, 1, 0]
    dy = [0, -1, 1, 1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                cnt = 1
                omok(i, j)
    print(f'#{tc} {ans}')