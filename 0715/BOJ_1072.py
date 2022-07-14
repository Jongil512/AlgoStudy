# 게임

import sys
import math

def BS(s, e):
    global cnt
    rate = Y / X
    Z = math.trunc(rate * 100)
    if Z == 99 or Z == 100:
        return -1
    while s <= e:
        mid = (s + e) // 2
        if math.trunc((Y + mid / X + mid) * 100) == Z:
            s = mid + 1
        else:
            cnt = mid
            e = mid - 1
    return cnt

X, Y = map(int, sys.stdin.readline().rstrip().split())

s = 1
e = 1000000000
cnt = 0

print(BS(s, e))