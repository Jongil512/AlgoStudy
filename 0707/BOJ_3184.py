# 양

import sys
sys.setrecursionlimit(10 ** 6)

def DFS(x, y):
    global wolf_cnt
    global sheep_cnt
    if yard[x][y] == "v":
        wolf_cnt += 1
    elif yard[x][y] == "o":
        sheep_cnt += 1
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and yard[nx][ny] != "#" and not visited[nx][ny]:
            visited[nx][ny] = 1
            DFS(nx, ny)


N, M = map(int, sys.stdin.readline().rstrip().split())
yard = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

fin_sheep = 0
fin_wolf = 0

for i in range(N):
    for j in range(M):
        sheep_cnt = 0
        wolf_cnt = 0
        if yard[i][j] != "#" and not visited[i][j]:
            visited[i][j] = 1
            DFS(i, j)
            if sheep_cnt > wolf_cnt:
                fin_sheep += sheep_cnt
            else:
                fin_wolf += wolf_cnt
print(fin_sheep, end=' ')
print(fin_wolf)
