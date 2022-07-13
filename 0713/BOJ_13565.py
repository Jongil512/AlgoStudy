# 침투

import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N and not figure[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            figure[nx][ny] = 2
            DFS(nx, ny)


M, N = map(int, sys.stdin.readline().rstrip().split())
figure = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

for i in range(1):
    for j in range(N):
        if not figure[i][j] and not visited[i][j]:
            visited[i][j] = 1
            DFS(i, j)

ans = "NO"
for i in range(M-1, M):
    for j in range(N):
        if figure[i][j] == 2:
            ans = "YES"
print(ans)