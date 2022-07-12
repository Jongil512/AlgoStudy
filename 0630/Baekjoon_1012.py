import sys

def DFS(x, y):
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx = x+dx
        ny = y+dy
        if 0 <= nx < N and 0 <= ny < M and farm[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            DFS(nx, ny)

T = int(sys.stdin.readline().rstrip())
for tc in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    farm = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(K):
        x, y = (map(int, sys.stdin.readline().split()))
        farm[y][x] = 1
    for i in range(N):
        for j in range(M):
            if farm[i][j] and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                DFS(i, j)
    print(cnt)