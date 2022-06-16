def kangaroo():
    cnt = 0
    flag = 1
    while flag:
        A = arr[1] - arr[0]
        B = arr[2] - arr[1]
        if A < B:
            arr[0] = arr[1]
            arr[1] = arr[1] + 1
            cnt += 1
        else:
            arr[2] = arr[1]
            arr[1] = arr[2] - 1
            cnt += 1



T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))