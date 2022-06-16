import sys
sys.stdin = open('3750_input.txt')

def digit_sum(n):
    ssum = 0
    while n >= 1:
        ssum += n % 10
        n //= 10
        if n == 0 and ssum >= 10:
            n = ssum
            ssum = 0
        elif n == 0 and ssum < 10:
            ans.append(ssum)

ans = []
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    digit_sum(N)
for i in range(len(ans)):
    print(f'#{i+1} {ans[i]}')