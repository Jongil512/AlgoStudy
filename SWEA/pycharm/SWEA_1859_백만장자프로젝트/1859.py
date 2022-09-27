import sys
sys.stdin = open('1859_input.txt')

def cal_sum(arr, n):
    profit = 0
    max_value = arr[n-1]
    for i in range(n-2, -1, -1):
        if max_value < arr[i]:
            max_value = arr[i]
        else: profit += max_value - arr[i]
    return profit

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {cal_sum(arr, N)}')