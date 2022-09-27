import sys
sys.stdin = open('파리퇴치_input.txt')

def catch_fly(arr, n, m):
    max_fly = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            fly_sum = 0
            for k in range(m):
                for l in range(m):
                    fly_sum += arr[i+k][j+l]
                    if max_fly < fly_sum:
                        max_fly = fly_sum
    return max_fly



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {catch_fly(arr, N, M)}')