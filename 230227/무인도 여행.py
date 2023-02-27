import sys
sys.setrecursionlimit(100000)

def solution(maps):
    answer = []
    # 한 번에 갈 수 있는 수의 합 초기화
    global total
    total = 0
    lands = [list(map) for map in maps]
    N = len(lands[0])
    M = len(lands)
    # 방문배열 초기화
    visited = [[0] * N for _ in range(M)]

    def dfs(x, y):
        global total
        # 방문체크
        visited[x][y] = 1
        # 상하좌우 돌면서 깊이 우선 탐색
        for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            # 다음으로 넘어가기 위한 조건
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and lands[nx][ny] != 'X':
                # 조건 만족시 total에 합해주고 다음 dfs로 넘어감
                total += int(lands[nx][ny])
                dfs(nx, ny)

    for i in range(M):
        for j in range(N):
            # 맵을 탐색하다 X가 아닌 곳에서 dfs 시작
            if lands[i][j] != 'X' and not visited[i][j]:
                # 시작 전 total에 해당 숫자 할당
                total = int(lands[i][j])
                dfs(i, j)
                # dfs 종료 후 total 값 추가
                answer.append(total)

    if answer:
        return sorted(answer)
    else:
        return [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))