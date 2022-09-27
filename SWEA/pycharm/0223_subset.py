def f(i, N, K): # i = 부분집합에 포함될지 결정할 원소의 인덱스, N = 전체 원소갯수, K = 찾는 합
    # --------가지 치기-----------
    if cur_sum > 10:
        return
    # ---------------------------
    if i == N:
        s = 0
        for j in range(N):
            if bit[j] == 1:
                s += arr[j]
        if s == K:
            for j in range(N):
                if bit[j] == 1:
                    print(arr[j], end=' ')
            print()
    else:
        # 두 가지 경우로 나눠 부분집합 찾기
        # i번 요소 포함
        bit[i] = 1
        f(i + 1, N, K, cur_sum + arr[i])
        # i번 요소 포함 안 함
        bit[i] = 0
        f(i + 1, N, K, cur_sum)
    return

# def powerset(n, k): # n: 원소의 길이, k: depth
#     # 기본파트
#     if n == k:
#         print(bit)
#     # 유도파트
#     else:
#         # k번째 요소 포함 유무
#         bit[k] == 1
#         powerset(n, k + 1)
#         bit[k] == 0
#         powerset(n, k + 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
N = len(arr)
bit = [0]*N
cur_sum = 0
f(0, N, 10)
