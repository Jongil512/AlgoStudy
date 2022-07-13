# 그림

import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):
    global cnt
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and draw[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            cnt += 1
            DFS(nx, ny)


N, M = map(int, sys.stdin.readline().rstrip().split())
draw = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
draw_cnt = 0
max_value = 0
for i in range(N):
    for j in range(M):
        if draw[i][j] and not visited[i][j]:
            cnt = 1
            draw_cnt += 1
            visited[i][j] = 1
            DFS(i, j)
            if max_value < cnt:
                max_value = cnt
print(draw_cnt)
print(max_value)