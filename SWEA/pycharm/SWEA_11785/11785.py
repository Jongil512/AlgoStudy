import sys

sys.stdin = open('11785_input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    min_v = arr[0]
    max_v = arr[0]

    for num in range(len(arr)):
        if min_v > arr[num]:
            min_v = arr[num]
        if max_v < arr[num]:
            max_v = arr[num]
    print(f'#{tc} {max_v - min_v}')