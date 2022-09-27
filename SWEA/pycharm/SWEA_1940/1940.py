import sys
sys.stdin = open('1940_input.txt')

def RCcar(arr, n):
    d = 0
    v = 0
    for i in range(n):
        data = arr[i]
        if data[0] == 1:
            v += data[0] * data[1]
        elif data[0] == 2:
            if v > 0 and v >= data[1]:
                v -= data[1]
            elif v < data[1]:
                v = 0
        d += v
    return d

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {RCcar(arr, N)}')