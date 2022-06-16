from itertools import product

# N과 M(7)
def perm(arr, m):
    perms = product(arr, repeat=m)
    return perms

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = sorted(list(perm(arr, M)))
for i in ans:
    for j in range(M):
        print(i[j], end=' ')
    print()
