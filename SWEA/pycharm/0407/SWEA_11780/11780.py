import sys
sys.stdin = open('11780_input.txt')

def BFS(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        for w in range(N+1):
            if adj[t][w] == 1 and not visited[w]:
                q.append(w)
                visited[w] = 1

def group():
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            BFS(i)
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        adj[arr[2 * i]][arr[2 * i + 1]] = 1
        adj[arr[2 * i + 1]][arr[2 * i]] = 1
    visited = [0]*(N+1)
    print(f'#{tc} {group()}')
