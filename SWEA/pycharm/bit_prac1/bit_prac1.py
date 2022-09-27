# 0,120,12,7,76,24,60,121,124,103

import sys
sys.stdin = open('input.txt')

arr = list(map(int, input()))
ans = []
for i in range(len(arr)//7):
    n = 0
    for j in range(7):
        n = n * 2 + arr[j]
    ans.append(n)
    arr = arr[7:]
print(*ans)