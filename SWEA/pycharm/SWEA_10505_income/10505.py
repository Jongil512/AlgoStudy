import sys
sys.stdin = open('10505_input.txt')

def income(arr):
    cnt = 0
    avg = sum(arr) / N
    for i in arr:
        if i < avg:
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {income(arr)}')