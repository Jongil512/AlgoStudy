# 현수막

import sys
sys.setrecursionlimit(6**10)

def DFS(x, y):
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1,-1), (1, -1), (-1, 1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N and temp[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            DFS(nx, ny)


M, N = map(int, sys.stdin.readline().rstrip().split())
temp = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

cnt = 0
for i in range(M):
    for j in range(N):
        if temp[i][j] and not visited[i][j]:
            visited[i][j] = 1
            cnt += 1
            DFS(i, j)
print(cnt)