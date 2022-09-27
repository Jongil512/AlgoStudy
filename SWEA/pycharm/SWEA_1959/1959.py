import sys
sys.stdin = open('numbers_input.txt')

T = int(input())

for tc in range(1, T + 1):
    a, b = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    check_list = []

    if len(A) < len(B):
        while len(B) >= len(A):
            multi_sum = 0
            for i in range(a):
                multi_sum += (A[i] * B[i])
            check_list.append(multi_sum)
            B = B[1:]
    else:
        while len(B) <= len(A):
            multi_sum = 0
            for i in range(b):
                multi_sum += (A[i] * B[i])
            check_list.append(multi_sum)
            A = A[1:]
    max_v = 0
    for nums in check_list:
        if max_v < nums:
            max_v = nums
    print(f'#{tc} {max_v}')