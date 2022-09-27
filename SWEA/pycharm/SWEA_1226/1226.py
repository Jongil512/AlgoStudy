import sys
sys.stdin = open('1226_input.txt')

def dfs(x, y, m):
    global flag
    visited[x][y] = 1
    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < m and arr[nx][ny] != 1 and visited[nx][ny] == 0:
            if arr[nx][ny] == 3:
                flag = 1
            else:
                dfs(nx, ny, m)

T = 10
for tc in range(1, T+1):
    N = int(input())
    M = 16
    arr = [list(map(int, input())) for _ in range(M)]
    sx = sy = 1
    flag = 0
    visited = [[0] * 16 for _ in range(M)]
    dfs(sx, sy, M)
    print(f'#{tc} {flag}')