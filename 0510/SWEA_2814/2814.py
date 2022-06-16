import sys
sys.stdin = open('2814_input.txt')

# 최장 경로 찾기

def DFS(v, cur_len):
    global max_len
    for w in range(1, N+1):
        if matrix[v][w] == 1 and not visited[w]:
            visited[w] = 1
            DFS(w, cur_len+1)
            visited[w] = 0
    if cur_len > max_len:
        max_len = cur_len

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for i in range(M):
        x, y = map(int, input().split())
        matrix[x][y] = matrix[y][x] = 1
    max_len = 0
    for i in range(1, N+1):
        visited[i] = 1
        DFS(i, 1)
        visited[i] = 0

    print(f'#{tc} {max_len}')