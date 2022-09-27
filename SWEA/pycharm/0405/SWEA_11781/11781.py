import sys
sys.stdin = open('11781_input.txt')

def grow_tree(v):
    total = 0
    D[v] = 0
    for i in range(V):
        min_v = 9999999
        for w in range(V):
            if adj[v][w] != 0 and D[w] < min_v and not visited[w]:
                min_v = D[w]
                u = w
        #     if D[w] < min_v and not visited[w]:
        #         min_v = D[w]
        #         u = w
        # visited[u] = 1
        # total += D[u]
        for w in range(V):
            if adj[u][w] and not visited[w]:
                if D[w] > adj[u][w]:
                    D[w] = adj[u][w]
    return total

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        s, e, d = map(int, input().split())
        adj[s][e] = adj[e][s] = d
    D = [99999999] * (V)
    visited = [0] * (V+1)
    print(f'#{tc} {grow_tree(0)}')