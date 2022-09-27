import sys
sys.stdin = open('11775_input.txt')

def factory(n, k, total):
    global min_v
    if n == k:
        if total <= min_v:
            min_v = total
            return
    elif total >= min_v:
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = i
                factory(n, k+1, total + arr[k][i])
                visited[i] = 0
    return min_v

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [0] * N
    visited = [0] * N
    min_v = 909999
    print(f'#{tc} {factory(N, 0, 0)}')
