from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 직사각형 좌표의 최댓값이 50이므로 2배만큼의 2차원 배열 생성
    field = [[-1] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]

    # 좌표값 두 배 후 좌표에 직사각형 그리기
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # 테두리를 제외한 내부는 0으로 저장
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아닌 테두리는 1로 저장
                elif field[i][j] != 0:
                    field[i][j] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # BFS 시작
    q = deque()
    q.append((characterX * 2, characterY * 2))
    while q:
        cx, cy = q.popleft()
        # 아이템에 도착하면 나누기 2한 값 저장
        if cx == itemX * 2 and cy == itemY * 2:
            answer = visited[cx][cy] // 2
            break
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if field[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1

    return answer