import sys
sys.stdin = open('5431_input.txt')

def select_bad(n):
    bad = []
    for i in range(1, n+1):
        if i not in complete:
            bad.append(i)
    bad.sort()

    return bad

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    complete = list(map(int, input().split()))
    print(f'#{tc}', end=' ')
    print(*select_bad(N))