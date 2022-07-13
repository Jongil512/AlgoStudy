# 랜선 자르기

import sys

def cut_lan(min_lan, max_lan):
    while min_lan <= max_lan:
        mid = (min_lan + max_lan) // 2
        cnt = 0
        for i in lan:
            cnt += i // mid
        if cnt >= N:
            min_lan = mid + 1
        else:
            max_lan = mid - 1
    return max_lan


K, N = map(int, sys.stdin.readline().rstrip().split())
lan = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

min_lan = 1
max_lan = max(lan)
print(cut_lan(min_lan, max_lan))