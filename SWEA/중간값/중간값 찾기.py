import sys

sys.stdin = open("middle_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
arr = list(map(int, input().split()))
num = sorted(arr)
print(num[T // 2])
# print(f'#{test_case} {num_list[x]}')
