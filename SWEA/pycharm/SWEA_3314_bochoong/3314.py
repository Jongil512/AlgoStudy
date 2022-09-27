import sys
sys.stdin = open('3314_input.txt')

def bochoong(arr):
    for i in range(len(arr)):
        if arr[i] < 40:
            arr[i] = 40
    return int(sum(arr) / len(arr))

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    print(f'#{tc} {bochoong(arr)}')