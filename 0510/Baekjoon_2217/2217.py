# 로프

def rope(n):
    arr.sort()
    ans = []
    for i in arr:
        ans.append(n*i)
        n -= 1
    return max(ans)

N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
print(rope(N))