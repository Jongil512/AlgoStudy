import sys
sys.stdin = open('11736_input.txt')

def common_num():
    cnt = 0
    for i in range(1, N-1):
        lst = arr[i-1:i+2]
        if arr[i] != min(lst) and arr[i] != max(lst):
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {common_num()}')