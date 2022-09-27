import sys
sys.stdin = open('14037_input.txt')

def check(si, sj):
    # 위쪽 방향
    for i in range(si-1, -1, -1):
        if v[i][sj] == 1:
            return 0
    # 좌상 방향
    i, j = si -1, sj -1
    while i >= 0 and j >= 0:
        if v[i][j] == 1:
            return 0
        i, j = i - 1, j - 1

    # 우상 방향
    i, j = si - 1, sj + 1
    while i >= 0 and j < N:
        if v[i][j] == 1:
            return 0
        i, j = i - 1, j + 1

    return 1

def DFS(n):
    global ans
    if n == N:
        ans += 1
        return
    else:
        for j in range(N):
            if check(n, j):
                v[n][j] = 1
                DFS(n+1)
                v[n][j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    v = [[0]*N for _ in range(N)]
    DFS(0)
    print(f'#{tc} {ans}')