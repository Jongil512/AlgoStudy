import sys
sys.stdin = open('11883_input.txt')

def perm_least_sum(n, k, cur_sum):
    global min_v
    # 가지치기
    if min_v < cur_sum:
        return

    # 순열코드
    if k == n:
        if min_v > cur_sum:
            min_v = cur_sum
    else:
        for i in range(k, n):
            A[k], A[i] = A[i], A[k]
            perm_least_sum(n, k+1, cur_sum + arr[k][A[k]])
            A[k], A[i] = A[i], A[k]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 65496842
    A = list(range(N)) # 0 1 2
    perm_least_sum(N, 0, 0)
    print(f'#{tc} {min_v}')