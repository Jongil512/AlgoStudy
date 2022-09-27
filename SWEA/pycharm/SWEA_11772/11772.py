import sys
sys.stdin = open('11772_input.txt')

def binary(arr, l_cnt, r_cnt, target):
    start = 0
    end = len(arr) - 1
    dir = -1

    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            ans.append(target)
            return
        elif target < arr[mid]:
            if dir == 0:
                return
            dir = 0
            end = mid - 1
        elif target > arr[mid]:
            if dir == 1:
                return
            dir = 1
            start = mid + 1
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    ans = []
    for i in B:
        if i in A:
            binary(A, 0, 0, i)
    print(f'#{tc}', len(ans))