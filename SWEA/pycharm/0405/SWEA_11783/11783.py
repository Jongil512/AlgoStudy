import sys
sys.stdin = open('11783_input.txt')

def min_dist(v):
    D[v] = 0
    for i in range(N+1):
        min_v = 9999999
        for w in range(N+1):
            if not visited[w] and D[w] < min_v:
                min_v = D[w]
                u = w
        visited[u] = 1
        for w in range(N+1):
            if adj [u][w] and not visited[w]:
                if D[w] > D[u] + adj[u][w]:
                    D[w] = D[u] + adj[u][w]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(E):
        s, e, d = map(int, input().split())
        adj[s][e] = d
    D = [99999999] * (N + 1)
    visited = [0] * (N + 1)
    min_dist(0)
    print(f'#{tc} {D[N]}')