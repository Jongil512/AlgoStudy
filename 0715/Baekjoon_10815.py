# 숫자 카드

import sys

def BS(s, e, k):
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == k:
            return 1
        elif arr[mid] <= k:
            s = mid + 1
        else:
            e = mid - 1
    return 0


N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
check = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
s = 0
e = len(arr) - 1

for num in check:
    print(BS(s, e, num))