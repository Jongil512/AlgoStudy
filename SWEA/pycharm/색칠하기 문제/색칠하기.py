import sys
sys.stdin = open('색칠하기_input.txt')

def puple_cnt(n):
    cnt = 0
    for i in range(n):
        x1, y1, x2, y2, c1 = map(int, input().split())
        for j in range(x1, x2 + 1):
            for k in range(y1, y2 + 1):
                color_sheet[j][k] += c1
                if color_sheet[j][k] == 3:
                    cnt += 1
    return cnt

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    color_sheet = [[0] * 10 for _ in range(10)]
    print(f'#{tc} {puple_cnt(N)}')
