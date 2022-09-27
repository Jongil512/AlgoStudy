def f(n, k):        # p[n]을 채우는 순열. k는 배열의 크기
    if n == k:
        print(p)
    else:
        # used에서 사용하지 않은 숫자 검색
        for i in range(k):
            if used[i] == 0:    # 앞에서 사용하지 않은 숫자인 경우
                used[i] = 1     # 사용함으로 바꾸고
                p[n] = a[i]     # 사용
                f(n+1, k)       # 재귀 호출
                used[i] = 0     # a[i]를 다른 위치에서 사용할 수 있도록 다시 사용하지 않은 것으로 바꿈
    return

a = [1, 2, 3]
p = [0] * 3
used = [0] * 3
f(0, 3)