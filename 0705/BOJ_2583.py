# 영역 구하기
import sys
sys.setrecursionlimit(10**5)

def DFS(x, y):
    global cnt
    for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
        nx = x+dx
        ny = y+dy
        if 0 <= nx < M and 0 <= ny < N and not matrix[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            cnt += 1
            DFS(nx, ny)

M, N, K = map(int, sys.stdin.readline().rstrip().split())
matrix = [[0]*(N) for _ in range(M)]
visited = [[0]*(N) for _ in range(M)]

for i in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            matrix[k][j] = 1

ans = []
square = 0

for i in range(M):
    for j in range(N):
        if not matrix[i][j] and not visited[i][j]:
            cnt = 1
            square += 1
            visited[i][j] = 1
            DFS(i, j)
            ans.append(cnt)
print(square)
ans.sort()
print(*ans)