# 그림

import sys
from collections import deque

def BFS(v, cnt):
    q = deque()
    q.append(v)
    while q:
        t = q.popleft()
        cnt += 1
        x, y = t[0], t[1]
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and drawing[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
    square.append(cnt)

N, M = map(int, sys.stdin.readline().split())
drawing = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
square = []
draw_cnt = 0
for i in range(N):
    for j in range(M):
        if drawing[i][j] and not visited[i][j]:
            draw_cnt += 1
            cnt = 0
            visited[i][j] = 1
            BFS((i, j), cnt)
if draw_cnt:
    print(draw_cnt)
    print(max(square))
else:
    print(draw_cnt)
    print(0)