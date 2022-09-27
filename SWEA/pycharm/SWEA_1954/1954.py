import sys

sys.stdin = open('1954_input.txt')

def snail_nums(arr, st, le, num):
    last = st + le - 1
    for c in range(st, last + 1):
        arr[st][c] = num
        num += 1
    for r in range(st + 1, last + 1):
        arr[r][last] = num
        num += 1
    for c in range(last - 1, st - 1, -1):
        arr[last][c] = num
        num += 1
    for r in range(last - 1, st, -1):
        arr[r][st] = num
        num += 1
    return num


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[0 for j in range(N)] for i in range(N)]
    num, st = 1, 0
    while N > 0:
        num = snail_nums(snail, st, N, num)
        N -= 2
        st += 1
    print(f'#{tc}')
    for arr in snail:
        print(*arr)