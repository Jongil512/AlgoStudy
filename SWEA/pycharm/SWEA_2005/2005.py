import sys
sys.stdin = open('2005_input.txt')

def pascal(n):
    memo = [[0] * (n) for _ in range(n)]
    # pascal_list = [[1]]
    # if n == 1:
    #     return pascal_list
    # else:
    #     for i in range(2, n + 1):
    #         arr = pascal_list[-1]
    #         result = [0] * i
    #         for j in range(i):
    #             if j == 0 or j == i-1:
    #                 result[j] = 1
    #             else:
    #                 result[j] = arr[j] + arr[j-1]
    #         pascal_list.append(result)
    #     return pascal_list
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
    return memo



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = pascal(N)
    print(f'#{tc}')
    for i in range(N):
        print(*pascal(N)[i][:i+1])
