import sys
sys.stdin = open('6485_input.txt')

def bus_stop(n):
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b + 1):
            cnt[j] += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = [0] * (5000 + 1)
    ans = bus_stop(N)
    P = int(input())
    print(f'#{tc}', end=' ')
    for i in range(P):
        print(cnt[i + 1], end=' ')
    print()