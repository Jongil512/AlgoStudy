from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def bfs(a, b):
        q = deque([(a, b)])
        visited[a][b] = 1
        while q:
            (x, y) = q.popleft()
            if x == N - 1 and y == M - 1:
                return visited[N - 1][M - 1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    bfs(0, 0)
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))