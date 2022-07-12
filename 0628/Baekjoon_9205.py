# 맥주 마시면서 걸어가기

import sys
from collections import deque

def beer(v):
    q = deque()
    q.append(v)
    visited[0] = 1
    while q:
        t = q.popleft()
        x1, y1 = t[0], t[1]
        if x1 == arr[-1][0] and y1 == arr[-1][1]:
            return "happy"
        for i in range(1, len(arr)):
            if abs(x1 - arr[i][0]) + abs(y1 - arr[i][1]) <= 1000 and not visited[i]:
                q.append(arr[i])
                visited[i] = 1
    return "sad"

T = int(sys.stdin.readline())
for tc in range(T):
    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N+2)]
    visited = [0]*(N+2)
    print(beer(arr[0]))