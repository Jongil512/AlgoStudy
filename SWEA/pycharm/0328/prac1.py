arr = [6, 6, 7 ,7 ,6 ,7]

def baby_gin():
    global flag
    check = 0

    if p[0] == p[1] and p[1] == p[2]: check += 1
    if p[3] == p[4] and p[4] == p[5]: check += 1

    if p[0] + 1 == p[1] and p[1] + 1 == p[2]: check += 1
    if p[3] + 1 == p[4] and p[4] + 1 == p[5]: check += 1

    if check == 2:
        flag = 1
        return

def perm(n, k):
    if flag == 1:
        return

    if n == k:
        baby_gin()
    else:
        # used에서 사용하지 않은 숫자 검색
        for i in range(n):
            if used[i] == 0:    # 앞에서 사용하지 않은 숫자인 경우
                used[i] = 1     # 사용함으로 바꾸고
                p[k] = arr[i]    # 사용
                perm(n, k + 1)       # 재귀 호출
                used[i] = 0     # a[i]를 다른 위치에서 사용할 수 있도록 다시 사용하지 않은 것으로 바꿈
    return

N = len(arr)
p = [0] * N
used = [0] * N
flag = 0
perm(N, 0)
if flag:
    print('Baby-gin')
else:
    print('Not Baby-gin')