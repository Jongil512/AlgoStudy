# 촌수 계산

def chonsu(v):
    q = [v]
    while q:
        t = q.pop(0)
        if t == goal:
            return visited[goal]
        for i in range(N+1):
            for j in range(N+1):
                if j == t and matrix[i][j] and not visited[i]:
                    q.append(i)
                    visited[i] = visited[t] + 1
    return -1

N = int(input())
start, goal = map(int, input().split())
M = int(input())
matrix = [([0]*(N+1)) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1
print(chonsu(start))