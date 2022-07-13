# 전쟁 - 전투

import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):
    global cnt
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N and maap[nx][ny] == "W" and not visited[nx][ny]:
            if maap[x][y] == "W":
                cnt += 1
                visited[nx][ny] = 1
                DFS(nx,ny)
        elif 0 <= nx < M and 0 <= ny < N and maap[nx][ny] == "B" and not visited[nx][ny]:
            if maap[x][y] == "B":
                cnt += 1
                visited[nx][ny] = 1
                DFS(nx,ny)


N, M = map(int, sys.stdin.readline().rstrip().split())
maap = [list(sys.stdin.readline().rstrip()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
power_W = 0
power_B = 0
for i in range(M):
    for j in range(N):
        if maap[i][j] == "W" and not visited[i][j]:
            cnt = 1
            visited[i][j] = 1
            DFS(i, j)
            power_W += cnt ** 2
        elif maap[i][j] == "B" and not visited[i][j]:
            cnt = 1
            visited[i][j] = 1
            DFS(i, j)
            power_B += cnt ** 2
print(power_W, end=' ')
print(power_B)