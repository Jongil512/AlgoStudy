import sys
sys.stdin = open('1234_input.txt')

def cs_password(n, arr):
    flag = 1
    while flag:
        for i in range(n-1):
            if arr[i] == arr[i+1]:
                arr = arr[:i] + arr[i+2:]
                n = len(arr)
                flag = 1
                break
            else:
                flag = 0
    return arr

T = 10
for tc in range(1, T+1):
    N, arr = input().split()
    print(f'#{tc} {cs_password(int(N), arr)}')