# 수 찾기

import sys

def BST(v):
    start = 0
    end = len(arr)-1
    middle = (start + end) // 2
    while True:
        if arr[middle] == v:
            return 1
        else:
            if start == end:
                return 0
        if arr[start] <= v < arr[middle]:
            end = middle
            middle = (start + end) // 2
        else:
            start = middle + 1
            middle = (start + end) // 2


N = sys.stdin.readline().rstrip()
arr = list(map(int, sys.stdin.readline().rstrip().split()))
M = sys.stdin.readline().rstrip()
search = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

for i in search:
    print(BST(i))
