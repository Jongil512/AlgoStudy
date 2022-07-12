# 점프 점프

import sys
# from collections import deque >> list보다 메모리 많이 먹음

def jaewhan(v):
    q.append(v)
    visited[v[0]] = 1               # 이유를 모르겠음 암튼 느림
    while q:
        t = q.pop(0)
        idx, cnt = t[0], t[1]
        if idx >= N-1:
            return cnt
        if miro[idx] == 0:
            continue
        for i in range(1, miro[idx]+1):
            if (idx+i) < N and not visited[idx+i]:
                q.append((idx+i, cnt+1))
                visited[idx+i] = 1
    return -1

N = int(sys.stdin.readline())
miro = list(map(int, sys.stdin.readline().split()))
visited = [0]*N
q = []
print(jaewhan((0, 0)))