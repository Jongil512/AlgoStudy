import sys

sys.stdin = open("big_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    big = arr[0]
    for item in arr:
        if item > big:
            big = item
    print(f'#{test_case} {big}')
