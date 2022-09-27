import sys
sys.stdin = open('1232_input.txt')

def post_order(n):
    if n < N and ch1[n] and ch2[n]:
        post_order(ch1[n])
        post_order(ch2[n])
        if sym[n] == '+':
            s[n] = s[ch1[n]] + s[ch2[n]]
        elif sym[n] == '*':
            s[n] = s[ch1[n]] * s[ch2[n]]
        elif sym[n] == '-':
            s[n] = s[ch1[n]] - s[ch2[n]]
        elif sym[n] == '/':
            s[n] = s[ch1[n]] / s[ch2[n]]
    return
            

T = 10
for tc in range(1, T+1):
    N = int(input())
    sym = [''] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    s = [0] * (N + 1)
    for i in range(1, N+1):
        arr = list(input().split())
        if len(arr) != 2:
            sym[i] = arr[1]
            ch1[i] = int(arr[2])
            ch2[i] = int(arr[3])
        else:
            s[i] = int(arr[1])
    post_order(1)
    print(f'#{tc} {int(s[1])}')