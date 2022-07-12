# 케빈 베이컨의 6단계 법칙
from collections import deque

def bacon(v):
    q = deque()
    for i in matrix[v]:
        q.append(i)
        visited[i] = visited[v] + 1
    while q:
        t = q.popleft()
        for j in matrix[t]:
            if j != v and not visited[j]:
                q.append(j)
                visited[j] = visited[t] + 1

N, M = map(int, input().split())
matrix = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)
ans = []
max_value = 9999999
min_idx = 0
for i in range(1, N+1):
    visited = [0]*(N+1)
    bacon(i)
    ans.append(sum(visited))
for j in range(len(ans)-1, -1, -1):
    if ans[j] <= max_value:
        max_value = ans[j]
        min_idx = j
print(min_idx + 1)