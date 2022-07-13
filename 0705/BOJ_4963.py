# 섬의 개수

import sys
sys.setrecursionlimit(10**5)

def DFS(x, y):
    for dx, dy in ((0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)):
        nx = x+dx
        ny = y+dy
        if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            DFS(nx, ny)

while True:
    W, H = map(int, sys.stdin.readline().rstrip().split())
    if W == 0 and H == 0:
        break
    arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(H)]
    visited = [[0]*W for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                DFS(i, j)
    print(cnt)