import sys
sys.setrecursionlimit(100000)

def solution(maps):
    answer = []
    global total
    total = 0
    lands = [list(map) for map in maps]
    N = len(lands[0])
    M = len(lands)
    visited = [[0] * N for _ in range(M)]

    def dfs(x, y):
        global total
        visited[x][y] = 1
        for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and lands[nx][ny] != 'X':
                total += int(lands[nx][ny])
                dfs(nx, ny)

    for i in range(M):
        for j in range(N):
            if lands[i][j] != 'X' and not visited[i][j]:
                total = int(lands[i][j])
                dfs(i, j)
                answer.append(total)

    if answer:
        return sorted(answer)
    else:
        return [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))