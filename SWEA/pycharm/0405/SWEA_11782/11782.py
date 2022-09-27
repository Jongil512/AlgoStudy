import sys
from collections import deque
sys.stdin = open('11782_input.txt')

def fuel(x, y):
    q = deque()
    q.append((x, y))
    adj[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                diff = 0
                if arr[x][y] < arr[nx][ny]:
                    diff = arr[nx][ny] - arr[x][y]
                if adj[x][y] + diff + 1 < adj[nx][ny]:
                    adj[nx][ny] = adj[x][y] + diff + 1
                    q.append((nx, ny))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    adj = [[99999] * N for _ in range(N)]
    fuel(0, 0)
    print(f'#{tc} {adj[N-1][N-1]}')