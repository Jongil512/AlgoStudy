import sys
sys.stdin = open('14069_input.txt')

def cooker(n, alst, blst):
    global ans
    if n == N:
        if len(alst) == len(blst):
            asum = bsum = 0
            for i in range(len(alst)):
                for j in range(len(alst)):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            if ans > abs(asum - bsum):
                ans = abs(asum - bsum)
        return

    cooker(n + 1, alst + [n], blst)
    cooker(n + 1, alst, blst + [n])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 12425345
    cooker(0, [], [])
    print(f'#{tc} {ans}')