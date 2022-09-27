import sys
sys.stdin = open('12368_input.txt')

def cal_time(h, nh):
    if int(h) + int(nh) >= 24:
        return int(h) + int(nh) - 24
    else:
        return int(h) + int(nh)

T = int(input())
for tc in range(1, T + 1):
    h, nh = input().split()
    print(f'#{tc} {cal_time(h, nh)}')