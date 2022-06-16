import sys
sys.stdin = open('6057_input.txt')

def graph():
    cnt = 0
    # 인접행렬을 만들었고 i < j < k이므로 반복문으로 i >> j, j >> k, k >> i가 모두 1인 경우를 찾음
    for i in range(N+1):
        for j in range(i, N+1):
            for k in range(j, N+1):
                # i >> j, j >> k가 1인 경우
                if adj[i][j] == 1 and adj[j][k] == 1:
                    # i >> k 도 1이면 카운트 + 1
                    if adj[i][k] == 1:
                        cnt += 1
    return cnt
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    for i in range(M):
        x, y = map(int, input().split())
        adj[x][y] = 1
        adj[y][x] = 1
    print(f'#{tc} {graph()}')

