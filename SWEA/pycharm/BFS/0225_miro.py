import sys
sys.stdin = open('11879_input.txt')

def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)]     # 미로의 크기만큼 visited 생성
    queue = []                              # 큐 생성
    queue.append((i, j))                    # 시작점 인큐
    visited[i][j] = 1                       # 시작점 방문표시
    while queue:
        i, j = queue.pop(0)                 # t <-디큐
        if maze[i][j] == 3:                 # visit[t] >> t에서 할 일 처리
            return 1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:      # i, j에 인접한 칸에 대해
            ni, nj = i+di, j+dj         # 주변 칸 좌표, 미로를 벗어나지 않고 인접한 칸이 벽이 아닐 때
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                # 인큐
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    # 목적지에 도달하지 못한 경우
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = fstart(N) # 출발 좌표 찾기
    ans = bfs(sti, stj, N)
    print(ans)