def f(i, N, s, t): # s: 이전까지 고려된 원소의 합, t: 목표값
    global cnt
    cnt += 1
    if s == t: # 목표값을 찾으면
        for j in range(N):
            if bit[j]:
                print(a[j], end=' ')
        print()
    elif i == N: # 더이상 고려할 원소가 없으면
        return
    elif s > t: # 고려한 원소의 합s가 이미 목표치 t를 초과한 경우
        return
    else:
        bit[i] = 1
        f(i + 1, N, s + a[i], t)
        bit[i] = 0
        f(i + 1, N, s, t)
    return

N = 10
a = [x for x in range(1, N+1)]
bit = [0]*N
cnt = 0
t = 10
s = 0
f(0, N, s, t)
print('cnt = ', cnt)