def counting_sort(A, B, K):
    # 카운팅
    C = [0] * (K+1)
    for i in range(0, len(A)):
        C[A[i]] += 1

    # 누적
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]

    # 배치
    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1


# 입력 리스트
arr = [0, 4, 1, 3, 1, 2, 4, 1]

# 정렬된 리스트
b = [0] * len(arr)
counting_sort(arr, b, 4)
print(b)
