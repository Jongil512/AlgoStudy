import sys
sys.stdin = open('1979_input.txt')

def word_insert(words, n, k):
    ans = 0
    for i in range(n + 1):
        row_cnt = 0
        col_cnt = 0
        for j in range(n + 1):
            if words[i][j] == 1:
                row_cnt += 1
            else:
                if row_cnt == k:
                    ans += 1
                row_cnt = 0
            if words[j][i] == 1:
                col_cnt += 1
            else:
                if col_cnt == k:
                    ans += 1
                col_cnt = 0
    return ans

T = int(input())

for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0]*(N+1))
    # print(arr)
    print(f'#{tc} {word_insert(arr, N, K)}')