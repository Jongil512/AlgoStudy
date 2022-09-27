import sys
sys.stdin = open('11867_input.txt')

def check_str(arr, n, m):
    for i in range(n):
        for j in range(n - m + 1):
            k = 0
            while k <= m//2:
                if arr[i][j + k] == arr[i][m + j - k - 1]:
                    if k == m//2:
                        return ''.join(arr[i][j:(m + j)])
                    k += 1
                else:
                    break

    for i in range(n):
        for j in range(n):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(n):
        for j in range(n - m + 1):
            k = 0
            while k <= m // 2:
                if arr[i][j + k] == arr[i][m + j - k - 1]:
                    if k == m // 2:
                        return ''.join(arr[i][j:(m + j)])
                    k += 1
                else:
                    break

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    print(f'#{tc}', check_str(arr, N, M))