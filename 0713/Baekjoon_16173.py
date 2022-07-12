# 점프왕 쩰리

import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):
    global ans
    if maap[x][y] == -1:
        ans = "HaruHaru"
    for dx, dy in ((1, 0), (0, 1)):
        nx = x+(dx*maap[x][y])
        ny = y+(dy*maap[x][y])
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = 1
            DFS(nx, ny)


N = int(sys.stdin.readline().rstrip())
maap = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

ans = "Hing"

DFS(0, 0)
print(ans)