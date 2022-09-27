import sys
sys.stdin = open('1289_input.txt')

def restore(arr):
    cnt = 0
    for i in range(len(arr)-1):
        if arr[i+1] != arr[i]:
            cnt += 1
    if arr[0] == '1':
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    bits = list(input())
    print(f'#{tc} {restore(bits)}')