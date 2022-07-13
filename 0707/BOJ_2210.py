# 숫자판 점프

import sys
sys.setrecursionlimit(10 ** 6)

def DFS(x, y, cnt, num):
    if cnt == 5:
        if num not in ans:
            ans.append(num)
        return
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            DFS(nx, ny, cnt+1, num + maap[nx][ny])


maap = [list(map(str, sys.stdin.readline().rstrip().split())) for _ in range(5)]
ans = []
for i in range(5):
    for j in range(5):
        DFS(i, j, 0, maap[i][j])

print(len(ans))