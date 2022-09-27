import sys
from collections import deque
sys.stdin = open('1249input.txt')

def BFS(x, y, ex, ey):
    q = deque()
    q.append((x, y))
    D[x][y] = arr[x][y]
    while q:
        sx, sy = q.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = sx + dx, sy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and D[nx][ny] > D[sx][sy] + arr[nx][ny]:
                q.append((nx, ny))
                D[nx][ny] = D[sx][sy] + arr[nx][ny]
    return D[ex][ey]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    D = [[99999999]*N for _ in range(N)]
    ans = BFS(0, 0, N-1, N-1)
    print(f'#{tc} {ans}')