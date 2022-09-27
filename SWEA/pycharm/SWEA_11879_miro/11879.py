import sys
sys.stdin = open('11879_input.txt')

def dfs(i, j, N):
    global flag
    visited[i][j] = 1
    for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
            if arr[ni][nj] == 3:
                flag = 1
            else:
                dfs(ni, nj, N)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j
    flag = 0
    visited = [[0] * N for _ in range(N)]
    dfs(x, y, N)
    print(f'#{tc} {flag}')


