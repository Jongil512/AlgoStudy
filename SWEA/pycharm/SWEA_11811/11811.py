import sys

sys.stdin = open('11811_input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    num = list(map(int, input()))

    my_list = [0] * 10

    for i in num:
        my_list[i] += 1

    max_idx = 0
    for j in range(len(my_list)):
        if my_list[max_idx] <= my_list[j]:
            max_idx = j

    print(f'#{tc} {max_idx} {my_list[max_idx]}')