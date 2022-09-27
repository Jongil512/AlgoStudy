# 숫자 카드2

import sys

def BS(s, e, k, t):
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == k:
            ans[t] = match_num[k]
            return
        elif arr[mid] <= k:
            s = mid + 1
        else:
            e = mid - 1
    return


N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
check = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
s = 0
e = len(arr) - 1
ans = [0]*M
match_num = {
}

for num in arr:
    if num in match_num:
        match_num[num] += 1
    else:
        match_num[num] = 1

for i in range(M):
    BS(s, e, check[i], i)

print(*ans)