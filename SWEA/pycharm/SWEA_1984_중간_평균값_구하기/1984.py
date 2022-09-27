import sys
sys.stdin = open('1984_input.txt')

def median_average(arr):
    min_v = 10000000
    max_v = 0
    total = 0
    for i in arr:
        if i < min_v:
            min_v = i
        if i > max_v:
            max_v = i
        total += i

    ans = total - min_v - max_v
    return round(ans/(len(arr)-2))

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    print(f'#{tc} {median_average(arr)}')