import sys
sys.stdin = open('11760_input.txt')

def min_sum(x, y, ssum):
    global min_v
    if x == N - 1 and y == N - 1:
        ssum += arr[x][y]
        if min_v > ssum:
            min_v = ssum
        return min_v
    elif ssum > min_v:
        return
    else:
        ssum += arr[x][y]
        if x + 1 < N:
            min_sum(x + 1, y, ssum)
        if y + 1 < N:
            min_sum(x, y + 1, ssum)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ssum = 0
    min_v = 999999
    min_sum(0, 0, 0)
    print(f'#{tc} {min_v}')