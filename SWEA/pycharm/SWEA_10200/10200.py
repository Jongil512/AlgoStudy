import sys
sys.stdin = open('10200_input.txt')

def subscribe():
    max_b = min_b = 0
    if A + B <= N:
        max_b = min(A, B)
        min_b = 0
    elif A + B > N:
        max_b = min(A, B)
        min_b = (A + B) - N
    return (max_b, min_b)

T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    print(f'#{tc}', *subscribe())