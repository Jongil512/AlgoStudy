# 암호 만들기

import sys

def password(v):
    if v == L:
        ans.append(''.join(pw))
        return

    for i in range(L):
        if visited[i] == 0:
            pw[]



L, C = map(int, sys.stdin.readline().rstrip().split())
alpha = list(map(str, sys.stdin.readline().rstrip().split()))
need = ['a', 'e', 'i', 'o', 'u']
alpha.sort()
visited = [0]*L
pw = ['']*L
ans = []