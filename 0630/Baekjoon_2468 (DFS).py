# 안전 영역

import sys
sys.setrecursionlimit(10**6)

def DFS(x, y, safe):
    for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
        nx = x+dx
        ny = y+dy
        if 0 <= nx < N and 0 <= ny < N and world[nx][ny] > safe and not visited[nx][ny]:
            visited[nx][ny] = 1
            DFS(nx, ny, safe)

N = int(sys.stdin.readline())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_depth = max(map(max, world))
min_depth = min(map(min, world))

safe_zone_cnt = 0

for k in range(max_depth+1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if world[i][j] > k and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                DFS(i, j, k)
    if cnt > safe_zone_cnt:
        safe_zone_cnt = cnt
print(safe_zone_cnt)