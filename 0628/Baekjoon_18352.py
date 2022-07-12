# 특정 거리의 도시 찾기
import sys
from collections import deque

def dist(num, distance):
    q = deque()
    visited[num] = 1
    q.append(num)

    while q:
        t = q.popleft()
        if visited[t] == distance + 1:                          # 최단거리인 도시는 ans 배열에 추가
            ans.append(t)

        for i in matrix[t]:                                 # q에서 빼온 도시와 연결된 모든 도시 큐에 추가
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1                 # visited를 이전 도시 +1

N, M, K, X = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x].append(y)                                     # 단방향 연결

ans = []
dist(X, K)

if len(ans) != 0:                                           # 추가된 도시가 없으면 -1 리턴
    ans.sort()                                              # 하나라도 있으면 정렬 후 출력
    for i in range(len(ans)):
        print(ans[i])
else:
    print(-1)