def f(k, N):
    global cnt
    if k == N:
        cnt += 1
        print(p, cnt)
    else:
        for i in range(k, N):
            p[k], p[i] = p[i], p[k]
            f(k+1, N)
            p[k], p[i] = p[i], p[k]

N = 5
cnt = 0
p = [x for x in range(1, N+1)]
f(0, N)