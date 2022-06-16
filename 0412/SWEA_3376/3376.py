import sys
sys.stdin = open('3376_input.txt')

# 파도반수열

def pado():
    start = [1, 1, 1, 2, 2]     # 초기값 세팅
    i = 5
    while i <= N:               # N번째 수는 (N-5)번째 수 + (N-1)번째 수
        start.append((start[i - 5]) + (start[i - 1]))
        i += 1
    return start[N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {pado()}')