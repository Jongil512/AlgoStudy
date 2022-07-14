# 게임

import sys

def BS(s, e):
    rst = 0
    Z = int((Y * 100) / X)
    if Z == 99 or Z == 100:
        return -1
    while s <= e:
        mid = (s + e) // 2
        if int((Y + mid) / (X + mid) * 100) > Z:
            rst = mid
            e = mid - 1
        else:
            s = mid + 1
    return rst


X, Y = map(int, sys.stdin.readline().rstrip().split())

s = 1
e = 1000000000
cnt = 0

print(BS(s, e))