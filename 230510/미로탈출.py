from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def bfs(sx, sy, tx, ty):
        nonlocal answer
        q = deque()
        q.append((sx, sy))
        cnt = [[0] * m for _ in range(n)]
        visited = [[0] * m for _ in range(n)]
        while q:
            x, y = q.popleft()
            if x == tx and y == ty:
                return cnt[x][y]
            visited[x][y] = 1
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != "X":
                    q.append((nx, ny))
                    cnt[nx][ny] = cnt[x][y] + 1
        answer = -1
        return

    start, end, lever = [0, 0], [0, 0], [0, 0]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = [i, j]
            elif maps[i][j] == "L":
                lever = [i, j]
            elif maps[i][j] == "E":
                end = [i, j]

    distA = bfs(start[0], start[1], lever[0], lever[1])
    distB = bfs(lever[0], lever[1], end[0], end[1])

    if distA == -1 or distB == -1:
        return -1

    return distA + distB

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))