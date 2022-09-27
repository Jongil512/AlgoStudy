import sys
sys.stdin = open('5789_input.txt')

def box_change():
    for i in range(1, Q+1):
        L = command[i][0]
        R = command[i][1]
        for j in range(L, R+1):
            arr[j] = i
    return arr[1:]

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    command = [[0] * Q] + [list(map(int, input().split())) for _ in range(Q)]
    arr = [0] * (N + 1)
    print(f'#{tc}', *box_change())