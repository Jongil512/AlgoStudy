import sys
sys.stdin = open('3233_input.txt')

# 정삼각형 분할 놀이

def triangle():
    d = int(A / B)
    cnt = 0
    for i in range(d):
        cnt += (2 * i + 1)
    return cnt

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    print(f'#{tc} {triangle()}')