# 촌수계산

import sys

def DFS(v, cnt):
    global ans
    visited[v] = 1
    if v == goal:
        ans = cnt
        return
    for i in matrix[v]:
        if not visited[i]:
            DFS(i, cnt+1)

N = int(sys.stdin.readline().rstrip())
start, goal = map(int, sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline().rstrip())
matrix = [[] for _ in range(N+1)]
visited = [0]*(N+1)
ans = -1
for i in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    matrix[x].append(y)
    matrix[y].append(x)
DFS(start, 0)
print(ans)