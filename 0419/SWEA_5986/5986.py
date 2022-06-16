# 새샘이와 세 소수

import sys
sys.stdin = open('5986_input.txt')

def saesam(k, n, ssum):
    global ans, cnt
    global used
    nums = []
    if ssum == n:
        if len(nums) == k:
            cnt += 1
            nums = []
    for i in range(len(lst)):
        if not used[i]:
            nums.append(i)
            used[i] = 1
            ssum += lst[i]
            saesam(k, n, ssum)
            used[i] = 0
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    ans = []
    used = [0] * len(lst)
    cnt = 0
    print(f'#{tc} {saesam(0, N, 0)}')