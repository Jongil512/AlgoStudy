import sys
sys.stdin = open('11926_input.txt')

def subtree(n):
    global cnt
    if ch1[n] != 0:
        cnt += 1
        subtree(ch1[n])
    if ch2[n] != 0:
        cnt += 1
        subtree(ch2[n])
    return cnt

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)
    cnt = 1
    for i in range(E):
        if ch1[arr[i*2]] == 0:
            ch1[arr[i*2]] = arr[i*2+1]
        else:
            ch2[arr[i * 2]] = arr[i*2+1]
    print(f'#{tc} {subtree(N)}')