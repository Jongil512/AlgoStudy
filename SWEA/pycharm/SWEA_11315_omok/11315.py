import sys
sys.stdin = open('11315_input.txt')

def omok(arr):
    dx = [1, 1, 0, 1]
    dy = [1, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    cnt = 1
                    ni = i
                    nj = j
                    while 0 <= ni+dx[k] <= N-1 and 0 <= nj+dy[k] <= N-1 and arr[ni+dx[k]][nj+dy[k]] == 'o':
                        cnt += 1
                        ni += dx[k]
                        nj += dy[k]
                        if cnt == 5:
                            return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    print(f'#{tc} {omok(arr)}')