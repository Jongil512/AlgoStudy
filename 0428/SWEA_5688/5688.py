import sys
sys.stdin = open('5688_input.txt')

def cube_root():
    # M 은 N의 세제곱근, 소수점 5번쨰에서 반올림
    M = round(pow(N, (1.0/3.0)), 5)
    # M이 float형태로 나오기 때문에 float(N)과 비교
    if M * M * M == float(N):
        return int(M)
    else:
        return -1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {cube_root()}')