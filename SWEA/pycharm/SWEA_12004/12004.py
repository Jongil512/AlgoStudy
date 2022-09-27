import sys
sys.stdin = open('12004_input.txt')

def double():
    # N을 i로 나눈 나머지가 0이고 몫이 한자릿수이면 'Yes' (i도 한자리수)
    for i in range(1, 10):
        if N % i == 0:
            if 1 <= (N / i) <= 9:
                return 'Yes'
    return 'No'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {double()}')