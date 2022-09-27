# nPr

def perm(n, r, k):    # n: 배열 크기, k: 깊이
    if r == k:
        print(*p)
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = arr[i]
                perm(n, r, k+1)
                visited[i] = 0

arr = [1, 2, 3, 4]
N = len(arr)
R = 2
p = [0] * R
visited = [0] * N
perm(N, R, 0)

# 1을 고정하고 나머지만 순열 -> 고정 후 나머지를 돌리는 것
p[0] = arr[0]
visited[0] = 1
perm(N, R, 1)