import sys
sys.stdin = open('부분집합의합_input.txt')

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(arr)

def subsum_check(x, y):
    ans = 0
    for i in range(1 << n):
        s_sum = 0
        cnt = 0
        subsum_list = []
        for j in range(n):
            if i & (1 << j):
                s_sum += arr[j]
                cnt += 1

        if s_sum == y and cnt == x:
            ans += 1
    return ans



T = int(input())

for tc in range(1, T + 1):
    X, Y = map(int, input().split())
    print(f'#{tc} {subsum_check(X, Y)}')