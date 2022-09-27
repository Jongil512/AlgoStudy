T = int(input())
 
for tc in range(1, T + 1):
    P, Q, R, S, W = list(map(int, input().split()))
    a = P * W
    if W > R:
        b = (W - R) * S + Q
    else:
        b = Q
    if a > b:
        print(f'#{tc} {b}')
    else:
        print(f'#{tc} {a}')