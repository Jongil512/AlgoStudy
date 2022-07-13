# 나무 탈출

import sys
sys.setrecursionlimit(10**6)

def DFS(v):
    global cnt
    for i in parent[v]:
        if parent[i]:
            cnt += 1
            DFS(i)


N = int(sys.stdin.readline().rstrip())
parent = [[] for _ in range(N+1)]
child = [[] for _ in range(N+1)]

cnt = 0

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    child[a].append(b)
    parent[b].append(a)
    # if a < b:
    #     child[a].append(b)
    #     parent[b].append(a)
    # else:
    #     child[b].append(a)
    #     parent[a].append(b)
for i in range(1, len(child)):
    if not child[i]:
        cnt += 1
        DFS(i)

ans = "No"

if cnt % 2 == 1:
    ans = "Yes"

print(ans)