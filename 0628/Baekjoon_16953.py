# A -> B
import sys
from collections import deque

def BFS(v):
    q = deque()
    q.append(v)
    while q:
        t = q.popleft()
        a, cnt = t[0], t[1]
        if a > B:
            continue
        if a == B:
            return cnt
        q.append((a*2, cnt+1))
        q.append((int(str(a)+"1"), cnt+1))
    return -1

A, B = map(int, sys.stdin.readline().split())
print(BFS((A, 1)))
