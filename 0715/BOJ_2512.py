# 예산

import sys

def BS(s ,e):
    max_value = 0
    while s <= e:
        mid = (s + e) // 2
        ssum = 0
        for i in budgets:
            if mid < i:
                ssum += mid
            else:
                ssum += i
        if ssum > K:
            e = mid - 1
        else:
            max_value = mid
            s = mid + 1
    return max_value


N = int(sys.stdin.readline().rstrip())
budgets = list(map(int, sys.stdin.readline().rstrip().split()))
K = int(sys.stdin.readline().rstrip())

budgets.sort()

s = 1
e = max(budgets)

print(BS(s, e))