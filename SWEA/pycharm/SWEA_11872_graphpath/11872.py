import sys
sys.stdin = open('11872_input.txt')

def dfs(s, g, v):
    visited[s] = 1
    for w in range(1, v + 1):
        if matrix[s][w] == 1 and visited[w] == 0:
            dfs(w, g, v)
    if visited[g] == 1:
        return 1
    if visited[g] == 0:
        return 0

def graph_path(arr, v, e, s, g):
    for i in range(e):
        matrix[arr[i][0]][arr[i][1]] += 1
    return dfs(s, g, v)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    matrix = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V+1)
    print(f'#{tc} {graph_path(arr, V, E, S, G)}')