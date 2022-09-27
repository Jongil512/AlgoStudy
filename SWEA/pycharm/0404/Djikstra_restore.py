import sys
sys.stdin = open('1249_input.txt')
import heapq

# def min_dist():
#     min_v = 99993333
#     x, y = -1, -1
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j] and D[i][j] < min_v:
#                 min_v = D[i][j]
#                 x, y = i, j
#     return x, y

def dijkstra(x, y):
    # 출발점
    D[x][y] = 0
    heapq.heappush(heap, (D[x][y], x, y)) # 가중치, x, y
    # 무한루프
    while True:
        # 가중치 최소값의 좌표 찾기
        # x, y = min_dist()
        d, x, y = heapq.heappop(heap)
        visited[x][y] = 1
        # [N-1][N-1]에 도착하면 리턴
        if x == N-1 and y == N-1:
            return
        # 4방향 탐색, 인접하고 방문하지 않은 좌표의 값 업데이트
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and D[nx][ny] > D[x][y] + arr[nx][ny]:
                D[nx][ny] = D[x][y] + arr[nx][ny]
                heapq.heappush(heap, (D[nx][ny], nx, ny))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    D = [[99999999]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    heap = []
    dijkstra(0, 0)
    print(f'#{tc} {D[N-1][N-1]}')