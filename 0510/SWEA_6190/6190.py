import sys
sys.stdin = open('6190_input.txt')

# 단조 증가하는 수

def danzo():
    max_num = 0
    for i in range(len(arr)-1):
        flag = 0
        num = str(int(arr[i]) * int(arr[i+1]))
        if len(num) == 1:
            flag = 1
        for j in range(len(num)-1):
            if num[j] > num[j+1]:
                break
            elif num[j] == num[j+1]:
                continue
            else:
                flag = 1
        if flag:
            if int(num) > int(max_num):
                max_num = num
    return max_num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    print(f'#{tc} {danzo()}')