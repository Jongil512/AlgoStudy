import sys

sys.stdin = open('Flatten_input.txt')

def solve(arr, dump):
    for i in range(dump):
        max_idx = 0
        min_idx = 0
        for j in range(1, 100):
            if arr[max_idx] < arr[j]:
                max_idx = j
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[max_idx] -= 1
        arr[min_idx] += 1

    max_value = arr[0]
    min_value = arr[0]
    for i in range(1, 100):
        if max_value < arr[i]:
            max_value = arr[i]
        if min_value > arr[i]:
            min_value = arr[i]

    return max_value - min_value
#
#
T = 10

for tc in range(1, T + 1):
    N = int(input())
    box = list(map(int, input().split()))
    ans = solve(box, N)
    print(f'#{tc} {ans}')

    # max_idx = 0
    # min_idx = 0
    # for i in range(N):
    #     for j in range(len(box)):
    #         if box[max_idx] < box[j]:
    #             max_idx = j
    #         if box[max_idx] < box[j]:
    #             min_idx = j
    #
    # for x in range(N):
    #     for y in range(len(box)):
    #         if box[y] == min_n(box):
    #             box[y] += 1
    #             break
    #
    # print(f'#{tc} {max_n(box) - min_n(box)}')