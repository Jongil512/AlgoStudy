import sys
sys.stdin = open('특별한정렬_input.txt')

def spec_list(arr, n):
    # 정렬 시작
    for i in range(n-1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # 새 리스트 생성
    ans_list = [0] * n
    for i in range(n):
        # 인덱스가 짝수인 경우
        if i % 2 == 0:
            ans_list[i] = arr[-(i//2)-1]
        # 인덱스가 홀수인 경우
        if i % 2 != 0:
            ans_list[i] = arr[(i//2)]
    return ans_list


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = spec_list(nums, N)
    print(f'#{tc}', end=' ')
    print(*ans[:10])