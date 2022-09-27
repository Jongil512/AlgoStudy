import sys
sys.stdin = open('11927_input.txt')

def in_order(n):
    global start
    if n <= N:
        in_order(n * 2)
        tree[n] = start
        start += 1
        in_order(n * 2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    start = 1
    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')