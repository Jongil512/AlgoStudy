# 음식물 피하기

import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):
    global cnt
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N+1 and 0 <= ny < M+1 and path[nx][ny] and not visited[nx][ny]:
            cnt += 1
            visited[nx][ny] = 1
            DFS(nx, ny)


N, M, K = map(int, sys.stdin.readline().rstrip().split())
path = [[0]*(M+1) for _ in range(N+1)]
visited = [[0]*(M+1) for _ in range(N+1)]
for i in range(K):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    path[x][y] = 1

max_food = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if path[i][j] and not visited[i][j]:
            cnt = 1
            visited[i][j] = 1
            DFS(i, j)
            if cnt > max_food:
                max_food = cnt
print(max_food)