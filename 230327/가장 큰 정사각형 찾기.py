# 전형적인 dp 문제
def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if board[i - 1][j - 1]:
                # board가 1일 때 dp 좌표의 좌, 상, 상좌 수 중 가장 작은 수 +1 이 만들 수 있는 정사각형의 변의 길이
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                answer = max(answer, dp[i][j])
    return answer ** 2