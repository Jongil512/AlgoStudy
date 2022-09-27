N, K = map(int, input().split())
Q = []
for i in range(1, N+1):
    Q.append(i)
ans = []
while Q:
    for j in range(K-1):
        r = Q.pop(0)
        Q.append(r)
    s = Q.pop(0)
    ans.append(s)
print('<', end='')
for i in range(N-1):
    print(f'{ans[i]}, ', end='')
print(ans[-1], end='')
print('>')