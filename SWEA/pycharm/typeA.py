from collections import deque

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] = arr[n][y] + 1
                visited[nx][ny] = 1
                q.append((nx, ny))