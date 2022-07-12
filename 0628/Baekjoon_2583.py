# 영역 구하기

def square(x1, x2, y1, y2):
    for i in range(y1, y2):
        for j in range(x1, x2):
            maap[i][j] = 1

def BFS(v):
    global cnt
    global width
    q = [v]
    cnt += 1
    while q:
        t = q.pop(0)
        x, y = t[0], t[1]
        for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N and not maap[nx][ny]:
                width += 1
                maap[nx][ny] = 2
                q.append((nx, ny))

M, N, K = map(int, input().split())
maap = [[0]*(N) for _ in range(M)]
for t in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    square(x1, x2, y1, y2)
cnt = 0
ssum = []
for i in range(M):
    for j in range(N):
        if maap[i][j] == 0:
            width = 1
            maap[i][j] = 2
            BFS((i, j))
            ssum.append(width)
ssum.sort()
print(cnt)
print(*ssum)