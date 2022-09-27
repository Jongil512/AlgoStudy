import sys
sys.stdin = open('1216_input.txt')

def check_palindrome_row(arr, n):
    # 행방향
    m = 100
    while m:
        for i in range(n):
            for j in range(n-m+1):
                flag = 1
                for k in range(m//2):
                    if arr[i][j+k] != arr[i][j+m-1-k]:
                        flag = 0
                        break
                    if flag:
                        return m
        m -= 1

def check_palindrome_col(arr, n):
    # 열방향
    m = 100
    while m:
        for i in range(n):
            for j in range(n - m + 1):
                flag = 1
                for k in range(m // 2):
                    if arr[j + k][i] != arr[j + m - 1 - k][i]:
                        flag = 0
                        break
                    if flag:
                        return m
        m -= 1




T = 10
for tc in range(1, T + 1):
    no = int(input())
    N = 100
    arr = [list(input()) for _ in range(100)]
    print(check_palindrome(arr))