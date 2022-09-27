import sys
sys.stdin = open('prac.txt')

def quicksort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end


    while l <= r:
        while l < r and arr[l] <= pivot:
            l += 1
        while l < r and arr[r] >= pivot:
            r -= 1
        if l < r:
            arr[pivot], arr[l] = arr[l], arr[pivot]


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
