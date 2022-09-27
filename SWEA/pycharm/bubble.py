def bubble_sort(a, N): # 오름차순
    for i in range(N-1, 0, -1): # 정렬 구간 설정
        for j in range(i):  # 비교할 왼쪽 원소
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    retutn


T = int(input()) #tc 개수
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    bubble_sort(arr, N)
    print(f'#{tc}', end=' ')
    # for x in arr:
    #     print(x, end=' ')
    print(*arr)