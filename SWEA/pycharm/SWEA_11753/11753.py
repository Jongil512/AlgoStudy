import sys
sys.stdin = open('11753_input.txt')

def asd():
    global N
    S = ''
    cnt = 0
    while N != 0 and cnt < 13:
        N = N * 2
        cnt += 1
        if N >= 1:
            S += '1'
            N -= 1
        else:
            S += '0'

    if cnt >= 13:
        return 'overflow'
    else:
        return S

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    print(f'#{tc} {asd()}')