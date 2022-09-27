import sys
sys.stdin = open('1961_input.txt')

def asd(arr, n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = arr[n-1-j][i]
    # new_arr[0].append()
    return arr
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    new_arr = [[0]*N for _ in range(N)]
    arr1 = asd(arr, N)
    arr2 = asd(arr1, N)
    arr3 = asd(arr2, N)
    print(arr3)
