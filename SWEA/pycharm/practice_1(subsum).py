arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)

# 부분집합의 합 구하기
cnt = 0
for i in range(1 << n): # i 값을 2진수로 표현 (1 << n)은 2의 n승
    # 값 초기화
    sum = 0
    for j in range(n):
        if i & (1 << j):
            sum += arr[j]

    # sum이 10일 때 출력
    if sum == 10:
        for j in range(n):
            if i & (1 << j):
                print(arr[j], end=', ')
        print()
        cnt += 1
print(cnt)
