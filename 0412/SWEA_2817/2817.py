import sys
sys.stdin = open('2817_input.txt')

def asd(idx, ssum):
    global cnt

    if idx >= N:
        return

    ssum += arr[idx]

    if ssum == K:
        cnt += 1

    asd(idx + 1, ssum)
    asd(idx + 1, ssum - arr[idx])

    return cnt

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    asd(0, 0)
    print(f'#{tc} {cnt}')