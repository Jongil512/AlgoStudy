import sys
sys.stdin = open('1865_input.txt')

def perm(k, max_v):
    global ans
    if max_v <= ans:
        return
    if k == N:
        if ans < max_v:
            ans = max_v
        else:
            for i in range(N):
                if v[i] == 0:
                    v[i] = 1
                    perm(k+1, max_v * (arr[k][i]/100))
                    v[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    ans = 0
    perm(0, 1)
    print(f'#{tc} {ans * 100:0.6f}')