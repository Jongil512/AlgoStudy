import sys

def DFS(x, y):
    global cnt
    visited[x][y] = 1
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx = x+dx
        ny = y+dy
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] and not visited[nx][ny]:
            cnt += 1
            DFS(nx, ny)

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
total_cnt = 0
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            total_cnt += 1
            cnt = 1
            DFS(i, j)
            ans.append(cnt)
print(total_cnt)
ans.sort()
for i in range(total_cnt):
    print(ans[i])