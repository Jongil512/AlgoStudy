# 부모 찾기

def parents(v):
    q = [v]
    while q:
        t = q.pop(0)
        for i in matrix[t]:
            if not parent[i]:
                parent[i] = t
                q.append(i)

N = int(input())
parent = [0] * (N+1)
matrix = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)
parents(1)
ans = parent[2:]
for i in range(len(ans)):
    print(ans[i])


