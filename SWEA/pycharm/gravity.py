import sys
sys.stdin = open('gravity_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        # i의 최대낙차값믄 N-1-i
        # i이후의 모든 행을 검사
        max_height = N - 1 - i
        for j in range(i+1, N):
            # 아래행이 1행보다 상자가 많거나 같으면 최대낙차값에서 -1
            if arr[i] <= arr[j]:
                max_height -= 1
        # 낙차값의 최댓값을 구하기
        if ans < max_height:
            ans = max_height

    print(f'#{tc} {ans}')