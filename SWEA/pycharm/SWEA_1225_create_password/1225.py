import sys
sys.stdin = open('1225_input.txt')

def create_password(Q):
    global cnt
    while True:
        temp = Q.pop(0)
        temp -= cnt % 5 + 1
        if temp < 0:
            temp = 0
        Q.append(temp)
        cnt += 1
        if temp == 0:
            break
    return Q

T = 10
for tc in range(1, T+1):
    N = int(input())
    Q = list(map(int, input().split()))
    cnt = 0
    create_password(Q)
    print(f'#{tc}', end=' ')
    print(*create_password(Q))