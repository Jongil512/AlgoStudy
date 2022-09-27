import sys
sys.stdin = open('5432_input.txt')

def razer(arr):
    cnt = 0
    ans = 0
    for i in range(len(arr)):
        # 막대기 추가
        if arr[i] == '(':
            cnt += 1
        else:
            # 레이저인 경우
            if arr[i - 1] == '(':
                cnt -= 1
                ans += cnt
            # 막대기 감소
            else:
                cnt -= 1
                ans += 1
    return ans

T = int(input())
for tc in range(1, T + 1):
    arr = list(input())
    print(f'#{tc} {razer(arr)}')