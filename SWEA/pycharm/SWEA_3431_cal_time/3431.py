import sys
sys.stdin = open('3431_input.txt')

def cal_time(l, u, x):
    if x > u:
        return -1
    elif l <= x <= u:
        return 0
    else:
        return l - x

T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split())
    print(f'#{tc} {cal_time(L, U, X)}')