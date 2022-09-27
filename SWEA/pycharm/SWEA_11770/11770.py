import sys
sys.stdin = open('11770_input.txt')

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    less_lst, equal_lst, bigger_lst = [], [], []
    for i in arr:
        if i > pivot:
            bigger_lst.append(i)
        elif i < pivot:
            less_lst.append(i)
        else:
            equal_lst.append(i)
    return quicksort(less_lst) + equal_lst + quicksort(bigger_lst)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = quicksort(arr)
    print(f'#{tc} {ans[N//2]}')