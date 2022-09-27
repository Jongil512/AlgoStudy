import sys
from collections import deque
sys.stdin = open('11779_input.txt')

def cal(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        t = q.popleft()
        if t == M:
            return visited[t]-1
        for i in range(4):
            if i == 2 and 0 <= (t*2) <= 1000000 and visited[t * 2] == 0:
                q.append(t * 2)
                visited[t * 2] = visited[t] + 1
            elif 0 <= (t+delta[i]) <= 1000000 and visited[t + delta[i]] == 0:
                q.append(t + delta[i])
                visited[t + delta[i]] = visited[t] + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    delta = [1, -1, 2, -10]
    print(f'#{tc} {cal(N)}')