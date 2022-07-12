# 연결 요소의 개수 (DFS)

import sys
sys.setrecursionlimit(10**6)

def DFS(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            DFS(i)

N, M = map(int, sys.stdin.readline().split())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 0
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1, N+1):
    if not visited[i]:
        visited[i] = 1
        cnt += 1
        DFS(i)
print(cnt)