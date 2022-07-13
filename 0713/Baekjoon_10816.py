# 숫자 카드2

import sys

def BS(s, e, k, t):
    cnt = 0
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == k:
            cnt += 1
            visited[mid] = 1
            for idx in (-1, 1):
                while 0 <= mid+idx < N and arr[mid+idx] == k:
                    if not visited[mid+idx]:
                        visited[mid+idx] = 1
                        mid = mid + idx
                        cnt += 1
                    else:
                        mid = mid + idx
            ans[t] = cnt
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
visited = [0]*N

arr.sort()
s = 0
e = len(arr) - 1
ans = [0]*M

for i in range(M):
    BS(s, e, check[i], i)

print(*ans)