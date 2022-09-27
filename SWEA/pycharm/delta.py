import sys

sys.stdin = open('delta.txt')

def take_abs(arr, n, m):
    sum_num = 0
    for i in range(n):
        for j in range(m):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if arr[ni][nj] > arr[i][j]:
                        sum_num += arr[ni][nj] - arr[i][j]
                    else:
                        sum_num += arr[i][j] - arr[ni][nj]
    return sum_num

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = take_abs(arr, N, M)
    print(ans)
