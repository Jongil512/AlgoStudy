import sys

sys.stdin = open('1966_input.txt')

def sort_nums(arr, n):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    print(f'#{tc}', *sort_nums(nums, N))