# 바이러스

import sys

def DFS(v):
    global cnt
    cnt += 1
    for i in connection[v]:
        if not visited[i]:
            visited[i] = 1
            DFS(i)

N = int(sys.stdin.readline())
V = int(sys.stdin.readline())
connection = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = -1
for i in range(V):
    x, y = map(int, sys.stdin.readline().split())
    connection[x].append(y)
    connection[y].append(x)
visited[1] = 1
DFS(1)
print(cnt)