def sqaure(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i

T = int(input())
for tc in range(1, T + 1):
    arr =  list(map(int, input().split()))
    print(f'#{tc} {square(arr)}')