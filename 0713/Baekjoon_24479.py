# 깊이 우선 탐색1

import sys
sys.setrecursionlimit(10**6)

def DFS(matrix, v, visited):
    global cnt
    visited[v] = cnt
    for i in matrix[v]:
        if not visited[i]:
            cnt += 1
            DFS(matrix, i, visited)


N, M, R = map(int, sys.stdin.readline().rstrip().split())
matrix = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for i in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    matrix[x].append(y)
    matrix[y].append(x)

for i in range(1, N+1):
    matrix[i].sort()

cnt = 1
DFS(matrix, R, visited)
for i in range(1, N+1):
    print(visited[i])