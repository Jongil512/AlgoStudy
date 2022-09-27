import sys
sys.stdin = open('1209_input.txt')

def sums(arr):
    max_value = 0
    for i in range(N):
        total = 0
        for j in range(N):
            total += arr[i][j]
            if total > max_value:
                max_value = total
        total = 0
        for j in range(N):
            total += arr[j][i]
            if total > max_value:
                max_value = total

    total = 0
    for i in range(N):
        total += arr[i][i]
        if total > max_value:
            max_value = total

    for i in range(N):
        total = 0
        for j in range(N-1, -1, -1):
            total += arr[i][j]
            if total > max_value:
                max_value = total
    return max_value


T = 10
for tc in range(1, T+1):
    dum = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {sums(arr)}')