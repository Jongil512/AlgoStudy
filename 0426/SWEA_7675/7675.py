import sys
sys.stdin = open('7675_input.txt')

def bible():
    k = 0
    cnt = 0
    for i in range(len(arr)):
        flag = 0
        for j in range(len(arr[i])):
            if arr[i][j].isupper():
                if j == 0:
                    flag = 1
                else:
                    flag = 0
            elif arr[i][j].isupper():
                flag = 0
            elif arr[i][j].isdigit():
                flag = 0
            elif arr[i][j] == '.' or arr[i][j] == '?' or arr[i][j] == '!':
                if flag:
                    cnt += 1
                order[k] = cnt
                k += 1
                flag = 0
                cnt = 0
        if flag:
            cnt += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    order = [0] * N
    bible()
    print(f'#{tc}', *order)