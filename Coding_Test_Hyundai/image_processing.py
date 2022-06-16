import sys

def image_processing(x, y, c):
    matrix[x][y] = c
    visited[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < H and 0 <= ny < W:
            if visited[nx][ny] == 0 and matrix[nx][ny] == origin_num:
                image_processing(nx, ny, c)
    return

H, W = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
Q = int(sys.stdin.readline())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(Q):
    visited = [[0] * W for _ in range(H)]
    i, j, c = map(int, sys.stdin.readline().split())
    origin_num = matrix[i - 1][j - 1]
    image_processing(i-1, j-1, c)
for lst in matrix:
    print(*lst)