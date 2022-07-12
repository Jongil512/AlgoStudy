from collections import deque
# 안전 영역

def BFS(x, y, safe):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    # 범위 확인 후 BFS
    while q:
        x, y = q.popleft()

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if world[nx][ny] >= safe and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

N = int(input())
world = [list(map(int, input().split())) for _ in range(N)]

world_min = min(map(min, world))    # 배열의 최솟값
world_max = max(map(max, world))    # 배열의 최댓값

max_safe_zone = 0
for safe in range(world_min, world_max+1):      # 배열의 최소부터 최대까지 반복
    visited = [([0] * N) for _ in range(N)]
    cnt = 0                                     # 안전한 영역 개수
    for i in range(N):
        for j in range(N):
            if world[i][j] >= safe and not visited[i][j]:
                BFS(i, j, safe)
                cnt += 1
    if cnt > max_safe_zone:                     # 최대값 갱신
        max_safe_zone = cnt

print(max_safe_zone)