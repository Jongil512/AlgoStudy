from collections import deque

def solution(board):
    N = len(board)
    M = len(board[0])
    answer = 999999
    # 각 방향에 따른 값을 저장해야 하기 때문에 3차원 배열 선언
    fee = [[[999999] * M for _ in range(N)] for _ in range(4)]

    q = deque()

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 시작점은 4방향 모두 0으로 고정
    for i in range(4):
        fee[i][0][0] = 0
    # 시작점이 (0, 0)이기 때문에 갈 수 있는 방향은 오른쪽과 아래뿐 (처음은 모두 직선)
    # 오른쪽으로 갈 수 있다면 (0, 1)에 왼쪽 방향에서 온 값을 100으로 저장 후 큐에 추가
    if board[0][1] != 1:
        q.append([0, 1, 100, 1])
        fee[1][0][1] = 100
    # 아래로 갈 수 있다면 (0, 1)에 왼쪽 방향에서 온 값을 100으로 저장 후 큐에 추가
    if board[1][0] != 1:
        q.append([1, 0, 100, 2])
        fee[2][1][0] = 100

    while q:
        x, y, cost, d = q.popleft()
        # 갈 수 있는 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 직전에 온 방향과 다른 방향일 경우 cost + 600 (코너)
            if d != i:
                n_cost = cost + 600
            # 직전에 온 방향과 같은 방향일 경우 cost + 100 (직선)
            else:
                n_cost = cost + 100

            # 범위 체크 및 진행 가능한지 체크
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 1:
                # 진행 가능하고 해당하는 값보다 현재 값이 작다면 해당 좌표에 진행방향과 함께 값 입력 후 큐에 추가
                if fee[i][nx][ny] > n_cost:
                    fee[i][nx][ny] = n_cost
                    q.append([nx, ny, n_cost, i])

    # 마지막 좌표의 4방향에서 온 값 중 최소값 저장
    for z in range(4):
        if answer > fee[z][-1][-1]:
            answer = fee[z][-1][-1]

    return answer