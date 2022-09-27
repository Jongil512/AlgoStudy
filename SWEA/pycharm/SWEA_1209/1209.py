import sys
sys.stdin = open('1209_input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_v = 0
    for i in range(100):
        sum_v = 0
        for j in range(100):
            sum_v += arr[i][j]
            if max_v < sum_v:
                max_v = sum_v
    for j in range(100):
        sum_v = 0
        for i in range(100):
            sum_v += arr[i][j]
            if max_v < sum_v:
                max_v = sum_v
    sum_v = 0
    for i in range(100):
        sum_v += arr[i][i]
        if max_v < sum_v:
            max_v = sum_v
    sum_v = 0
    for i in range(100):
        sum_v += arr[i][i]
        if max_v < sum_v:
            max_v = sum_v
    print(f'#{tc} {max_v}')


