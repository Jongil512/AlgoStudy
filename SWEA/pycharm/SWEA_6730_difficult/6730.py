import sys
sys.stdin = open('6730_input.txt')

def diff(arr, n):
    up_score = 0
    down_score = 0
    for i in range(1, n):
        if arr[i] - arr[i-1] > 0 and arr[i] - arr[i-1] > up_score:
            up_score = arr[i] - arr[i-1]
        if arr[i] - arr[i-1] < 0 and arr[i] - arr[i-1] < down_score:
            down_score = arr[i] - arr[i-1]
    return up_score, abs(down_score)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc}', *diff(arr, N))