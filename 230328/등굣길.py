def solution(m, n, puddles):
    # indexError 방지를 위해 가장 위, 가장 왼쪽 배열 1줄씩 추가
    matrix = [[0] * (m + 1) for _ in range(n + 1)]
    # 시작은 1로 고정
    matrix[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 웅덩이거나 시작점이면 continue
            if [j, i] in puddles or [i, j] == [1, 1]:
                continue
            # 아니라면 왼쪽 + 위
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix[-1][-1] % 1000000007