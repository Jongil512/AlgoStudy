import sys
sys.stdin = open('11885_input.txt')

def pizza():
    idx = N + 1
    while len(Q) > 1:
        p = Q.pop(0)
        C[p] = C[p]//2
        if C[p] != 0:
            Q.append(p)
        elif idx <= M:
            Q.append(idx)
            idx += 1
    return Q

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = [0] + list(map(int, input().split()))
    Q = list(range(1, N+1))
    print(f'#{tc}', *pizza())