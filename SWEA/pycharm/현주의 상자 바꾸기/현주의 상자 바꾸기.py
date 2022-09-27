import sys
sys.stdin = open('5789_sample_input.txt')

def box_change(n, q):
    lst = [0] * (n + 1)
    for i in range(1, q + 1):
        L, R = map(int, input().split())
        for j in range(L, R + 1):
            lst[j] = i
    return lst[1:]

T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    print(f'#{tc}', *box_change(N, Q))
