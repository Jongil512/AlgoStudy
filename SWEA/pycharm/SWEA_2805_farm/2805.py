import sys
sys.stdin = open('2805_input.txt')

def farm(arr, n):
    total = 0
    middle = N//2
    s = e = middle
    for i in range(N):
        for j in range(s, e+1):
            total += int(arr[i][j])
        if i < middle:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    return total

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(f'#{tc} {farm(arr, N)}')