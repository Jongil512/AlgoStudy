import sys
sys.stdin = open('6692_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    total = 0
    for i in range(N):
        p, x = map(float, input().split())
        total += p * x
    print(f'#{tc} {total}')