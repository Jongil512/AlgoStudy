import sys
sys.stdin = open('1983_input.txt')

def score(arr, n, k):
    sum_score = []
    for i in range(n):
        total = 0
        total += arr[i][0] * 0.35
        total += arr[i][1] * 0.45
        total += arr[i][2] * 0.2
        sum_score.append(total)

    cnt = 0
    percent = n / 10
    for i in range(len(sum_score)):
        if sum_score[k - 1] < sum_score[i]:
            cnt += 1
    if cnt < percent:
        return 'A+'
    elif cnt < percent * 2:
        return 'A0'
    elif cnt < percent * 3:
        return 'A-'
    elif cnt < percent * 4:
        return 'B+'
    elif cnt < percent * 5:
        return 'B0'
    elif cnt < percent * 6:
        return 'B-'
    elif cnt < percent * 7:
        return 'C+'
    elif cnt < percent * 8:
        return 'C0'
    elif cnt < percent * 9:
        return 'C-'
    else:
        return 'D0'

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {score(arr, N, K)}')