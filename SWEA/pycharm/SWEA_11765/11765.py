import sys
sys.stdin = open('11765_input.txt')

def working():
    finish = 0
    ans = 0
    for i in range(N):
        if finish <= arr[i][0]:       # 앞 작업 이후에 시작하면
            ans += 1
            finish = arr[i][1]
    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x:(x[1], x[0]))
    print(f'#{tc} {working()}')