import sys
sys.stdin = open('11889_input.txt')

def node_count(s, g):
    Q = []
    Q.append(s)
    while Q:
        t = Q.pop(0)
        if t == g:
            return visited[g]
        for w in range(1, V+1):
            if adj[t][w] == 1 and visited[w] == 0:
                visited[w] = visited[t] + 1
                Q.append(w)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    for i, j in arr:
        adj[i][j] = adj[j][i] = 1
    visited = [0] * (V+1)
    node_count(S, G)
    print(f'#{tc} {visited[G]}')