import sys
sys.stdin = open('10726_input.txt')

def if_1(m):
    ans = []
    while m >= 2:
        ans.append(m % 2)
        m = m // 2
    ans.append(1)
    flag = 'ON'
    a = ans[:N]
    if len(ans) >= N:
        for i in a:
            if not i:
                flag = 'OFF'
    else:
        flag = 'OFF'
    return flag

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} { if_1(M)}')