# 섬의 개수

def land(v):
    q = [v]
    while q:
        t = q.pop(0)
        x = t[0]
        y = t[1]
        visited[x][y] = 1
        # 델타 검색
        for dx, dy in D:
            nx = x + dx
            ny = y + dy
            # 범위 및 방문 확인
            if 0 <= nx < H and 0 <= ny < W and world[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break

    world = [list(map(int, input().split())) for _ in range(H)]
    print(world)
    visited = [[0]*W for _ in range(H)]
    cnt = 0
    D = ((1, 1), (1, -1), (-1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (-1, 0))

    # 섬이면서 방문하지 않은 곳 BFS
    for i in range(H):
        for j in range(W):
            if world[i][j] and not visited[i][j]:
                land((i, j))
                cnt += 1
    print(cnt)