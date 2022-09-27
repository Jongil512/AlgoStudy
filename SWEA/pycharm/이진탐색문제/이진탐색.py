import sys
sys.stdin = open('이진탐색_input.txt')

def binary_search(n, m):
    # 변수 할당
    start = 1
    end = n
    cnt = 0

    while start <= end:
        mid = (start + end) // 2
        # 조건 나누기
        if m > mid:
            start = mid
            cnt += 1
        elif m < mid:
            end = mid
            cnt += 1
        else:
            return cnt

T = int(input())

for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    a = binary_search(N, A)
    b = binary_search(N, B)
    if a > b:
        print(f'#{tc} B')
    elif a < b:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')
