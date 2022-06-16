import sys
sys.stdin = open('5642_input.txt')
# 합
def ssum(): 1 3 -8 18 -8
    for i in range(1, N):
        ssum_lst[i] = max(arr[i], ssum_lst[i-1] + arr[i])
    return max(ssum_lst)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ssum_lst = [-1000] * N
    ssum_lst[0] = arr[0]
    print(f'#{tc} {ssum()}')