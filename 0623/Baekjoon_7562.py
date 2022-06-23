def chess(v):
    q = [v]
    while q:
        t = q.pop(0)
        nx = t[0]
        ny = t[1]
        if (GX, GY) == t:
            return visited[GX][GY]
        for dx, dy in D:
            px = nx+dx
            py = ny+dy
            if 0 <= px < I and 0 <= py < I and not visited[px][py]:
                visited[px][py] = visited[nx][ny] + 1
                q.append((px, py))

T = int(input())
for tc in range(1, T+1):
    I = int(input())
    X, Y = map(int, input().split())
    GX, GY = map(int, input().split())
    visited = [([0]*I) for _ in range(I)]
    D = ((1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2))
    print(chess((X, Y)))