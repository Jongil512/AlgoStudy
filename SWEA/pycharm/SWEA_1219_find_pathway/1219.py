import sys
sys.stdin = open('1219_input.txt')

def DFS(s, e, v):
    visited[s] = 1
    for w in range(0, v):
        if matrix[s][w] == 1 and visited[w] == 0:
            DFS(w, e, v)
    if visited[e] == 1:
        return 1
    if visited[e] == 0:
        return 0

def find_pathway(arr, n):
    for i in range(n):
        a, b = arr[i * 2], arr[i * 2 + 1]
        matrix[a][b] = 1

T = 10
for tc in range(1, T+1):
    dum, N = map(int, input().split())
    arr = list(map(int, input().split()))
    S = 0
    E = 99
    matrix = [[0] * (E+1) for _ in range(E+1)]
    visited = [0] * (E+1)
    find_pathway(arr, N)
    print(f'#{tc} {DFS(S, E, 100)}')