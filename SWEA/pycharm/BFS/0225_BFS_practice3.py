import sys
sys.stdin = open('practice3_input.txt')

def practice3(adj, v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        print(f'-{t}', end='')
        for w in range(N+1):
            if adj[t][w] == 1 and visited[w] == 0:
                q.append(w)
                visited[w] = 1

N = int(input())
arr = list(map(int, input().split()))
visited = [0] * (N + 1)
adj = [[0] * (N+1) for _ in range(N+1)]
for i in range(len(arr)//2):
    s, e = arr[2*i], arr[2*i+1]
    adj[s][e] = 1
print(adj)
(practice3(adj, 1))
