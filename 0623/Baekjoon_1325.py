# 효율적인 해킹

def hacking():


N, M = map(int, input().split())
D = [[] for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    D[x] = y
    D[y] = x

min_val = min(map(min, D))
max_val = max(map(max, D))

max_cnt = 0
for num in D:
    