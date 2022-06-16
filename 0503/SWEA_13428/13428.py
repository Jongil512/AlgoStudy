import sys
sys.stdin = open('13428_input.txt')

# 숫자 조작

def find_min(n):
    min_arr = list(n)
    min_idx = 0
    for i in range(len(min_arr) - 1):
        max_idx = i
        for j in range(i + 1, len(min_arr)):
            if min_arr[i] > min_arr[j]:
                if i != 0:
                    if min_arr[min_idx] >= min_arr[j]:
                        min_idx = j
                else:
                    if min_arr[min_idx] >= min_arr[j] and min_arr[j] != '0':
                        min_idx = j
        if min_idx != 0:
            min_arr[max_idx], min_arr[min_idx] = min_arr[min_idx], min_arr[max_idx]
            return ''.join(min_arr)

    return ''.join(min_arr)

def find_max(n):
    max_arr = list(n)
    max_idx = 0
    for i in range(len(max_arr) - 1):
        min_idx = i
        for j in range(i + 1, len(max_arr)):
            if max_arr[i] < max_arr[j]:
                if max_arr[max_idx] <= max_arr[j]:
                    max_idx = j
        if max_idx != 0:
            max_arr[max_idx], max_arr[min_idx] = max_arr[min_idx], max_arr[max_idx]
            return ''.join(max_arr)

    return ''.join(max_arr)

T = int(input())
for tc in range(1, T + 1):
    N = input()
    if N == '0':
        print(f'#{tc} 0 0')
    else:
        print(f'#{tc}', find_min(N), find_max(N))