# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def dfs(v):
    # 방문처리
    visited[v] = 1
    print(v, end=' ')

    # 시작정점(v)의 인접한 모든 정점에 대해
    # 방문하지 않은 정점이면 재귀호출
    for w in range(1, V+1):
        # 인접하고 방문하지 않은 정점들
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)

V, E = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)] # 인접행렬 초기화
visited = [0] * (V+1) # 방문처리
temp = list(map(int, input().split()))

# 인접행렬 저장하기
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    adj[s][e] = adj[e][s] = 1 # 방향성 없음

# 확인용
for i in range(V+1):
    print(f'{i} | {adj[i]}')