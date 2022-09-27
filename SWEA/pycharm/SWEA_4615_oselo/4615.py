import sys
sys.stdin = open('4615_input.txt')

def oselo():
    for i in range(M):
        si, sj, d = insert[i][0], insert[i][1], insert[i][2]
        matrix[si][sj] = d
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, 1), (0, -1)):
            s = []
            for k in range(1, N):
                ni, nj = si + di * k, sj + dj * k
                if 1 <= ni <= N and 1 <= nj <= N:
                    if matrix[ni][nj] == 0:
                        break
                    elif matrix[ni][nj] == d:
                        for ci, cj in s:
                            matrix[ci][cj] = d
                        break
                    else:
                        s.append((ni, nj))
                else:
                    break
    black = white = 0
    for lst in matrix:
        black += lst.count(1)
        white += lst.count(2)

    return black, white

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [[0] * (N+1) for _ in range(N + 1)]
    matrix[N // 2][N // 2] = matrix[N // 2 + 1][N // 2 + 1] = 2
    matrix[N // 2 + 1][N // 2] = matrix[N // 2][N // 2 + 1] = 1
    insert = [list(map(int, input().split())) for _ in range(M)]
    print(f'#{tc}', *oselo())
