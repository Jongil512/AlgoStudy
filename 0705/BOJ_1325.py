# 효율적인 해킹

import sys
sys.setrecursionlimit(10**6)

def DFS(v):
    global cnt
    for i in matrix[v]:
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            DFS(i)

N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    matrix[y].append(x)

ans = [0]*(N+1)

for i in range(1, N+1):
    visited = [0]*(N+1)
    cnt = 0
    DFS(i)
    ans[i] = cnt

max_cnt = max(ans)

for i in range(len(ans)):
    if ans[i] == max_cnt:
        print(i, end=' ')