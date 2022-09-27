import sys
from collections import deque
sys.stdin = open('1249input.txt')

def BFS(si, sj, ei, ej):
    q = deque()
    v = [[100000]*N for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]
    return v[ei][ej]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = BFS(0, 0, N-1, N-1)
    print(f'#{tc} {ans}')