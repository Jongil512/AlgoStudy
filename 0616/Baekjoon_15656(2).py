N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
result = []

def perm(depth, n, m):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        result.append(arr[i])
        perm(depth+1, n, m)
        result.pop()

perm(0, N, M)