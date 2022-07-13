# 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**5)

def DFS(v):
    for i in matrix[v]:
        if i != 1 and not used[i]:
            parent[i] = v
            used[i] = 1
            DFS(i)

N = int(sys.stdin.readline().rstrip())
parent = [0] * (N+1)
used = [0] * (N+1)
matrix = [[] for _ in range(N+1)]
for i in range(N-1):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    matrix[x].append(y)
    matrix[y].append(x)
used[1] = 1
DFS(1)
for i in range(2, N+1):
    print(parent[i])