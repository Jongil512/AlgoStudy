import sys
sys.stdin = open('3260_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {N+M}')