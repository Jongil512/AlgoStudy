import sys
sys.stdin = open('view_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(2, N-2):
        max_height = 0
        check_list = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
        for num in check_list:
            if max_height < num:
                max_height = num
        if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i + 1] < arr[i] and arr[i + 2] < arr[i]:
            cnt += arr[i] - max_height
    print(f'#{tc} {cnt}')