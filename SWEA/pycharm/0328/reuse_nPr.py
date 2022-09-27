def perm(n, k):     # n: 배열 크기, k: 깊이
    if n == k:
        print(*p)
    else:
        for i in range(n):
            p[k] = arr[i]
            perm(n, k+1)

arr = [1, 2, 3]
N = len(arr)
p = [0] * N
used = [0] * N
perm(N, 0)

