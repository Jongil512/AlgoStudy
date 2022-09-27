import sys
sys.stdin = open('13988_input.txt')

def triple():
    for i in range(1, N+1):
        if i ** 3 == N:
            return i
        elif i ** 3 > N:
            return -1
    return -1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {triple()}')