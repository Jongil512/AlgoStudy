from cgi import test
import sys

sys.stdin = open("odd_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):    

    arr = list(map(int, input().split()))
    # print(arr)
    total = 0
    for item in arr:
        if item % 2 == 1:
            total += item
    print(f'#{test_case} {total}')