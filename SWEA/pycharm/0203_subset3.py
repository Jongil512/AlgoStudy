def f(i, N, s, t, rs): # s: 이전까지 고려된 원소의 합, t: 목표값
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
    elif s + rs < t: # 고려할 모든 원소들의 합이 목표값에 못 미치는 경우
        return
    else:
        bit[i] = 1
        f(i+1, N, s+a[i], t, rs - a[i])
        bit[i] = 0
        f(i + 1, N, s, t, rs - a[i])
    return

N = 10
a = [x for x in range(1, N+1)]
bit = [0]*N
cnt = 0
t = 27
s = 0
f(0, N, s, t, sum(a))
print('cnt = ', cnt)