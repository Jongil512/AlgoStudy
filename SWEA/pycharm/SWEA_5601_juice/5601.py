import sys
sys.stdin = open('5601_input.txt')

def juice(n):
    return f'1/{n}'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}', end=' ')
    for i in range(N):
        print(juice(N), end=' ')
    print()